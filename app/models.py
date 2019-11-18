class News:
    '''
    Class to instantiate news sources
    '''

    def __init__(self,id,name,category,language,description,url,country):
        self.id = id
        self.name = name
        self.category = category
        self.language = language
        self.description = description
        self.url = url
        self.country = country

class Highlights:
    def __init__(self,Author,title,description,urlToImage,publishedAt,url):
        self.Author = Author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self. publishedAt= publishedAt
        self.url = url
  
  



        