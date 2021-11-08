import os
from datetime import datetime
from flask import Flask, request, jsonify
from qanary_helpers.registration import Registration
from qanary_helpers.registrator import Registrator
from qanary_helpers.qanary_queries import insert_into_triplestore, get_text_question_in_graph, query_triplestore

# TODO: MAY be changed to other config type (e.g. parsing a json file)
SPRING_BOOT_ADMIN_URL = os.environ['SPRING_BOOT_ADMIN_URL']    
SPRING_BOOT_ADMIN_USERNAME = os.environ['SPRING_BOOT_ADMIN_USERNAME']
SPRING_BOOT_ADMIN_PASSWORD = os.environ['SPRING_BOOT_ADMIN_PASSWORD']
SERVICE_HOST = os.environ['SERVICE_HOST']
SERVICE_PORT = os.environ['SERVICE_PORT']
SERVICE_NAME_COMPONENT = os.environ['SERVICE_NAME_COMPONENT']
SERVICE_DESCRIPTION_COMPONENT = os.environ['SERVICE_DESCRIPTION_COMPONENT']
URL_COMPONENT = f"{SERVICE_HOST}" # While using server with permanent external IP address: URL_COMPONENT = f"http://{SERVICE_HOST}:{SERVICE_PORT}"

app = Flask(__name__)


@app.route("/annotatequestion", methods=["POST"])
def qanary_service():
    triplestore_endpoint_url = request.json["values"]["urn:qanary#endpoint"]
    triplestore_ingraph_uuid = request.json["values"]["urn:qanary#inGraph"]
    
    # get question text from triplestore
    question_text = get_text_question_in_graph(triplestore_endpoint_url, triplestore_ingraph_uuid)

    # Start TODO: configure your business logic here and adjust the sparql query
    # if you want to get the question text from the triplestore, you can use the following query: 
    # query_triplestore(triplestore_endpoint_url, your_sparql_query)
    
    # here we simulate that our component created this sparql query:
    sparql_query = """
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        SELECT * WHERE {
        dbr:Angela_Merkel dbo:birthPlace ?uri .
        }
    """
    # and this "generated" query is stored in the triplestore with this INSERT query:
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
                    uuid=triplestore_ingraph_uuid,
                    question_uri=triplestore_endpoint_url,
                    component=SERVICE_NAME_COMPONENT.replace(" ", "-"),
                    sparql_query=sparql_query.replace("\n", "\\n").replace("\"", "\\\""))

    insert_into_triplestore(triplestore_endpoint_url,
                            SPARQLquery)  # inserting new data to the triplestore
    # End TODO

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