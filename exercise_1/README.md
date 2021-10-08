# Exercise 1: Recognizing and Linking Named Entities in the Textual Questions

## Context

Analyzing and processing Natural Language is one of the basic and first things in the Question Answering (QA) systems.

One of the important steps is to recognize so-called [Named Entities](https://en.wikipedia.org/wiki/Named_entity) ([Named Entity Recognition, NER](https://en.wikipedia.org/wiki/Named-entity_recognition)) and/or link them to a resource on the web or in a knowledge graph ([Named Entity Linking (NEL)](https://en.wikipedia.org/wiki/Entity_linking)).

For example, in the following question: "Where was Angela Merkel born?", we can recognize (NER) and link (NEL) the named entity "Angela Merkel" to a corresponding resource in the [DBpedia Knowledge Graph](https://www.dbpedia.org/about/#:~:text=DBpedia%20is%20a%20crowd%2Dsourced,for%20everyone%20on%20the%20Web.) -- https://dbpedia.org/page/Angela_Merkel (i.e., to a URI that is an ID of the person "Angela Merkel").

The information about named entities is used by a QA system in the future steps of answering a question (e.g., in the query builder component).

## Learning Objectives

* Learn how to preprocess Natural Language texts manually and automatically.
* Learn how to use Named Entity Recognition tools (spaCy).
* Learn how to use Named Entity Linking tools (DBpedia Spotlight).

## Task

### Part 1 (manual)

Select any 10 questions from the dataset **according to your variant** and do the following:
* translate them from English to your mother tongue (e.g., German, Chinese, etc.); please do no use machine translation (if possible).
* extract named entities manually from these questions (and translations) and determine their types (e.g., Person, Politician, Entertainer, Location, City, Company, etc.); please be as precise as possible
* put everything together in the structured JSON format as shown below.

```
[
    {
        'id': '4831',
        'question_text': 'In what wars was Steve Buyer involved?',
        'question_text_LANG_CODE': 'An welchen Kriegen war Steve Buyer beteiligt?',
        'named_entities': {'Steve Buyer': ['Person']},
        'named_entities_LANG_CODE': {'Steve Buyer': 'Person'}
    },
    {
        'id': '4635',
        'question_text': 'What is the occupation of the Irving Chernev and Karen Grigorian?',
        'question_text_LANG_CODE': 'What is the occupation of the Irving Chernev and Karen Grigorian?',
        'named_entities': {'Irving Chernev': ['Person'], 'Karen Grigorian': ['Person']},
        'named_entities_LANG_CODE': {'Irving Chernev': 'Person', 'Karen Grigorian': 'Person'}
    }
]
```

**NOTE**: replace `LANG_CODE` with the code of your native language. In this example it will be: `de` (German). Please, follow [this link](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for the list of language codes.

Analyze your work, do you see anything unusual/suspicious/strange? Briefly write your thoughts about it in the README file attached to your solution.

### Part 2 (programming)

Depending on your **exercise variant** write a script, which takes for input a list of questions and outputs for each question:
* preprocessed question (tokenization, stopwords and special characters removing, lemmatization);
* a dictionary `{'text': 'type'}` of recognized named entities from the question (use [spaCy](https://spacy.io/usage/linguistic-features#named-entities)).
* a dictionary `{'uri': 'text'}` of linked named entities from the question (use [DBpedia Spotlight](https://www.dbpedia-spotlight.org/)). 

The format of the script output is a JSON file with the following structure:

```
[
    {
        'id': '4831',
        'question_text': 'In what wars was Steve Buyer involved?',
        'question_text_preprocessed': ['In', 'war', 'Steve', 'Buyer', 'involved'],
        'named_entities_recognized': {'Steve Buyer': 'PERSON'},
        'named_entities_linked': {'http://dbpedia.org/resource/Steve_Buyer': 'Steve Buyer'}
    },
    {
        'id': '4635',
        'question_text': 'What is the occupation of the Irving Chernev and Karen Grigorian?',
        'question_text_preprocessed': ['What', 'occupation', 'Irving', 'Chernev', 'Karen', 'Grigorian'],
        'named_entities_recognized': {'Irving Chernev': 'PERSON', 'Karen Grigorian': 'PERSON'},
        'named_entities_linked': {'http://dbpedia.org/resource/Irving_Chernev': 'Irving Chernev', 'http://dbpedia.org/resource/Karen_Grigorian': 'Karen Grigorian'}
    }
]
```

The output JSON file has to contain all the questions from your variant.

Manually check your results for possible mistakes of the software. Briefly write your findings in the README file attached to your solution.

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
* What is Named Entity Recognition: https://en.wikipedia.org/wiki/Named-entity_recognition
* What is Named Entity Linking: https://en.wikipedia.org/wiki/Entity_linking
* spaCy documentation for NER: https://spacy.io/usage/linguistic-features#named-entities
* An introduction to HTTP (for sending requests to DBpedia Spotlight): https://www.freecodecamp.org/news/http-and-everything-you-need-to-know-about-it/, https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/http_basics.html
