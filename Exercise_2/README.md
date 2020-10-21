## Context

Analyzing and processing Natural Language is one of the basic things in the Question Answering and Chatbots field.

## Learning Objectives

* Learn how to preprocess Natural Language texts.
* Learn how to use Named Entity Linking tools (DBpedia Spotlight).

## Task

Depending on your exercise variant write a script, which takes for input a list of questions and outputs for each question:
* preprocessed question (tokenization, stopwords and special characters removing, lemmatization);
* a dictionary `{'uri': 'text'}` of linked named entities from the question (use DBpedia Spotlight). 

The format of the script output is a JSON file with the following structure:

```
[
    {
        'id': '4831',
        'question_text': 'In what wars was Steve Buyer involved?',
        'question_text_preprocessed': ['In', 'war', 'Steve', 'Buyer', 'involved'],
        'named_entities': {'http://dbpedia.org/resource/Steve_Buyer': 'Steve Buyer'},
        'named_entities_preprocessed': {'http://dbpedia.org/resource/Steve_Buyer': 'Steve Buyer'}
    },
    {
        'id': '4635',
        'question_text': 'What is the occupation of the Irving Chernev and Karen Grigorian?',
        'question_text_preprocessed': ['What', 'occupation', 'Irving', 'Chernev', 'Karen', 'Grigorian'],
        'named_entities': {'http://dbpedia.org/resource/Irving_Chernev': 'Irving Chernev', 'http://dbpedia.org/resource/Karen_Grigorian': 'Karen Grigorian'},
        'named_entities_preprocessed': {'http://dbpedia.org/resource/Irving_Chernev': 'Irving Chernev', 'http://dbpedia.org/resource/Karen_Grigorian': 'Karen Grigorian'}
    }
]
```

Randomly pick 5 questions and do the following:
* analyze manually the difference between `named_entities` and `named_entities_preprocessed`;
* manually perform the Named Entity Linking task on the questions and compare your annotation with the DBpedia Spotlight one

Briefly write your thoughts about it in the README file attached to your solution.

While working with DBpedia Spotlight always use fixed `confidence = 0.5`.

## DBpedia Spotlight example with Python

As the public API of the DBpedia Spotlight is not stable, we deployed it locally on the University's server. Here is the example of API usage with Python 3:

```
import requests

response = requests.get(url="http://webengineering.ins.hs-anhalt.de:43720/rest/annotate",
                            params={"text": "Where was Angela Merkel born?", "confidence": 0.5},
                            headers={'accept': 'application/json'},
                            verify=False)
```

## Guidance / Tutorials

* Getting started with Text Preprocessing: https://www.kaggle.com/sudalairajkumar/getting-started-with-text-preprocessing
* What is Named Entity Linking: https://en.wikipedia.org/wiki/Entity_linking
* An introduction to HTTP: https://www.freecodecamp.org/news/http-and-everything-you-need-to-know-about-it/, https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/http_basics.html
