## Context

Text classification has many applications in Natural Language Processing. Specifically, in Question-Answering & Chatbots, it can be used as a Relation (Predicate) Prediction component.

## Learning Objectives

* Learn how to implement question classifier.
* Learn how to evaluate (test) implemented question classifier.

## Task

Depending on your exercise variant analyze data in `train.csv` and `test.csv` by calculating:
* Number of questions per class;
* Average token number in a question;
* Average character number a question.

Depending on your exercise variant implement a question classification algorithm based on provided training data (see variant). You can use a Rule-Based approach (e.g. keyword classifier) **or** a Machine Learning approach (e.g. Bag of Words + Logistic Regression).

Train (or set up) your algorithm on `train.csv` data. Test the quality of the algorithm on `test.csv` data.

For testing use following metrics: `Precision`, `Recall`, `F1 Score` (averaging type = weighted).

In the README.md file in your submission include your findings of the datasets analysis and the metrics results.

**OPTIONAL:** compare the metrics values while training on non-preprocessed data and preprocessed (see previous exercise).

## Simple ML classifier with Python

```
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

**Note:** if you use a Machine Learning approach -- compare at least TWO different approaches between each other. For example, use a Logistic Regression model, while generating features using a Bag of Words (BoW) and a TF-IDF. In this case you're comparing BoW vs TF-IDF while the model stays the same.

## Guidance / Tutorials

* Keyword based text classification example: https://stackoverflow.com/questions/1490061/classifying-text-based-on-groups-of-keywords
* Machine Learning based text classification: https://monkeylearn.com/text-classification/
* Neural Networks based text classification: https://realpython.com/python-keras-text-classification/
* Metrics for testing: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
