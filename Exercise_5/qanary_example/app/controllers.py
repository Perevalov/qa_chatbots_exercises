import json
import requests
from qanary_helpers.qanary_queries import query_triplestore
from flask import Blueprint, request

main_module = Blueprint('main', __name__, url_prefix='/')
qanary_pipeline_url = "http://webengineering.ins.hs-anhalt.de:43740/startquestionansweringwithtextquestion"


def get_text_response(triplestore_endpoint, graph, SPARQLquery):
    """
    Returns result for a given query and endpoint
    """

    text_response = None
    result = query_triplestore(triplestore_endpoint + "/query", graph, SPARQLquery)

    for binding in result['results']['bindings']:
        text_response = binding['o']['value']

    return text_response


def get_final_result(endpoint, in_graph):
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

    return get_text_response(triplestore_endpoint=endpoint,
                             graph=in_graph,
                             SPARQLquery=SPARQLquery)


@main_module.route('/question', methods=['POST'])
def get_question():
    question_text = request.args.get("user_text")

    # run Qanary pipeline
    response = requests.post(url=qanary_pipeline_url,
                             params={
                                 "question": question_text,
                                 "componentlist[]": ["relation_prediciton"]
                             }).json()

    # get result of the Qanary pipeline execution
    result = get_final_result(response['endpoint'], response['inGraph'])

    return json.dumps({'answer': result})
