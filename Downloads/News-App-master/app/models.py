

class Article:
    
    '''
    News  class to define News Objects
    '''
    def __init__(self, author, title,description,publishedAt,content,urlToImage):
        self.title=title
        self.author=author
        self.description=description
        self.urlToImage=urlToImage
        self.content=content
        self.publishedAt=publishedAt

class Source:
    '''
    Sources class that defines each source object
    '''

    def __init__(self,id, name, description,url,category,language,country):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.country=country