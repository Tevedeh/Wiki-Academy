import datetime
import time
import requests
from bs4 import BeautifulSoup
import os

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Crawler:

    baseurl = 'https://en.wikipedia.org'

    def __init__(self, seed, maximum, topics, filename):
        self.seed = seed
        self.maximum = maximum
        self.topics = topics
        self.filename = filename
        self.queue = []
        self.visited = []
        self.out = open(filename)
        self.accessInARow = 0


    def crawl(self):
        self.out.write(self.maximum)
        while len(self.visited) < self.maximum:
            print(f'RUN! Page is {self.queue[0]}')
            self.addLinks()
        self.printEdges()

    def getPage(self, link):
        self.startTime = time.time()
        self.accessInARow += 1
        if self.accessInARow >= 25:
            time.sleep(3)
            self.accessInARow = 0
        http = urllib3.PoolManager()
        page = http.request('GET', self.baseurl + link)
        soup = BeautifulSoup(page.data, 'html.parser')
        soupstr = str(soup).encode('utf-8')
        links = soup.find_all('a')
        for link in links:
            mystr = link.get('href')
            if mystr is None:
                print("None")
            elif 'wiki' in mystr:
                print(link.get('href'))
        return soupstr
        

        


    def checkTopics(self, page):
        for topic in self.topics:
            if not topic in page:
                return False
        return True


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