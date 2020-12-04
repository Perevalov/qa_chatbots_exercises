<h2>Context</h2>
<p>We want our system to work in any environment: local PC, server of the University, server of the Project Sponsor etc. However, every environment has its own setup: hardware, OS, libraries and dependencies. The solution is to put each microservice into
    a separate container that is completely isolated from dependencies and libraries of the OS.</p>
<h2>Learning Objectives</h2>
<ul>
    <li>Learn how to create a Docker image;</li>
    <li>Learn how to run multiple Docker containers.</li>
    <li>Prepare the final project together with your team</li>
</ul>
<h2>Task 1</h2>
<p>Work in teams:</p>
<ol>
    <li>Obtain access to a server of the university; there is a server prepared for each project team:
        <ul>
            <li>dockerXX: ...</li>
            <li>dockerXX: ...</li>
            <li>dockerXX: ...</li>
        </ul>
    </li>
    <li>Set up a repository for your solution and clone files on the server. You can use any VCS that you want (however, Git via the GitLab server of our university would be suggested);</li>
    <li>Create a&nbsp;<code>Dockerfile</code>&nbsp;for each of your Qanary components as well as for the Frontend and the Backend;</li>
    <li>Define a file&nbsp;<code>docker-compose.yml</code>&nbsp;to run multiple containers;</li>
    <li>Start your containers using <code>docker-compose up</code>.</li>
</ol>
<p>Before you start -- check this&nbsp;<a href="https://github.com/Perevalov/qa_chatbots_exercises/tree/main/Exercise_7/qanary_example">example</a>.</p>
<p>Be prepared to answer the following control questions:</p>
<ul>
    <li>What is Gunicorn and what is its difference vs. Flask? (answer if you use Python);</li>
    <li>Can we reuse a Docker image in order to run several Docker containers?</li>
    <li>What is the difference between the Docker image and the Docker container?</li>
    <li>Can we run Docker containers without the docker-compose commands?</li>
    <li>What is the difference between Docker containers and Virtual Machines?</li>
    <li>What is the difference between Git, GitHub, and GitLab?</li>
</ul>

<h2>Task 2</h2>
<p>You already had a kickoff meeting with the project sponsors. Now, you have to start working on the project. Typically, that is completely your responsibility (so we will not prepare nor validate each step in the project for you). However, in the task,
    we will provide you with some guidance, how to start the project.</p>
<p>It is suggested to follow the following procedure to create a sketch of a possible system on a sheet of (digital) paper:</p>
<ol>
    <li>Choose 5-7 examples (questions and conversations) that should be addressed in your project.</li>
    <li><span style="font-size: 1rem;">Highlight the important parts of each input and define what annotations need to be computed to build the required query that will answer the query.</span></li>
    <li><span style="font-size: 1rem;">Define for each example the possible queries that need to be built to answer the exemplary user input.</span></li>
</ol>
<p>Be as precise as possible. However, as lecturers, we know that not everything will be clear at the beginning.</p>
<p><span style="text-decoration: underline;">Remark:</span> After completing this task it is suggested to already start with implementing a prototype.</p>
<p></p>
<h2>Submission check</h2>
<p>In this exercise, the&nbsp;<strong>submission check of Task 1 will be performed in two steps</strong>:</p>
<ol>
    <li>You send the code with your solution and a Markdown file named README.md with a description of the files to Moodle (as usual). Then I check it, if everything is OK, we move to the second step.</li>
    <li>During our practical exercise, you share your screen and show how it works.</li>
</ol>
<p>After completion of these two steps, you pass the exercise.</p>
<p>However, submit also the solution for Task 2 (PDF or image). It will be evaluated by both&nbsp;lecturers.</p>
<p></p>
<h2>Guidance / Tutorials</h2>
<ul>
    <li>Connection and work with the University's servers: <a href="https://moodle.hs-anhalt.de/mod/wiki/view.php?id=46441" rel="nofollow">https://moodle.hs-anhalt.de/mod/wiki/view.php?id=46441</a></li>
    <li>How to work with Git: <a href="https://moodle.hs-anhalt.de/mod/wiki/view.php?id=64219" rel="nofollow">https://moodle.hs-anhalt.de/mod/wiki/view.php?id=64219</a></li>
    <li>How to work with University's GitLab: <a href="https://moodle.hs-anhalt.de/mod/wiki/view.php?id=48095" rel="nofollow">https://moodle.hs-anhalt.de/mod/wiki/view.php?id=48095</a></li>
    <li>Docker overview: <a href="https://docs.docker.com/engine/" rel="nofollow">https://docs.docker.com/engine/</a></li>
    <li>Docker Compose overview: <a href="https://docs.docker.com/compose/" rel="nofollow">https://docs.docker.com/compose/</a></li>
    <li>A comprehensive tutorial about Docker: <a href="https://github.com/vadikl/Projects-and-Materials/blob/main/Computer%20Science/Docker/Docker.ipynb">https://github.com/vadikl/Projects-and-Materials/blob/main/Computer%20Science/Docker/Docker.ipynb</a></li>
</ul>
<p></p>
<p></p>
