class Crawler():

    baseurl = 'https://en.wikipedia.org'

    def __init__(self, seed, maximum, topics, filename):
        self.seed = seed
        self.maximum = maximum
        self.topics = topics
        self.filename = filename
        self.queue = []

    def crawl(self):
        pass
    
    def getPage(self):
        pass

    def checkTopics(self):
        pass

    def printEdges(self):
        pass

    def addLinks(self):
        pass

    def findEdge(self):
        pass

    def printVisited(self):
        pass

    def printQueue(self):
        for x in self.queue:
            print(x)
