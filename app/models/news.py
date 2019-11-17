class News:
    '''
    Movie class to instantiate news
    '''

    def __init__(self,id,name,category,language,poster,description,url):
        self.id =id
        self.name = name
        self.category = category
        self.language = language
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.description = description
        self.url = url


        