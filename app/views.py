from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():
  general = news()
  return render_template('index.html',general = general)
