## THIS IS AN EXAMPLE FOR EXERCISE 3

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
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT DISTINCT ?dev ?devLabel
WHERE {
    wd:Q40984 wdt:P178 ?dev . # Skype - developer - ?
  
  	# Uncomment to get English labels
  	# ?dev rdfs:label ?devLabel .
  	# FILTER(LANG(?devLabel) = "en").
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
LIMIT 1
```

**SPARQL 2 Wikidata**

```
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT DISTINCT ?city ?cityLabel
WHERE {
    ?city wdt:P17 wd:Q837 . # object based in Nepal
    ?city wdt:P31 wd:Q515 . # type City
  	
  	# Uncomment to get English labels
  	# ?city rdfs:label ?cityLabel .
  	# FILTER(LANG(?cityLabel) = "en") .
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
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>

SELECT DISTINCT ?timeZone ?timeZoneLabel
WHERE {
    wd:Q11746 wdt:P421 ?timeZone . # looking for a time zone
  
  	# Uncomment to get English labels
  	# ?timeZone rdfs:label ?timeZoneLabel .
  	# FILTER(LANG(?timeZoneLabel) = "en").
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
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>

ASK
WHERE {
    wd:Q76 wdt:P19 wd:Q782 .
}
```
