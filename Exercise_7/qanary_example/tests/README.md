## How to run tests

Start all components that will be tested.

In this directory run the following commands:

1. `pip install pytest`
2. `pytest .`

## Example of SPARQL Queries for checking the annotations

For example, component "Relation Prediction" creates the following annotation:

```sparql
PREFIX qa: <http://www.wdaqua.eu/qa#>
PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
INSERT {
GRAPH <GRAPHID> {
    ?a rdf:type qa:AnnotationOfInstance .
    ?a oa:relation <http://dbpedia.org/ontology/birthPlace> .
    ?a oa:annotatedBy <urn:qanary:myQaSystem> .
    ?a oa:annotatedAt ?time .
    }
}
WHERE {
    BIND (IRI(str(RAND())) AS ?a) .
    BIND (now() as ?time) 
}
```

Then, to check the correctness of the annotation we can run following query

```sparql
PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX qa: <http://www.wdaqua.eu/qa#>

ASK
FROM <GRAPHID>
WHERE {
    ?annotationId rdf:type qa:AnnotationOfInstance .
    ?annotationId oa:relation <http://dbpedia.org/ontology/birthPlace> .
}

```

See corresponding [example](https://github.com/Perevalov/qa_chatbots_exercises/blob/main/Exercise_6/qanary_example/tests/test_relation_prediction_component.py).