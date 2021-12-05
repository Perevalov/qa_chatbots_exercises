# Template for Qanary component

## How to run

In this directory run:

1. `docker build -t my-qanary-container .`
1. `docker-compose up` 

## Environment variables description

SPRING_BOOT_ADMIN_URL -- URL of the Qanary pipeline
SPRING_BOOT_ADMIN_USERNAME -- the admin username of the Qanary pipeline
SPRING_BOOT_ADMIN_PASSWORD -- the admin password of the Qanary pipeline
SERVICE_HOST -- the host of your component without protocol prefix (e.g. http://). It has to be visible to the Qanary pipeline
SERVICE_PORT -- the port of your component (has to be visible to the Qanary pipeline)
SERVICE_NAME_COMPONENT -- the name of your component
SERVICE_DESCRIPTION_COMPONENT -- the description of your component

You may also change the configuration via environment variables to any configuration that you want (e.g. via a json file).