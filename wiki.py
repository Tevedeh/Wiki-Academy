import datetime
import time
import requests
from bs4 import BeautifulSoup
import urllib3

class PageData():

    baseurl = 'https://en.wikipedia.org'

    def __init__(self, data):
        self.soup = data

    def getLinks:

class WikiScrape():
    baseurl = 'https://en.wikipedia.org'

    def __init__(self, seed, maximum, topics, filename):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.seed = seed
        self.maximum = maximum
        self.topics = topics
        self.filename = filename
        self.queue = []
        self.visited = []
        self.out = open(filename)
        self.startTime = 0.0
        self.accessTime = 0.0
        self.topicTime = 0.0
        self.linkTime = 0.0
        self.subStringTime = 0.0
        self.accessInARow = 0

    def getPageData(self, link):
        self.startTime = time.time()
        self.accessInARow += 1
        if self.accessInARow >= 25:
            time.sleep(3)
            self.accessInARow = 0
        http = urllib3.PoolManager()
        page = http.request('GET', self.baseurl + link)
        return PageData(data = BeautifulSoup(page.data, 'html.parser')
    

        


    def checkTopics(self):
        pass

    def printEdges(self):
        pass

    def addLinks(self):
        pass

    def findEdge(self):
        pass

    def printVisited(self):
        for x in self.visited:
            print(x)

    def printQueue(self):
        for x in self.queue:
            print(x)
