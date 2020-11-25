import json
import requests
from qanary_helpers.qanary_queries import query_triplestore


qanary_pipeline_url = "http://webengineering.ins.hs-anhalt.de:43740/startquestionansweringwithtextquestion"

with open("../../variant_1/test.json") as f:
    test = json.load(f)

questions = [q['question'] for q in test]


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

def test_relation_created():
    for text in questions[:5]: # take only first 5 questions for the example
        # run Qanary pipeline
        # component has to be started and registered
        response = requests.post(url=qanary_pipeline_url,
                                params={
                                    "question": text,
                                    "componentlist[]": ["relation_prediciton_perevalov"]
                                }).json()

        # get result of the Qanary pipeline execution
        result = get_result(response['endpoint'], response['inGraph'])

        assert len(result) > 0 # assert when result's length equals 0
