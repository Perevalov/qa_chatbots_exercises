import pickle
import sys
import json
from sklearn.metrics import f1_score, precision_score, recall_score
sys.path.append("../app")
from utils import stemmed_words

F1_EXPECTED = 0.8
PRECISION_EXPECTED = 0.8
RECALL_EXPECTED = 0.8

with open("../app/relation_prediction/models/classifier.pickle", "rb") as c:
    classifier = pickle.load(c)

with open("../app/relation_prediction/models/vectorizer.pickle", "rb") as v:
    vectorizer = pickle.load(v)

with open("../../variant_1/test.json") as f:
    test = json.load(f)

questions = [q['question'] for q in test]
predicates = [q['predicate'] for q in test]
predictions = classifier.predict(vectorizer.transform(questions))

def test_model_f1_score():
    F1_ACTUAL = f1_score(predicates, predictions, average='weighted')
    assert F1_ACTUAL > F1_EXPECTED # assert if actual f1 score lower than expected

def test_model_precision():
    PRECISION_ACTUAL = precision_score(predicates, predictions, average='weighted')
    assert PRECISION_ACTUAL > PRECISION_EXPECTED # assert if actual precision score lower than expected

def test_model_recall():
    RECALL_ACTUAL = recall_score(predicates, predictions, average='weighted')
    assert RECALL_ACTUAL > RECALL_EXPECTED # assert if actual recall score lower than expected
