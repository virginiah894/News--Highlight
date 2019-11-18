from flask import render_template
from . import main
from ..request import get_news,get_highlights


@main.route('/')
def index():
  general_news = get_news('general')
  # business_news = get_news('business')
  # technology_news = get_news('technology')
  sports_news = get_news('sports')
  title = 'NEWS NOW.COM-Home for all news updates'
  name = 'ABC News'

  return render_template('index.html',title= title,name = name,sports=sports_news )
@main.route('/highlights')
def highlights():

    '''
    View movie page function that returns the movie details page and its data
    '''
    highlights = get_highlights()
    title = f'{highlights.name}'

    return render_template('highlights.html',title = title,highlights=highlights)
