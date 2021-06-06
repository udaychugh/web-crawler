import scrapy


class spider1(scrapy.Spider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Battery_(electricity)']

    def parse(self, response):
        pass


import requests
from bs4 import BeautifulSoup


def web(page, WebUrl):
    if page > 0:
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class': 's-access-details-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)


enterUrl = input("Enter Url=")

web(1, enterUrl)
