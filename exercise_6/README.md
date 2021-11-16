# Exercise 6: Quality Measurement

## Context

Search engines and question answering systems share the same methods of measuring the quality of their work. In general, there are two levels of measuring quality of such systems: 
* component-level;
* system-level. 

On the component level the quality of a particular task is measured, for instance, for Named Entity Linking or Relation Prediction -- classical Confusion Matrix, Precision, Recall, and F1 Score can be used.
For the system-level quality measurments, the metrics are divided into two classes:
* non-ranked output metrics;
* ranked output metrics.

In the non-ranked output setting we do not care about the position of the truth answers i.e., the position is not taken into account. Again, in this case the Confusion Matrix, Precision, Recall, and F1 Score may be used, however, the way of calculation is different from the component-oriented setting.
In the ranked output setting, the metrics also take into account the positions of true answers in the list (typically, the higher -- the better) e.g., Precision@k, Mean Reciprocal Rank.

Finally, on both component- and system-levels we can measure system performance with respect to the execution time.

## Learning Objectives

* Learn the metrics for QA quality;
* Learn how to use RDF annotations to trace the QA process generate quality reports.

## Task

### Required Part

* Using the [data (subject and predicate) from Exercise 4](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/exercise_4) according to your variant and DBpedia SPARQL endpoint, retrieve the truth answers for each of the questions.
* Run the questions from the test dataset on your system and collect all the graph ids returned from [Qanary pipeline](https://webengineering.ins.hs-anhalt.de:43740/startquestionansweringwithtextquestion).
* Using the graph ids from the previous step to build a SPARQL SELECT query (or several queries) to gather all the information that is required to measure the follwing metrics:
  * For each component: Execution time, Confusion Matrix, Precision, Recall, and F1 Score;
  * For the system: Confusion Matrix, Precision, Recall, F1 Score, Precision@k (where k=1,5,10), Mean Reciprocal Rank;
* Create a .csv file that incorporates the aformentioned metrics with the following structure: `graph_id, nel_execution_time, nel_precision, nel_recall, nel_f1,  ..., query_builder_f1, system_precision, ..., system_precision_at_1, ..., system_mean_reciprocal_rank`;
* Create tables with confusion matrices for all the components and the system.

To call the [Qanary pipeline](https://webengineering.ins.hs-anhalt.de:43740/startquestionansweringwithtextquestion) with Python code, use the follwing example:

```python
response = requests.post(url="https://webengineering.ins.hs-anhalt.de:43740/startquestionansweringwithtextquestion",
                        params={
                            "question": "Question Text",
                            "componentlist[]": ["component1", "component2"]
                        }).json()

graph_id = response['inGraph']
```

Please, refer to [this document](https://nlp.stanford.edu/IR-book/pdf/08eval.pdf) for the guidance on how to calculate Information Retrieval metrics.

### Optional Part (for creativity)

* Create visualizations based on your .csv report;
* Create a set of questions to a user of your system s.t. it is possible to evaluate his/her experience.

## Guidance / Tutorials

* A good article on component-level metrics: https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9
* Evaluation in Information Retrieval: https://nlp.stanford.edu/IR-book/pdf/08eval.pdf
