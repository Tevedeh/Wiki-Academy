from crawler import Crawler

crawl = Crawler(seed=0, maximum=0, topics=0, filename=0)

hello = crawl.getPage(link='/wiki/Iowa_State_University')

print(hello)



