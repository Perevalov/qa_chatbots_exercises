# Part Simple KGQA System

## Context

From previous exercises, you have learned how to: write SPARQL queries, [work with natural language](), [extract and link named entities (NEL)](), [predict relations](), and [create a Client-Server (Web Service) application](). However, to create a KGQA system you have only combine these components. In the Figure below you can see the architecture of QA process from Server (backend) side:


Please note, that in this exercise we implement the QA system only for so-called Forward queries (`subject-predicate-?`), however, if you want to do it also for Backward queries (`?-predicate-object`) you have to additionally implement a query type classifier (it is optional).

## Learning Objectives

* Learn how to combine previously implemented components in order to create a simple KGQA system.

## Task

0. Re-train relation prediction model based on the new data (see [repository]());
1. Combine all the components together as it's shown in the Figure above (Note: each component has to be wrapped into a web-service);
2. Implement a Web Service that is orchestrating your components -- it will recieve requests and send responses to a user (check what is [microservice architecture](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices)).

Please, try to start structuring your code into different functions and modules. Additionally, store queries, templates, and config parameters in separate files ([hardcoding](https://softwareengineering.stackexchange.com/questions/368448/how-can-hard-coding-be-considered-a-code-smell-in-the-age-of-micro-services) is an antipattern).

Note, that after performing NEL and Relation Prediction your system will get the named entity and relation from these components respectively.
Then, using the obtained information you need to fill the query template:

```sparql
SELECT ?object 
WHERE {
        <subject> <predicate/relation> ?object .
}
```

Hence, if NEL returns: dbr:Michael_Jordan and Relation Prediction: dbo:birthPlace, then your query executor will work with the following query:

```sparql
SELECT ?object 
WHERE {
        dbr:Michael_Jordan dbo:birthPlace ?object .
}
```

Prefixes in the queries are ommitted.

## Submission check

In this Exercise, **submission check will be performed in two steps**:
1. You send the code with your solution and the README with a description of files to Moodle (as usual). Then I check it, if everything is OK, we move to the second step.
2. On the Exercise, you perform a system demonstration (e.g. via Swagger UI provided via FastAPI).

After completion of these two steps, you pass the exercise.

## Guidance / Tutorials

* Microservice Architecture: https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices
* Creating REST Service with Java Spring: https://spring.io/guides/gs/rest-service/
* Python FastAPI docs: https://fastapi.tiangolo.com/
* Additional help: https://moodle.hs-anhalt.de/course/view.php?id=1384
