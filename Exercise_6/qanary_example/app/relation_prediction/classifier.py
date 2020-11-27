from flask import Blueprint, jsonify, request
from qanary_helpers.configuration import Configuration
from qanary_helpers.qanary_queries import get_text_question_in_graph, insert_into_triplestore
import pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import SnowballStemmer
from nltk.stem.snowball import EnglishStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
import sys
sys.path.append("..")
from utils import stemmed_words
import nltk
import requests
import json
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
relation_clf = Blueprint('relation_clf', __name__, template_folder='templates')
configfile = "app.conf"

configuration = Configuration(configfile, [
    'servicename',
    'serviceversion'
])

stopWords = text.ENGLISH_STOP_WORDS.union(["book"]) 
stemmer = EnglishStemmer() 
analyzer = CountVectorizer().build_analyzer()
vectorizer = CountVectorizer(analyzer=stemmed_words)

with open("models/classifier.pickle", "rb") as c:
    classifier = pickle.load(c)

with open("models/vectorizer.pickle", "rb") as v:
    vectorizer = pickle.load(v)

@relation_clf.route("/annotatequestion", methods=['POST'])
def qanary_service():
    """the POST endpoint required for a Qanary service"""

    triplestore_endpoint = request.json["values"]["urn:qanary#endpoint"]
    triplestore_ingraph = request.json["values"]["urn:qanary#inGraph"]
    triplestore_outgraph = request.json["values"]["urn:qanary#outGraph"]

    logging.info(
        "endpoint: %s, inGraph: %s, outGraph: %s" % (triplestore_endpoint, triplestore_ingraph, triplestore_outgraph))

    text = get_text_question_in_graph(triplestore_endpoint=triplestore_endpoint, graph=triplestore_ingraph)[0]['text']

    logging.info(f'Question Text: {text}')

    pred = classifier.predict(vectorizer.transform([text]))

    SPARQLquery = """
                    PREFIX qa: <http://www.wdaqua.eu/qa#>
                    PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

                    INSERT {{
                    GRAPH <{uuid}> {{
                        ?a rdf:type qa:AnnotationOfInstance .
                        ?a oa:relation <{relation_uri}> .
                        ?a oa:annotatedBy <urn:qanary:{app_name}> .
                        ?a oa:annotatedAt ?time .
                        }}
                    }}
                    WHERE {{
                        BIND (IRI(str(RAND())) AS ?a) .
                        BIND (now() as ?time) 
                    }}
                """.format(
        uuid=triplestore_ingraph,
        app_name="{0}:{1}:Python".format(configuration.servicename, configuration.serviceversion),
        relation_uri=pred[0]
    )  # building SPARQL query

    logging.info(f'SPARQL: {SPARQLquery}')

    insert_into_triplestore(triplestore_endpoint, triplestore_ingraph,
                            SPARQLquery)  # inserting new data to the triplestore

    return jsonify(request.get_json())


@relation_clf.route("/", methods=['GET'])
def index():
    """an example GET endpoint returning "hello world (String)"""

    logging.info("host_url: %s" % (request.host_url,))
    return "Hi! \n This is Relation Prediction component."
