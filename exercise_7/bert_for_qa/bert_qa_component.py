import os
import json
from datetime import datetime
from flask import Flask, request, jsonify
from qanary_helpers.registration import Registration
from qanary_helpers.registrator import Registrator
from qanary_helpers.qanary_queries import insert_into_triplestore, get_text_question_in_graph, select_from_triplestore
from transformers import AutoTokenizer, TFAutoModelForQuestionAnswering
import tensorflow as tf

SPRING_BOOT_ADMIN_URL = os.environ['SPRING_BOOT_ADMIN_URL']    
SPRING_BOOT_ADMIN_USERNAME = os.environ['SPRING_BOOT_ADMIN_USERNAME']
SPRING_BOOT_ADMIN_PASSWORD = os.environ['SPRING_BOOT_ADMIN_PASSWORD']
SERVICE_HOST = os.environ['SERVICE_HOST']
SERVICE_PORT = os.environ['SERVICE_PORT']
SERVICE_NAME_COMPONENT = os.environ['SERVICE_NAME_COMPONENT']
SERVICE_DESCRIPTION_COMPONENT = os.environ['SERVICE_DESCRIPTION_COMPONENT']
DEFAULT_ANSWER = os.environ['DEFAULT_ANSWER']
URL_COMPONENT = f"{SERVICE_HOST}:{SERVICE_PORT}" # While using server with permanent external IP address: URL_COMPONENT = f"http://{SERVICE_HOST}:{SERVICE_PORT}"

tokenizer = AutoTokenizer.from_pretrained('distilbert-base-cased-distilled-squad')
model = TFAutoModelForQuestionAnswering.from_pretrained('distilbert-base-cased-distilled-squad')

app = Flask(__name__)

def convert_to_json(literal_answer: str):
    return {
        "head": {
            "vars": [
            "answer"
            ]
        },
        "results": {
            "bindings": [
                {
                    "answer": {
                        "type": "literal",
                        "xml:lang": "en",
                        "value": literal_answer
                    }
                }
            ]
        }
    }

@app.route("/annotatequestion", methods=["POST"])
def qanary_service():
    triplestore_endpoint_url = request.json["values"]["urn:qanary#endpoint"]
    triplestore_ingraph_uuid = request.json["values"]["urn:qanary#inGraph"]
    triplestore_outgraph_uuid = request.json["values"]["urn:qanary#outGraph"]
    
    # 1. get question text from triplestore
    question_text = get_text_question_in_graph(triplestore_endpoint_url, triplestore_ingraph_uuid)[0]['text']

    # 2. get text annotation from triplestore
    SPARQLquery = """
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX qa: <http://www.wdaqua.eu/qa#>
        PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        SELECT ?passage
        FROM <{uuid}> 
        WHERE {{
            ?a rdf:type qa:AnnotationOfTextualPassage .
            ?a oa:hasBody ?passage .  
        }}
    """.format(uuid=triplestore_ingraph_uuid)

    response = select_from_triplestore(triplestore_endpoint_url, SPARQLquery)
    text = response['results']['bindings'][0]['passage']['value'] if len(response['results']['bindings']) > 0 else DEFAULT_ANSWER

    # 3. get answer from model
    input_dict = tokenizer(question_text, text, return_tensors='tf', max_length=512, truncation=True)
    outputs = model(input_dict)
    start_logits = outputs.start_logits
    end_logits = outputs.end_logits

    all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
    answer = ' '.join(all_tokens[tf.math.argmax(start_logits, 1)[0] : tf.math.argmax(end_logits, 1)[0] + 1])
    answer.replace(" ##", "")

    if len(answer) == 0 or answer == "[SEP]":
        answer = DEFAULT_ANSWER
    
    # 4. insert into triplestore
    SPARQLquery = """
                    PREFIX dbr: <http://dbpedia.org/resource/>
                    PREFIX dbo: <http://dbpedia.org/ontology/>
                    PREFIX qa: <http://www.wdaqua.eu/qa#>
                    PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    INSERT {{
                    GRAPH <{uuid}> {{
                        ?newAnnotation rdf:type qa:AnnotationOfAnswerSPARQL .
                        ?newAnnotation oa:hasTarget <{question_uri}> .
                        ?newAnnotation oa:hasBody \"{sparql_query}\"^^xsd:string .
                        ?newAnnotation qa:score \"1.0\"^^xsd:float .
                        ?newAnnotation oa:annotatedAt ?time .
                        ?newAnnotation oa:annotatedBy <urn:qanary:{component}> .
                        }}
                    }}
                    WHERE {{
                        BIND (IRI(str(RAND())) AS ?newAnnotation) .
                        BIND (now() as ?time) 
                    }}
                """.format(
                    uuid=triplestore_outgraph_uuid,
                    question_uri=triplestore_endpoint_url,
                    component=SERVICE_NAME_COMPONENT.replace(" ", "-"),
                    sparql_query="dummy query")

    insert_into_triplestore(triplestore_endpoint_url,
                            SPARQLquery)  # inserting new data to the triplestore

    SPARQLquery = """
                    PREFIX qa: <http://www.wdaqua.eu/qa#>
                    PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
                	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
					PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    INSERT {{
                    GRAPH <{uuid}> {{
                        ?b a qa:AnnotationOfAnswerJson ;
                            oa:hasTarget <{question_uri}> ;
                            oa:hasBody ?answer ;
                            oa:annotatedBy <urn:qanary:{component}> ;
                            oa:annotatedAt ?time .
                        ?answer a qa:AnswerJson ;
                                rdf:value "{json_answer}"^^xsd:string .
                        qa:AnswerJson rdfs:subClassOf qa:Answer .
                        }}
                    }}
                    WHERE {{
                        BIND (IRI(str(RAND())) AS ?b) .
                        BIND (IRI(str(RAND())) AS ?answer) .
                        BIND (now() as ?time) .
                    }}
                """.format(
                    uuid=triplestore_outgraph_uuid,
                    question_uri=triplestore_endpoint_url,
                    component=SERVICE_NAME_COMPONENT.replace(" ", "-"),
                    json_answer=json.dumps(convert_to_json(answer), ensure_ascii=False).replace('\\"',"").replace('"', '\\"'))

    insert_into_triplestore(triplestore_endpoint_url,
                            SPARQLquery)  # inserting new data to the triplestore

    return jsonify(request.get_json())


@app.route("/health", methods=["GET"])
def health():
    return "alive"


metadata = {
    "start": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "description": SERVICE_DESCRIPTION_COMPONENT,
    "written in": "Python"
}

print(metadata)

registration = Registration(
    name=SERVICE_NAME_COMPONENT,
    serviceUrl=f"{URL_COMPONENT}",
    healthUrl=f"{URL_COMPONENT}/health",
    metadata=metadata
)

reg_thread = Registrator(SPRING_BOOT_ADMIN_URL, SPRING_BOOT_ADMIN_USERNAME,
                        SPRING_BOOT_ADMIN_PASSWORD, registration)
reg_thread.setDaemon(True)
reg_thread.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
