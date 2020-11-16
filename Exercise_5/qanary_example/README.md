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
3. Set-up `serviceport` in `app.conf` and run `./ngrok http YOUR_PORT` in the directory of the ngrok
4. Run `run.py`
5. Run `app.py`
6. Go to [Qanary Admin panel](http://webengineering.ins.hs-anhalt.de:43740) to see if your component is running
7. Use `/question` method of the Backend to start the Qanary pipeline