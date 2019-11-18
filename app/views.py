from flask import render_template
from app import app
from .request import get_news,get_source


@app.route('/')
def index():
  general_news = get_news('general')
  business_news = get_news('business')
  technology_news = get_news('technology')
  sports_news = get_news('sports')
  title = 'NEWS NOW.COM-Home for all news updates'
  name = 'ABC News'

  return render_template('index.html',title= title,name = name,general = general_news,business = business_news,technology = technology_news,sports = sports_news)
@app.route('/source/<int:id>')
def source(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    source = get_source(id)
    title = f'{news.name}'

    return render_template('source.html',title = title,news = news)
