

import unittest

from app.models import Sources

class ArticlesTest(unittest.TestCase):

    def setUp(self):
        self.new_Source=Sources('abc-news','ABC news','Your trusted source for breaking news',"https://abcnews.go.com","general","en","us")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__=="__main__":
    unittest.main()