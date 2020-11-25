# This script creates test datasets
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import json
from tqdm import tqdm

def query(subject, predicate):
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?object
    WHERE
    {{
      <{s}> <{p}> ?object .
    }}
    """.format(s=subject, p=predicate))

  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()
  result = results["results"]["bindings"]
  if len(result) > 0:
    response_list = list()
    for res in result:
      response_list.append(res['object']['value'])
    return response_list
  else:
    result = None

if __name__ == "__main__":
  test = pd.read_csv("../../Exercise_5/variant_3/test.csv", sep=";")

  json_result = list()

  for i, row in tqdm(test.iterrows()):
    try:
      result = query(row.subject.replace("\"",""), row.predicate.replace("\"",""))
      item = {
        'id': row.id,
        'question': row.question,
        'subject': row.subject,
        'predicate': row.predicate,
        'result': result
      }
      json_result.append(item)
    except Exception as e:
      print(e)

  with open("variant_3.json", "w") as f:
    json.dump(json_result, f, indent=4, ensure_ascii=False)

