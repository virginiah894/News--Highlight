from app import app
import urllib.request,json
from . models import news

News = news.News
# fetching the api key
api_key = app.config['NEWS_API_KEY']

# base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):

    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None
        if get_news_response['sources']:

            news_sources_list = get_news_response['sources']
            news_sources = process_sources(news_sources_list)
    return news_sources
def process_sources(news_list):


    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''

    news_sources = []
    for news_item in news_list:

        id = news_item.get('id')
        name = news_item.get('name')
        category = news_item.get('category')
        language = news_item.get('language')
        description = news_item.get('description')
        url = news_item.get('url')
        country = news_item.get('country')
        news_object=News(id,name,category,language,description,url,country)
        news_sources.append(news_object)
        # id,name,category,language,description,url,country
    return news_sources
    
