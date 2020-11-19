## Example of Qanary Framework usage with Python

```
├── app
│   ├── controllers.py - contains routes and logic for the Backend
│   ├── __init__.py - initializes the Backend
│   └── relation_prediction - folder with the Qanary component (can be located outside of the project)
│       ├── app.conf - conatins configuration parameters for the Backend
│       ├── app.py - runs the Qanary component "relation_prediction"
│       ├── classifier.py - file with classifier implementation and Qanary methods
├── config.py - conatins configuration parameters for the Backend
├── README.md
└── run.py - runs the Backend
```

## Steps to start the example

1. Run `pip install -r requirements.txt` in this directory
2. Download and unpack [ngrok](https://ngrok.com/download). (You will not need this step when you'll run it on server)
3. Set-up `serviceport` in `app.conf`
4. Run `./ngrok http YOUR_PORT` in the directory of the ngrok
5. Replace `servicehost` with the URL given by ngrok
6. Run `run.py`
7. Run `app.py`
8. Go to [Qanary Admin panel](http://webengineering.ins.hs-anhalt.de:43740) to see if your component is running
9. Use `/question` method of the Backend to start the Qanary pipeline

## Steps to implement a new Qanary component using Python

Note, that you have to split your QA system into separate components. Each component should be located within one package/folder (see this example).

### Step 1

Install `qanary_helpers` library via `pip install qanary-helpers`

### Step 2

Create basic component file structure:
* Create a directory for your component `my_component` and change your working directory to it;
* Create config file `app.conf` and specify the configuration parameters:

```
[ServiceConfiguration]
# the URL of the Spring Boot Admin server endpoint (e.g., http://localhost:8080)
springbootadminserverurl = http://localhost:8080/ # if you want to use our admin server, use http://webengineering.ins.hs-anhalt.de:43740
# Spring Boot Admin server credentials (by default: admin, admin)
springbootadminserveruser = admin
springbootadminserverpassword = admin
# the name of your service (e.g., my service)
servicename = my_component
# the port (integer) of your service (e.g., 5000)
serviceport = 1130
# the host of your service (e.g., http://127.0.0.1)
servicehost = http://127.0.0.1
# a description of your service functionality 
servicedescription = My component description
# version of component
serviceversion = 0.1.0
```

* Create a file with the component's implementation `my_component.py`:

```
from flask import Blueprint, jsonify, request
from qanary_helpers.configuration import Configuration
from qanary_helpers.qanary_queries import get_text_question_in_graph, insert_into_triplestore
import requests
import json
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
my_component = Blueprint('my_component', __name__, template_folder='templates')
configfile = "app.conf"

configuration = Configuration(configfile, [
    'servicename',
    'serviceversion'
])

@my_component.route("/annotatequestion", methods=['POST'])
def qanary_service():
    """the POST endpoint required for a Qanary service"""

    triplestore_endpoint = request.json["values"]["urn:qanary#endpoint"]
    triplestore_ingraph = request.json["values"]["urn:qanary#inGraph"]
    triplestore_outgraph = request.json["values"]["urn:qanary#outGraph"]

    logging.info(
        "endpoint: %s, inGraph: %s, outGraph: %s" % (triplestore_endpoint, triplestore_ingraph, triplestore_outgraph))

    text = get_text_question_in_graph(triplestore_endpoint=triplestore_endpoint, graph=triplestore_ingraph)[0]['text']

    logging.info(f'Question Text: {text}')

    # TODO: implement your logic here

    SPARQLquery = """
                    PREFIX qa: <http://www.wdaqua.eu/qa#>
                    PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
                    PREFIX dbo: <http://dbpedia.org/ontology/>
                    INSERT {{
                    GRAPH <{uuid}> {{
                        # TODO: implement your annotation here
                        ?a oa:annotatedBy <urn:qanary:{app_name}> .
                        ?a oa:annotatedAt ?time .
                        }}
                    }}
                    WHERE {{
                        BIND (IRI(str(RAND())) AS ?a) .
                        BIND (now() as ?time) 
                    }}
                """.format(
        uuid=triplestore_ingraph,
        app_name="{0}:{1}:Python".format(configuration.servicename, configuration.serviceversion)
    )  # building SPARQL query

    logging.info(f'SPARQL: {SPARQLquery}')

    insert_into_triplestore(triplestore_endpoint, triplestore_ingraph,
                            SPARQLquery)  # inserting new data to the triplestore

    return jsonify(request.get_json())


@my_component.route("/", methods=['GET'])
def index():
    """an example GET endpoint returning "hello world (String)"""

    logging.info("host_url: %s" % (request.host_url,))
    return "Hi! \n This is My Component."
```

* Create a file for the webservice implementaiton `app.py` (pay attention to the TODO comments):

```
import logging
import argparse
from flask import Flask, render_template
from datetime import datetime

from qanary_helpers.configuration import Configuration
from qanary_helpers.registration import Registration
from qanary_helpers.registrator import Registrator
from my_component import my_component # TODO: change it whenever you change the name of the previous file

# default config file (use -c parameter on command line specify a custom config file)
configfile = "app.conf"

# endpoint for Web page containing information about the service
aboutendpoint = "/about"

# endpoint for health information of the service required for Spring Boot Admin server callback
healthendpoint = "/health"

# initialize Flask app and add the externalized service information
app = Flask(__name__)
app.register_blueprint(my_component)

# holds the configuration
configuration = None


@app.route(healthendpoint, methods=['GET'])
def health():
    """required health endpoint for callback of Spring Boot Admin server"""
    return "alive"


@app.route(aboutendpoint)
def about():
    """optional endpoint for serving a web page with information about the web service"""
    return render_template("about.html", configuration=configuration)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # allow configuration of the configfile via command line parameters
    argparser = argparse.ArgumentParser(
        description='You might provide a configuration file, otherwise "%s" is used.' % (configfile))
    argparser.add_argument('-c', '--configfile', action='store', dest='configfile', default=configfile,
                           help='overwrite the default configfile "%s"' % (configfile))
    configfile = argparser.parse_args().configfile
    configuration = Configuration(configfile, [
        'springbootadminserverurl',
        'springbootadminserveruser',
        'springbootadminserverpassword',
        'servicehost',
        'serviceport',
        'servicename',
        'servicedescription',
        'serviceversion'
    ])

    try:
        configuration.serviceport = int(configuration.serviceport)  # ensure an int value for the server port
    except Exception as e:
        logging.error(
            "in configfile '%s': serviceport '%s' is not valid (%s)" % (configfile, configuration.serviceport, e))

    # define metadata that will be shown in the Spring Boot Admin server UI
    metadata = {
        "start": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "description": configuration.servicedescription,
        "about": "%s:%d%s" % (configuration.servicehost, configuration.serviceport, aboutendpoint),
        "written in": "Python"
    }

    # initialize the registation object, to be send to the Spring Boot Admin server
    myRegistration = Registration(
        name=configuration.servicename,
        serviceUrl="%s:%d" % (configuration.servicehost, configuration.serviceport), # TODO: if you are running with ngrok, change configuraiton.serviceport to 80
        healthUrl="%s:%d%s" % (configuration.servicehost, configuration.serviceport, healthendpoint), # TODO: if you are running with ngrok, change configuraiton.serviceport to 80
        metadata=metadata
    )

    # start a thread that will contact iteratively the Spring Boot Admin server
    registratorThread = Registrator(
        configuration.springbootadminserverurl,
        configuration.springbootadminserveruser,
        configuration.springbootadminserverpassword,
        myRegistration
    )
    registratorThread.start()

    # start the web service
    app.run(debug=True, port=configuration.serviceport)
```

### Step 3

Run `app.py` with `python app.py` and go to the admin panel e.g. http://webengineering.ins.hs-anhalt.de:43740/#/applications to see your component's status.

### How to expose multiple ports with ngrok?

1. Register free account at https://ngrok.com/;
2. Copy auth token in your dashboard;
3. Create `ngrok.yml` file in the same directory where your ngrok tool located. The structure of the `ngrok.yml`:
```
authtoken: PASTEYOURTOKENHERE
tunnels:
  first:
    addr: 1130
    proto: http    
  second:
    addr: 1180
    proto: http
```
4. Run ngrok with the following command (Linux): `./ngrok start -config ngrok.yml --all`
