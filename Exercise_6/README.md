<h2>Context</h2>
<p>Software testing on a par with software development is an integral part of the process of delivering the system to its users. The testing phase is intended to find and localize the errors in the newly developed system. There are several statements about
    errors in the code that can help to understand the importance of testing better:</p>
<ul>
    <li>The error always exists;</li>
    <li>The error is always not where you are looking for it;</li>
    <li>Debugging is the process of fixing errors, while coding is the process of creating errors;</li>
    <li>It can be hard to write a test, but it should be easy to run a test.</li>
</ul>
<h2>Learning Objectives</h2>
<ul>
    <li>Learn how to assure the quality of a Question Answering system.</li>
</ul>
<h2>Task</h2>
<p>Based on the data provided for each variant create the following tests:</p>
<ol>
    <li>Implement end-to-end Question Answering quality test using <a href="https://stackoverflow.com/questions/55748792/understanding-precisionk-apk-mapk" rel="nofollow">Precision@k</a> metric;
        <ul>
            <li>i.e., compare the expected answers (hence, correct answers) with the ones that were computed by your system)</li>
        </ul>
    </li>
    <li><a href="https://github.com/Perevalov/qa_chatbots_exercises/blob/main/Exercise_6/qanary_example/tests/test_relation_prediction_component.py">Components testing</a>: implement tests for all components contained in your QA system. The tests should check
        the correctness of components' work (e.g. it has to be checked if the required annotations were created)
        <ul>
            <li>i.e., you need to implement for each component in your Question Answering system at least one SPARQL query (c.f., the presentation in the lecture)</li>
            <li>note: it is assumed that you define at <em>least 10 test cases</em> for your system (i.e., also for your components)</li>
        </ul>
    </li>
    <li><a href="https://github.com/Perevalov/qa_chatbots_exercises/blob/main/Exercise_6/qanary_example/tests/test_relation_prediction_model.py">Models evaluation</a>: create a test for your machine learning models (e.g., relation classifier) such that it
        achieves the expected value of a target metric (<a href="https://en.wikipedia.org/wiki/Precision_and_recall" rel="nofollow">Precision</a>, <a href="https://en.wikipedia.org/wiki/Precision_and_recall" rel="nofollow">Recall</a>, <a href="https://en.wikipedia.org/wiki/F-score"
            rel="nofollow">F1 Score</a>).</li>
</ol>
<p>Put all tests in the <code>tests</code> directory of your project.</p>
<p>Please, be prepared to answer the following control questions:</p>
<ul>
    <li>What is Regression testing and why it is important in the system delivering process?</li>
    <li>What is end-to-end testing and&nbsp;micro-benchmarking? How do we combine these two approaches?</li>
    <li>What are the specifics of testing projects that are using Machine/Deep Learning?</li>
    <li>What is the difference between functional and non-functional testing?</li>
</ul>
<p><strong>NOTE:</strong> You have to complete both parts of Exercise 5 in order to make and pass this exercise.</p>
<h2>Guidance / Tutorials</h2>
<ul>
    <li>Example of tests in Python (see README and the content of the tests): <a href="https://github.com/Perevalov/qa_chatbots_exercises/tree/main/Exercise_6/qanary_example/tests">https://github.com/Perevalov/qa_chatbots_exercises/tree/main/Exercise_6/qanary_example/tests</a></li>
    <li>Types of functional testing: <a href="https://www.simform.com/functional-testing-types/" rel="nofollow">https://www.simform.com/functional-testing-types/</a></li>
    <li>Functional Vs. Non-Functional Testing: <a href="https://www.guru99.com/functional-testing-vs-non-functional-testing.html" rel="nofollow">https://www.guru99.com/functional-testing-vs-non-functional-testing.html</a></li>
    <li>Test frameworks for Python: <a href="https://docs.pytest.org/en/stable/" rel="nofollow">https://docs.pytest.org/en/stable/</a>, <a href="https://docs.python.org/3/library/unittest.html" rel="nofollow">https://docs.python.org/3/library/unittest.html</a></li>
    <li>Test frameworks for Java:&nbsp;<a href="https://junit.org/junit5/">https://junit.org/junit5/</a>&nbsp; &nbsp;</li>
</ul>
