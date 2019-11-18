import urllib.request,json
from . models import News, Highlights
from config import Config


# fetching the api key
global api_key,base_url
api_key = Config.NEWS_API_KEY

# base url
base_url = Config.NEWS_API_BASE_URL
highlight_url = Config.HIGHLIGHTS_BASE_URL
all_url = Config.ALL_ARTICLES_BASE_URL
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

# 
def get_highlights():


    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(highlight_url.format(api_key)) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        

        news_highlights = None
        if get_news_response['articles']:
            news_highlights_list = get_news_response['articles']
            news_highlights = process_highlights(news_highlights_list)
    return news_highlights
def process_highlights(news_list):


    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''

    news_highlights = []
    for news_item in news_list:

        Author = news_item.get('Author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        url = news_item.get('url')
        highlights_object=Highlights(Author,title,description,urlToImage,publishedAt,url)
        news_highlights.append(highlights_object)
        # id,name,category,language,description,url,country
        # if urlToImage:

        #     highlights_object = Highlights(Author,title,description,urlToImage,publishedAt,url)
        #     highlights_articles.append(highlights_object)



    return news_highlights

def get_all():

    get_news_details_url = all_url.format(api_key)


    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_all= None
        if news_details_response['articles']:
            news_all_list = news_details_response['articles']
            news_all = process_articles(news_all_list)
    return news_all

def process_articles(news_list):


    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''

    news_all= []
    for news_item in news_list:

        Author = news_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        url = news_item.get('url')
        highlights_object=Highlights(Author,title,description,urlToImage,publishedAt,url)
        news_all.append(highlights_object)
    return news_all


