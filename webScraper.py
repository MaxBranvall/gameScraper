# Recieves and scrapes specified webpages. Will recieve properly handled user inputs
# from backend. Scraping results will be sent to backend.py.
import requests, urllib, backend
from lxml import html

url = [
    'https://www.bing.com/search?q=',
]

header = { 
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


class SCRAPER_IO:

    def inputFromBackend(game, platform):

        Scraping.getURL(game, platform)

    def sendToBackend():

        
        Scraping.getURL.URL

class Scraping:

    def getURL(game, platform):

        URL = (url[0]+game+'+'+platform)
        print(URL)

        getPage = requests.get(URL, headers= header)       
        rawPage = html.fromstring(getPage.content)

        amazonLink = rawPage.xpath('//*[@id="b_results"]/li[2]/h2/a/@href')

        while ('amazon' not in amazonLink[0]): # this will keep searching hrefs until it finds Amazon

            n = 0
            n += 1

            amazonLink = rawPage.xpath('//*[@id="b_results"]/li[{}]/h2/a/@href' .format(n))

            if 'amazon' in amazonLink[0]:

                print(amazonLink)
                print('in link')

                getAmazonPage = requests.get(amazonLink[0], headers= header)
                getAmazonContent = html.fromstring(getAmazonPage.content)

                Scraping.scrapeContents(getAmazonContent)
        
        # print('getAmazon')
        getAmazonPage = requests.get(amazonLink[0], headers= header)
        getAmazonContent = html.fromstring(getAmazonPage.content)

        Scraping.scrapeContents(getAmazonContent)

    def scrapeContents(newUrl):

        # print('scrape')
        amazonPage = newUrl

        def getTitle():

            rawTitle = amazonPage.xpath('//*[@id="productTitle"]/text()')
            titleSplit = rawTitle[0].split()
            gameTitle = ' '.join(titleSplit)

            return gameTitle

        try:
            price1 = amazonPage.xpath('//*[@id="priceblock_ourprice"]/span[2]/text()')
            price2 = amazonPage.xpath('//*[@id="priceblock_ourprice"]/span[3]/text()')

            if (IndexError): # this will happen if amazon pulls up a used sale first
                price1 = amazonPage.xpath('//*[@id="priceblock_usedprice"]/span[2]/text()')
                price2 = amazonPage.xpath('//*[@id="priceblock_usedprice"]/span[3]/text()')
        
        finally:
            print(getTitle())
            print('$'+price1[0]+'.'+price2[0])

        