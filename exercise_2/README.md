## Context

Text classification has many applications in Natural Language Processing. Specifically, in Question Answering & Chatbots, it can be used as a **Relation (Predicate) Prediction** component.

**Relation (or Predicate)** in terms of knowledge graphs is an edge that is connecting two nodes (or entities). 
For example, having a triple: `<Mona_Lisa> <?> <Leonardo_da_Vinci>` the relation `<?>` is `<Author>` (or e.g. `<Was_Created_By>`). 

In this regard, **Relation Prediction** is the task of recognizing a relation, based on a textual question. In this case, question: `"Who is the author of Mona Lisa?"` has relation `"Author"` (or e.g. `"Was created by"`).

<img src="https://user-images.githubusercontent.com/16652575/137500625-22516edf-0094-48f2-a32a-7b6e4d076f90.png" alt="Example KG by W3C" width="500"/>

We can use Relation Prediction in Knowledge Graph Question Answering systems. Here, the task is directly connected to a Knowledge Graph that we are using. Let's consider our example question: `"Who is the author of Mona Lisa?"` with [DBpedia Knowledge Graph](https://dbpedia.org/). First, we need to determine what named entities are contained in the question using the **NEL** tool. If we use [DBpedia Spotlight](https://www.dbpedia-spotlight.org/), the answer will be: `http://dbpedia.org/resource/Mona_Lisa`. Then, we apply our **Relation Prediciton** algorithm that returns us `http://dbpedia.org/ontology/author`. Now, we have all the data to fulfill our SPARQL query template to fetch the information from the DBpedia Knowledge graph:

```
SELECT ?answer
WHERE
{
  <http://dbpedia.org/resource/Mona_Lisa> <http://dbpedia.org/ontology/author> ?answer .
}
```

The illustrated example of usage of the Relation Prediction task can be applied in your further work with the projects.

## Learning Objectives

* Learn how to implement a question classifier for the Relation Prediction.
* Learn how to evaluate (test) implemented question classifier.
* Learn how to build web services/APIs.

## Task

### Part 1 (Creating a classification algorithm)

Depending on your exercise variant analyze data in `train.csv` and `test.csv` by calculating:
* Number of questions per class;
* Average token number in a question;
* Average character number a question.

Depending on your exercise variant implement a question classification algorithm based on provided training data (see variant). You can use a Rule-Based approach (e.g. keyword classifier) **or** a Machine Learning approach (e.g. Bag of Words + Logistic Regression).

Train (or set up) your algorithm on `train.csv` data. Test the quality of the algorithm on `test.csv` data.

For testing use following metrics: `Precision`, `Recall`, `F1 Score` (averaging type = weighted).

Compare the metrics values while training on non-preprocessed data and preprocessed (see the previous exercise).

In the `README.md` file in your submission include your findings of the datasets analysis and the metrics results.

## Simple ML classifier with Python

```python
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer # Bag of Words
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score


# read our datasets
train = pd.read_csv("Exercise_3/variant_example/train.csv", sep=';')
test = pd.read_csv("Exercise_3/variant_example/test.csv", sep=';')

vectorizer = CountVectorizer() # init vectorizer
vectorizer.fit(train.append(test).question) # "fit" vectorizer on train+test

X_train = vectorizer.transform(train.question) # transform train questions to vectors
X_test = vectorizer.transform(test.question) # transform test questions to vectors
y_train = train.predicate.values # init train target variable
y_test = test.predicate.values # init test target variable

classifier = LogisticRegression() # init classification model
classifier.fit(X_train, y_train) # train the model
y_pred = classifier.predict(X_test) # make predictions for test vectors

f1 = f1_score(y_test, y_pred, average='weighted') # calculate f1 score
print('F1 Score = {0}'.format(f1))

# F1 Score = 0.9859812799120309
```

**Note:** if you use a Machine Learning approach -- compare at least TWO different approaches between each other. For example, use a Logistic Regression model, while generating features using a Bag of Words (BoW) and a TF-IDF. In this case, you're comparing BoW vs TF-IDF while the model stays the same.

### Part 2 (Wrapping the classification algorithm into a Web API)

Now when you have your classificaiton algorithm, you are asked to integrate it inside a Web Service, that satisfies the following:
* Request path name: `/predict`;
* Request type: `POST`;
* Input structure of request: `{'question': 'Question To Classify'}`
* Output structure of request: `{'predicted_relation': 'RELATION'}`

After you establish a Web Service, run all your questions through the `/predict` method and write the predictions into a structured JSON file:

```json
[
    {
        "question": "QuestionText",
        "predicted_relation": "RELATION",
        "true_relation": "RELATION_FROM_test.csv"
    }
]
```

The simple example of the Web Service with FastAPI on Python:

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/predict/")
async def predict(question: str):
    # execute your classification algorithm with question
    output = {'predicted_relation': 'RELATION'}
    return JSONResponse(content=output)
```

Execute `uvicorn web_api:app --host 0.0.0.0 --port 8899` to run it on your PC. Go to http://0.0.0.0:8899/docs to check Swagger UI.

## Guidance / Tutorials

* RDF by W3C: https://www.w3.org/TR/rdf11-primer/
* Keyword based text classification example: https://stackoverflow.com/questions/1490061/classifying-text-based-on-groups-of-keywords
* Classification metrics explained: https://towardsdatascience.com/the-5-classification-evaluation-metrics-you-must-know-aa97784ff226
* [Python] Machine Learning based text classification: https://monkeylearn.com/text-classification/
* [Python] Neural Networks based text classification: https://realpython.com/python-keras-text-classification/
* [Java] Text classificaiton libraries: https://github.com/jatecs/jatecs, https://stackoverflow.com/questions/2821575/java-text-classification-problem
* [Python] Metrics in scikit-learn: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
* [Python] FastAPI docs: https://fastapi.tiangolo.com/
