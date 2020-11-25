## Context

Software testing on a par with the software development is an integral part of the process of delivering the system to its users. The testing phase is intended to find and localize the errors in the newly developed system. There are several statements about errors in the code that can help to undertand the importance of testing better:

* The error always exists;
* The error is always not where you are looking for it;
* Debugging is the process of fixing errors, while coding is the process of creating errors;
* It can be hard to write a test, but it should be easy to run a test.


## Learning Objectives

* Learn how to create tests for Question Answering system.

## Task

Based on the data provided for each variant create the following tests:

1. Implement end-to-end Question Answering quality test using [Precision@k](https://stackoverflow.com/questions/55748792/understanding-precisionk-apk-mapk) metric (compare True answers with the ones that your system outputs);
2. Components testing: write tests for at least 2 components that are checking the correcntess of its work (e.g. check if the required annotation was created);
3. Models evaluation: create a test for your machine learning models (e.g. relation classifier) such that it achieves the expected value of a target metric ([Precision](https://en.wikipedia.org/wiki/Precision_and_recall), [Recall](https://en.wikipedia.org/wiki/Precision_and_recall), [F1 Score](https://en.wikipedia.org/wiki/F-score)).

Additionally, create at least 2 unit tests for your "common" functionality e.g. preprocessing functions.

Put all tests in the `tests` directory of your project.

Please, be prepared to answer following control questions:

* What is the Regression testing and why it is important in the system delivering process?
* What are the specifics of testing projects that are using Machine/Deep Learning?
* What is the difference between functional and non-functional testing?

**NOTE:** You have to complete both parts of the Exercise 5 in order to make and pass this Exercise.

## Guidance / Tutorials

* Example for tests in Python: https://github.com/Perevalov/qa_chatbots_exercises/tree/main/Exercise_6/qanary_example/tests
* Types of functional testing: https://www.simform.com/functional-testing-types/
* Functional Vs. Non-Functional Testing: https://www.guru99.com/functional-testing-vs-non-functional-testing.html
* Test frameworks for Python: https://docs.pytest.org/en/stable/, https://docs.python.org/3/library/unittest.html
* Test frameworks for Java: 