import json
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import SnowballStemmer
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer  # Bag of Words
from sklearn.feature_extraction.text import TfidfVectorizer  # Bag of Words
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score  # f1
from sklearn.metrics import recall_score  # recall
from sklearn.metrics import precision_score  # precision
from sklearn.feature_extraction import text  # stopwords
import numpy as np
from utils import stemmed_words
from io import StringIO
from nltk.stem.snowball import EnglishStemmer
import pickle


# train prediction model
train = pd.read_csv("train.csv", sep=';')
test = pd.read_csv("test.csv", sep=';')
completeDF = train.append(test)
predicates = completeDF.predicate.drop_duplicates()


stopWords = text.ENGLISH_STOP_WORDS.union(["book"])  # initialize stopwords
# create stemmer
stemmer = EnglishStemmer()
analyzer = CountVectorizer().build_analyzer()


#def stemmed_words(doc):
#    return ([stemmer.stem(w) for w in analyzer(doc) if not w in stopWords])


###########################################################################################
vectorizer = CountVectorizer(analyzer=stemmed_words)  # init vectorizer
vectorizer.fit(train.append(test).question)  # "fit" vectorizer on train+test

# transform train questions to vectors
X_train = vectorizer.transform(train.question)
# transform test questions to vectors
X_test = vectorizer.transform(test.question)
y_train = train.predicate.values  # init train target variable
y_test = test.predicate.values  # init test target variable

classifier = LogisticRegression()  # init classification model
classifier.fit(X_train, y_train)  # train the model
y_pred = classifier.predict(X_test)

with open("classifier.pickle", "wb") as c:
    pickle.dump(classifier, c)
with open("vectorizer.pickle", "wb") as v:
    pickle.dump(vectorizer, v)
predicates.to_csv('predicates.csv', index=False)
print(predicates)
