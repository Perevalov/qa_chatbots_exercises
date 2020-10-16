## THIS IS AN EXAMPLE VARIANT FOR EXERCISE 1

***

**Question 1:** "Who developed Skype?"

**SPARQL 1 DBpedia:**

```
PREFIX dbo: <http://dbpedia.org/ontology/> 
PREFIX dbr: <http://dbpedia.org/resource/> 

SELECT DISTINCT ?dev # we can name ?dev whatever we want -- this is variable
WHERE { 
    dbr:Skype dbo:developer ?dev . # Skype - developer - ?
}
```

**SPARQL 1 Wikidata**

```
SELECT DISTINCT ?dev
WHERE {
    wd:Q40984 wdt:P178 ?dev . # Skype - developer - ?
}
```

***

**Question 2:** "Name a city in Nepal."

**SPARQL 2 DBpedia:**

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/> 

SELECT DISTINCT ?city 
WHERE { 
    ?city dbo:country dbr:Nepal . # object located in Nepal
  	?city rdf:type dbo:City . # type City
}
```

**SPARQL 2 Wikidata**

```
SELECT DISTINCT ?city
WHERE {
    ?city wdt:P17 wd:Q837 . # object based in Nepal
    ?city wdt:P31 wd:Q515 . # type City
}
```

***

**Question 3:** "What is the timezone in Wuhan (China)?"

**SPARQL 3 DBpedia:**

```
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/> 

SELECT DISTINCT ?timeZone 
WHERE { 
  	VALUES ?predicate { dbo:timeZone dbp:timezone } . # in DBpedia 2 predicates are representing time zone property
    dbr:Wuhan ?predicate ?timeZone . # looking for a timezone
}
```

**SPARQL 3 Wikidata**

```
SELECT DISTINCT ?timeZone
WHERE {
    wd:Q11746 wdt:P421 ?timeZone . # looking for a time zone
}
```

***

**Question 4:** "Was Barack Obama born in Hawaii?"

**SPARQL 4 DBpedia:**

```
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/> 

ASK
WHERE { 
  	VALUES ?p { dbp:birthPlace dbo:birthPlace } . # in DBpedia 2 predicates are representing birth place property
    dbr:Barack_Obama ?predicate dbr:Hawaii .
}
```

**SPARQL 4 Wikidata**

```
ASK
WHERE {
    wd:Q76 wdt:P19 wd:Q782 .
}
```