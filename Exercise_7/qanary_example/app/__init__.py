from flask import Flask, render_template
from app.controllers import main_module


app = Flask(__name__)
app.config.from_object('config')

# Register blueprint(s)
app.register_blueprint(main_module)
# app.register_blueprint(xyz_module)
# ..
