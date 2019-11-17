import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test to implement news behavior
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('CNN','general','en','View the latest news and breaking news today for U.S. world, weather, entertainment, politics and health at CNN','http://wwww.us.cnn.cnn','us')
# id,name,category,language,description,url,country
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news News))


if __name__ == '__main__':
    unittest.main()
