# Exercise 7: Information-Retrieval based Question Answering

## Context

There are two major paradigms of Question Answering systems:
* Information-Retrieval based (IR-based);
* Knowledge Base Question Answering (KBQA).

### IR-based QA

IR-based QA systems work with unstructured data (e.g., web pages, text documents). These systems execute two steps in order to retrieve the answer:
1. Retrieve the most relevant document (sometimes called as "passage") among the others (alternative name: retriever step);
2. Find the answer in the document from the previous step while extracting a textual span from it (alternative name: reader step/reading comprehension).

This 2-step process is also called retriever-reader.

### Knowledge Base Question Answering (KBQA)

The KBQA systems work over structured data (e.g., relatinal DBs, knowledge graphs). The goal of such system is to map a textual question to semantic representation of a query to a Knowledge Base (KB). For example, the question “In what city was Angela Merkel born?” can be mapped to:
* `λ.x.birthPlace(Angela_Merkel) ∧ isCity(x)`
* `SELECT ?city WHERE { dbr:Angela_Merkel dbo:birthPlace ?city . ?city rdf:type dbo:City }`

In this regard, Knowledge Graph QA systems (KGQA) are the subset of KBQA: KGQA ⊂ KBQA.

### What paradigm is better?

As always, the truth is somewhere in between. That is why in this exercise we will combine both paradigms.

## Learning Objectives

* Learn how the IR-based QA systems work;
* Learn how to combine KGQA and IR-based QA.

## Task

### General formulation

The task is to answer questions from [Exercise 4](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_4) using both structured and unstructured data. To do so, you have to implement a QA process with Qanary framework that does the following steps:
1. Determines a named entity that is mentione in a question ([Named Entity Linking](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_1))
2. Retrieves an abstract (short textual description) of the named entity (used `dbo:abstract` property) -- retriever step;
3. Finds a textual span in the retrieved abstract and returns this as an answer (use [RoBERTa-For-QA](https://webengineering.ins.hs-anhalt.de:43740/#/applications/RoBERTa-For-QA) Qanary component) -- reader step.

### ToDo steps

Using the [data (subject and predicate) from Exercise 4](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_4) according to your variant and DBpedia SPARQL endpoint, retrieve the truth answer labels for each of the questions (use `rdfs:label` property). If you completed the [previous exercise](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_6), you already should have all the code prepared.

Run the questions from the test dataset on your system and collect all the graph IDs returned from [Qanary pipeline](https://webengineering.ins.hs-anhalt.de:43740/startquestionansweringwithtextquestion). For example, you can have the following components in the pipeline: (1) `NEL`, (2) `Retriever` (Fetches an abstract from DBpedia), (3) `RoBERTa-For-QA` (Reader) -- see the steps in General formulation. Thus, the last component (reader) will try to extract the desired answer from the abstract text that was retrieved in the second component.

Prepare a .csv table with the following columns: `graph_id`, `question_text`, `correct_answer_text`, `answer_text`, `is_true`. The `is_true` column has a binary value (either True or False) -- the same as `precision` column in the [previous exercise](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_6). You can obtain `is_true` value by directly comparing `correct_answer_text` and `answer_text` or you can use fuzzy string comparison (e.g., [Levenstein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)) with a certain threshold.

Report on the results in the .csv file while answering the following quesitons:
* What is the average of `is_true`? 
* Did you use fuzzy or direct string comparison? 
* What are the error causes in your QA pipeline?

### Help

The [RoBERTa-For-QA](https://webengineering.ins.hs-anhalt.de:43740/#/applications/RoBERTa-For-QA) Qanary component uses the following query to insert the result (you are looking for the `json_answer`):
```sparql
PREFIX qa: <http://www.wdaqua.eu/qa#>
PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
INSERT {
GRAPH <{uuid}> {
    ?b a qa:AnnotationOfAnswerJson ;
        oa:hasTarget <{question_uri}> ;
        oa:hasBody ?answer ;
        oa:annotatedBy <urn:qanary:{component}> ;
        oa:annotatedAt ?time .
    ?answer a qa:AnswerJson ;
            rdf:value "{json_answer}"^^xsd:string .
    qa:AnswerJson rdfs:subClassOf qa:Answer .
    }
}
WHERE {
    BIND (IRI(str(RAND())) AS ?b) .
    BIND (IRI(str(RAND())) AS ?answer) .
    BIND (now() as ?time) .
}
```

## Guidance / Tutorials

* A holistic material on the Question Answering field: https://web.stanford.edu/~jurafsky/slp3/23.pdf
* Python library for fuzzy string comparison: https://pypi.org/project/fuzzywuzzy/
