import os


DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
CSRF_ENABLED = True
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"
HOST = '0.0.0.0'
PORT = 8000
