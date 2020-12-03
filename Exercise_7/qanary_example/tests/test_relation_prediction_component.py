import json
import requests
from qanary_helpers.qanary_queries import query_triplestore


qanary_pipeline_url = "http://webengineering.ins.hs-anhalt.de:43740/startquestionansweringwithtextquestion"

with open("../../variant_1/test.json") as f:
    test = json.load(f)


def get_result(endpoint, in_graph):
    """
    returns a result of Qanary pipeline execution
    SPARQL query can be customized
    """

    SPARQLquery = """
        PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
        SELECT ?p ?o
        FROM <{graph_guid}>
        WHERE 
        {{
            VALUES ?p {{oa:relation}} .
            ?s ?p ?o .
        }}""".format(graph_guid=in_graph)

    result = query_triplestore(endpoint + "/query", in_graph, SPARQLquery)

    return result['results']['bindings']

def ask_result(endpoint, in_graph, expected_result):
    """
    asks if the annotated result is correct
    SPARQL query can be customized
    """
    SPARQLquery = """
        PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX qa: <http://www.wdaqua.eu/qa#>

        ASK
        FROM <{graph_guid}>
        WHERE {{
            ?annotationId rdf:type qa:AnnotationOfInstance .
            ?annotationId oa:relation <{relation_uri}> .
        }}""".format(graph_guid=in_graph, relation_uri=expected_result)

    result = query_triplestore(endpoint + "/query", in_graph, SPARQLquery)

    return result['boolean']

def test_relation_created():
    for q in test[:5]: # take only first 5 questions for the example
        # run Qanary pipeline
        # component has to be started and registered
        response = requests.post(url=qanary_pipeline_url,
                                params={
                                    "question": q['question'],
                                    "componentlist[]": ["relation_prediciton_perevalov"]
                                }).json()

        # get result of the Qanary pipeline execution
        result = get_result(response['endpoint'], response['inGraph'])

        assert len(result) > 0 # assert when result's length equals 0

def test_relation_correct():
    for q in test[:5]: # take only first 5 questions for the example
        # run Qanary pipeline
        # component has to be started and registered
        response = requests.post(url=qanary_pipeline_url,
                                params={
                                    "question": q['question'],
                                    "componentlist[]": ["relation_prediciton_perevalov"]
                                }).json()
        
        # get result of the Qanary pipeline execution
        result = ask_result(response['endpoint'], response['inGraph'], q['predicate'])
        
        assert result == True
