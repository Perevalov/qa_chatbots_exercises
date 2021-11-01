# Exercise 4: Simple KGQA System

## Context

From previous exercises, you have learned how to: [write SPARQL queries](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_3), [work with natural language](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_1), [extract and link named entities (NER & NEL)](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_1), [predict relations](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_2), and [create a Client-Server (Web Service) application](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_2). However, to create a KGQA system, you have only combine these components. 
In the figure below, you can see the architecture of QA process from the server (backend) side where just text is given by user via an Webservice API and the resonse (answer) is also text.

![simple-kgqa](https://user-images.githubusercontent.com/16652575/139591569-eea04bd4-4a24-4a19-8877-223173a4d318.jpg)

Please note, that in this exercise we implement the QA system only for so-called Forward queries (`subject-predicate-?`), however, if you want to do it also for Backward queries (`?-predicate-object`) you have to additionally implement a query type classifier (it is optional).

## Learning Objectives

* Learn how to combine previously implemented components in order to create a simple KGQA system.
* Improve your understanding of a component-oriented approach to solve question answering tasks.
* Start thinking about quality assurance in question answering.

## Task

0. Re-train relation prediction model based on the new data (see [repository](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_4));
1. Combine all the components together as it's shown in the Figure above (Note: each component has to be wrapped into a Web service);
2. Implement a Web service that is calling your components (API Gateway) -- it will receive requests and send responses to a user (check what is [microservice architecture](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices)).
3. All the services should be runned in the individual Docker containers.
4. This is considered to be the first step toward quality assurance of your system: Provide at least 5 questions that work correctly and 5 questions that are not supported correctly by your implementation, because of a flawed classification result (i.e., classifier has identified the false resource) or another quality issues (not solvable because of a bug you put into the source code is not accepted). All questions of each group should have different subjects and predicates. For the question of the second group provide also the exact reason why the question could not be processed correctly. 

Please, try to start structuring your code into different functions and modules. Additionally, store queries, templates, and config parameters in separate files ([hardcoding](https://softwareengineering.stackexchange.com/questions/368448/how-can-hard-coding-be-considered-a-code-smell-in-the-age-of-micro-services) is an antipattern).

Note, that after performing NEL and Relation Prediction, your system will get the named entity and relation from these components respectively.
Then, using the obtained information, you need to fill the query template:

```sparql
SELECT ?object 
WHERE {
        <subject> <predicate/relation> ?object .
}
```

Hence, if NEL returns `dbr:Michael_Jordan` and Relation Prediction returns `dbo:birthPlace`, then your query executor will work with the following query of the DBpedia knowledge graph:

```sparql
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT ?object 
WHERE {
        dbr:Michael_Jordan dbo:birthPlace ?object .
}
```

Prefixes in the queries are omitted.

Get inspired by the Docker example:.

## Submission check

In this exercise, **submission check will be performed in two steps**:

1. You send the code with your solution and the README with a description of files and the quality assurance examples to Moodle (as usual). Then, I check it. If everything is OK, we move to the second step.
2. On the exercise, you perform a system demonstration (e.g., via Swagger UI provided via FastAPI).

After completion of these two steps, you pass the exercise.

## Guidance / Tutorials

* Microservice Architecture: https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices
* Creating REST Service with Java Spring: https://spring.io/guides/gs/rest-service/
* Python FastAPI docs: https://fastapi.tiangolo.com/
* Install Docker: https://docs.docker.com/engine/install/
* Install Docker Compose: https://docs.docker.com/compose/install/
* Additional help: https://moodle.hs-anhalt.de/course/view.php?id=1384
