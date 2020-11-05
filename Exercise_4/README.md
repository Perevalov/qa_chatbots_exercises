## Context

As Question Answering system is a software product -- we need share it with the user. Mostly, it is done in the form of a Web Application. A canonical Web Application has the "Client-Server" or "Frontend-Backend" architecture. Where Client presents a graphical interface to a user and sends all the user's data to a Server, which does all computations and sends back a result.

In case of a Question Answering system, Client has to provide user a Form where he/she can put a question and see an answer. When the question is provided, Client sends it to the Server which computes an answer and sends it back to the Client.

## Learning Objectives

* Learn how to create a Web Interface for Question Answering system.
* Learn how to implement Client-Server application template.

## Task

**NOTE:** this exercise doesn't have variants. However, it provides many options for the implementation.

### 1. Front-end (Client)

Implement a client for a Question Answering system or a Chatbot. The Client has to have input form for a question and a text area for an answer. It can be implemented in a Chat-like form or in a Search engine-like form.

If you are not familiar with Front-end stack you can use any Messenger's API (Telegram, Slack, Discord, VK, Facebook Messenger etc.). In this case, you can just reuse existing components of a particular messenger to your needs. Just Google **[Telegram, Slack, Discord, ...] API**.

### 2. Back-end (Server)

Implement a server for your Question Answering system. The server has to support 2 HTTP methods:

1. Type: `GET`, Name: `health`, Returns: `{'status': 'OK'}`;
2. Type: `POST`, Name: `get_answer`, Params: `question_text`, Returns: `{'answer_text': 'This is your question <question_text>'}`.

**OPTIONAL:** reuse Named Entity Linking and Relation Prediction components in your Back-end. Then, the 2nd method has to return following: 
```
{
    'answer_text': 'This is your question <question_text>',
    'named_entities': [{'URI1': 'SurfaceForm1'}, {'URI2': 'SurfaceForm2'}],
    'relation': '<relation_uri>'
}
```

### 3. Connect Front-end and Back-end

Connect Front-end and Back-end together, such that user can send questions and recieve answers. Keep in mind that you have to parse JSON response from your Back-end and present it in a "beautiful" way in Front-end.

## Submission check

In this Exercise, **submission check will be performed in two steps**:
1. You send the code with your solution and README with description of files to Moodle (as usually). Then I check it, if everything is OK, we move to the second step.
2. On the Exercise you share your screen and show how it works.

After completion of these two steps you pass the exercise.

## Guidance / Tutorials

* Links to deployed projects from previous year: https://moodle.hs-anhalt.de/mod/folder/view.php?id=82995
* Front-end of the project from previous year: https://github.com/Perevalov/nuance-web
* Simple QA system (with Front-end): https://github.com/Perevalov/kb-qa
* Back-end of the project from previous year: https://github.com/Perevalov/nuance-core
* Creating REST Service with Java Spring: https://spring.io/guides/gs/rest-service/
* Creating REST Service with Python Flask: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
* Additional help: https://moodle.hs-anhalt.de/course/view.php?id=1384
