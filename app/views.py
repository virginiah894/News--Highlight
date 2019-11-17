from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():
  general_news = get_news('general')
  business_news = get_news('business')
  technology_news = get_news('technology')
  sports_news = get_news('sports')
  name = 'ABC News'

  return render_template('index.html',name = name,general = general_news,business = business_news,technology = technology_news,sports = sports_news)
