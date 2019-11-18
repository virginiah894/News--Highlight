from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap



def create_app(config_name):

  # beginning the app
  app = Flask(__name__)
  # environment configuration
  app.config.from_object(config_options[config_name])

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  #initialising flask extensions
  Bootstrap.init_app

  return app