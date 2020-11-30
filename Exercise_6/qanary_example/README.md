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

Please see this [tutorial](https://github.com/WDAqua/Qanary/wiki/How-to-Implement-a-Qanary-Component-using-Python-Qanary-Helpers).


### How to expose multiple ports with ngrok?

1. Register free account at https://ngrok.com/;
2. Copy auth token in your dashboard;
3. Create `ngrok.yml` file in the same directory where your ngrok tool located. The structure of the `ngrok.yml`:
```
authtoken: PASTEYOURTOKENHERE
tunnels:
  first:
    addr: 3002
    bind_tls: false
    proto: http    
  second:
    addr: 8080
    bind_tls: false
    proto: http
  third:
    addr: 8081
    bind_tls: false
    proto: http
  fourth:
    addr: 8082
    bind_tls: false
    proto: http
```
4. Run ngrok with the following command (Linux): `./ngrok start -config ngrok.yml --all`
