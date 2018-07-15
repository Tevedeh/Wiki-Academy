import datetime
import time
import requests
from bs4 import BeautifulSoup

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Crawler():

    baseurl = 'https://en.wikipedia.org'

    def __init__(self, seed, maximum, topics, filename):
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


    def crawl(self):
        self.out.write(self.maximum)
        while len(self.visited) < self.maximum:
            print(f'RUN! Page is {self.queue[0]}')
            self.addLinks()
        self.printEdges()
        print(self.accessTime)
        print(self.topicTime)
        print(self.linkTime)
        print(self.subStringTime)

    def getPage(self, link):
        self.startTime = time.time()
        self.accessInARow += 1
        if self.accessInARow >= 25:
            time.sleep(3)
            self.accessInARow = 0
        #print(self.baseurl+link)
        http = urllib3.PoolManager()
        page = http.request('GET', self.baseurl + link)
        #soup = BeautifulSoup(page.data, 'html.parser').find_all('a')  
        soup = BeautifulSoup(page.data, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            mystr = link.get('href')
            if mystr is None:
                print("None")
            elif 'wiki' in mystr:
                print(link.get('href'))

        


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


crawler = Crawler(seed=0, maximum=0, topics=0, filename=0)

crawler.getPage(link='/wiki/Iowa_State_University')