## Context

As Question Answering system is a software product -- we need to share it with the user. Mostly, it is done in the form of a Web application. A canonical Web application follows the "Client-Server" or "Frontend-Backend" architecture. Where the client presents a graphical user interface (GUI) to a user and sends all the user's data to a server, which does all computations and sends back a result.

In the case of a Question Answering system, the client has to provide the user with a form where he/she can insert a question and see an answer. When the question is provided, the client sends it to the server which computes an answer and sends it back to the client (i.e., shows it to the user).

## Learning Objectives

* Learn how to create a Web Interface for Question Answering system.
* Learn how to implement the Client-Server application template.

## Task

### 1. Frontend (Client)

Implement a client for a Question Answering system or a Chatbot. The client has to have an input form for a question and a text area for an answer. It can be implemented in a form that might be similar to a chat or a search engine.

If you are not familiar with Frontend stack you can use any Messenger's API (Telegram, Slack, Discord, VK, Facebook Messenger, etc.). In this case, you can just reuse existing components of a particular messenger to your needs. Just Google **[Telegram, Slack, Discord, ...] API**.

### 2. Backend (Server)

Implement a server for your Question Answering system. The server has to support 2 HTTP methods:

1. Type: `GET`, Name: `health`, Returns: `{'status': 'OK'}`;
2. Type: `POST`, Name: `question`, Params: `question_text`, Returns: see next paragraph.

Reuse Named Entity Linking and Relation Prediction components in your Backend. Then, the 2nd method has to return following: 
```
{
    'answer_text': 'This is your question <question_text>',
    'named_entities': [{'URI1': 'SurfaceForm1'}, {'URI2': 'SurfaceForm2'}],
    'relation': '<relation_uri>'
}
```

The GET endpoint should be used to check if your service is accessible, i.e., a frontend will first check if the backend service is available).

Process the questions via the `question` method according to your variant and save it to the `output.json` file.

### 3. Connect Frontend and Backend

Connect frontend and backend together, such that a user can send questions and receive answers. Keep in mind that you have to parse the JSON response from your backend and present it in a "beautiful" way in the frontend.

## Submission check

In this Exercise, **submission check will be performed in two steps**:
1. You send the code with your solution, `output.json` file, and the README with a description of files to Moodle (as usual). Then I check it, if everything is OK, we move to the second step.
2. On the Exercise, you share your screen and show how it works.

After completion of these two steps, you pass the exercise.

## Guidance / Tutorials

* Links to deployed projects from previous year: https://moodle.hs-anhalt.de/mod/folder/view.php?id=82995
* The Frontend of the project from the previous year: https://github.com/Perevalov/nuance-web
* Simple QA system (with Frontend): https://github.com/Perevalov/kb-qa
* The Backend of the project from the previous year: https://github.com/Perevalov/nuance-core
* Creating REST Service with Java Spring: https://spring.io/guides/gs/rest-service/
* Creating REST Service with Python Flask: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
* Additional help: https://moodle.hs-anhalt.de/course/view.php?id=1384
