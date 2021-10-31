# Exercise 3: SPARQL Queries over DBpedia & Wikidata

## Context

In our course we mainly study Question Answering systems over Knowledge Graphs (KGs). In its turn, KGs are mainly stored using [Resource Description Framework (RDF)](https://www.w3.org/TR/rdf-syntax-grammar/). RDF is a specification for modeling data (mainly on the Web). The data in RDF is modelled in so-called triples, which is a structure that has `<Subject>`, `<Predicate> (or <Relation>)`, and `<Object>`. For example, `<Mona Lisa> <AuthoredBy> <Leonardo Da Vinci>`. RDF has many vocabularies that extend its applicability. One of the popular RDF use cases that we use everyday is schema.org vocabulary, that is used to markup HTML pages of Online Stores for better Search Engine Optimization (SEO).

To retrieve RDF data there is a special query language exists: [SPARQL](https://www.w3.org/TR/sparql11-overview/). A knowledge graph as a usual database has an interface to its content, in the context of RDF, such interface is called SPARQL Endpoint. In this exercise, you will have to learn its basic syntax for ASK and SELECT queries. In addition, you will write queries over two different knowledge graphs: [DBpedia](https://www.dbpedia.org/) and [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page). This knowledge will help you in future to deal with knowledge graphs and extract required data from them efficiently.


## Learning Objectives

* Learn to write simple SPARQL queries (ASK and SELECT).
* Learn to write the queries over both DBpedia and Wikidata.

## Task

Depending on your exercise variant manually write SPARQL queries for the corresponding questions. To get inspired, see the example variant. Plese, start with queries over DBpedia, then continue with Wikidata.

Describe you findings during writing the queries. What's common and different in DBpedia and Wikidata?

After you wrote and checked that your queries are executable, write a script that reads a query, executes it on a knowledge graph, fetches the answer, and writes it to a JSON file of the following structure:

```
[
  {
    "question_text": "Given question text",
    "sparql_dbpedia": "Query over DBpedia written by you",
    "sparql_wikidata": "Query over Wikidata written by you",
    "answer_dbpedia": "Response from DBpedia",
    "answer_wikidata": "Response from Wikidata"
  }
]
```

Get inspired with the queries from the [example variant](https://github.com/Perevalov/qa_chatbots_exercises/blob/7d4984a6e8a218a3f657c83a7235f06e8f12ca9d/exercise_3/variant_example/README.md).

Please, check that you don't have any errors.

NOTE: Despite, DBpedia and Wikidata are general domain knowledge graphs, not all the information that exists in one of them also present in the another.

### An example of how to query a SPARQL endpoint written in Python

```python
from SPARQLWrapper import SPARQLWrapper, JSON

# question: "Name a city in Nepal"

dbpedia_query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/> 

SELECT DISTINCT ?city 
WHERE { 
    ?city dbo:country dbr:Nepal . # object located in Nepal
    ?city rdf:type dbo:City . # type City
}
LIMIT 1
"""
dbpedia_endpoint = "https://dbpedia.org/sparql"

sparql = SPARQLWrapper(dbpedia_endpoint)
sparql.setQuery(dbpedia_query)
sparql.setReturnFormat(JSON)
response = sparql.query().convert() # answer from the SPARQL Endpoint of a KG
```

## Guidance / Tutorials

* A gentle and interactive introduction into the Semantic Web: https://github.com/SemWebNotebooks/Notebooks
* Wikidata introduction: https://www.wikidata.org/wiki/Wikidata:Introduction 
* DBpedia introduction: http://www.semantic-web-journal.net/system/files/swj499.pdf
* Short SPARQL tutorials: https://www.w3.org/2009/Talks/0615-qbe/, https://www.youtube.com/watch?v=FvGndkpa4K0
* A nice SPARQL query editor is available at https://yasgui.triply.cc/, use the following **endpoint configurations**:
  * DBpedia: https://dbpedia.org/sparql
  * Wikidata: https://query.wikidata.org/bigdata/namespace/wdq/sparql
