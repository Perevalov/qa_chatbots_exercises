## Context

We want our system to work in any environment: local PC, server of the University, server of the Project Sponsor etc. However, every environment has its own setup: hardware, OS, libraries and dependencies. The solution is to put each microservice into a separate container that is completely isolated from dependencies and libraries of the OS. 

## Learning Objectives

* Learn how to create a Docker image;
* Learn how to run multiple Docker containers.

## Task

Work in teams:

1. Obtain an access to a server of the University;
2. Set up a repository for your solution and clone files on the server. You can use any VCS that you want;
3. Create `Dockerfile(s)` for your components as well as for the Frontend and the Backend;
4. Define `docker-compose.yml` file to run multiple containers;
5. Start your containers using `docker-compose`.

Before you start -- check the [example](https://github.com/Perevalov/qa_chatbots_exercises/tree/main/Exercise_7/qanary_example).

Be prepared to answer the following control questions:

* What is Gunicorn and what is its difference vs. Flask? (answer if you use Python);
* Can we reuse a Docker image in order to run several Docker containers?
* What is the difference between the Docker image and the Docker container?
* Can we run Docker containers without Docker Compose?
* What is the difference between Docker containers and Virtual Machines?
* What is the difference between Git, GitHub, and GitLab?

## Submission check

In this Exercise, **submission check will be performed in two steps**:
1. You send the code with your solution and the README with a description of files to Moodle (as usual). Then I check it, if everything is OK, we move to the second step.
2. On the Exercise, you share your screen and show how it works.

After completion of these two steps, you pass the first part.

## Guidance / Tutorials

* Connection and work with the University's servers: https://moodle.hs-anhalt.de/mod/wiki/view.php?id=46441
* How to work with Git: https://moodle.hs-anhalt.de/mod/wiki/view.php?id=64219
* How to work with University's GitLab: https://moodle.hs-anhalt.de/mod/wiki/view.php?id=48095
* Docker overview: https://docs.docker.com/engine/
* Docker Compose overview: https://docs.docker.com/compose/
* A comprehensive tutorial about Docker: https://github.com/vadikl/Projects-and-Materials/blob/main/Computer%20Science/Docker/Docker.ipynb
