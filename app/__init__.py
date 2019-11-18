from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap



# beginning the app
app = Flask(__name__,instance_relative_config = True)

# environment configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
from app import views
bootstrap = Bootstrap(app)
from app import error