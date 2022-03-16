class Article:
    
    '''
    News  class to define News Objects
    '''
    def __init__(self, author,title,description,urlToImage,content,publishedAt):
        self.title=title
        self.author=author
        self.description=description
        self.urlToImage=urlToImage
        self.content=content
        self.publishedAt=publishedAt