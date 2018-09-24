"""Recieves and scrapes specified webpages. Will recieve properly handled user inputs from backend. Scraping results will be sent to backend.py."""

import requests, urllib, backend
from lxml import html

#TODO Refactor

url = [
    'https://www.bing.com/search?q=',
]

header = { 
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

class SCRAPER_IO:

    def inputFromBackend(game, platform):

        Scraping.getURL(game, platform)

    def sendToBackend(gameTitle, gamePrice, priceType):

        backend.BACKEND_IO.inputFromScraper(gameTitle, gamePrice, priceType)


class Scraping:

    def getURL(game, platform):

        def parseForLink(amazonLink, hrefNumber):

            while ('amazon' not in amazonLink[0]):

                hrefNumber += 1
                print(hrefNumber)

                amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[{}]/h2/a/@href' .format(hrefNumber))
                print(amazonLink)

                try:
                    if ('amazon' in amazonLink[0]):

                        print(amazonLink)

                        Scraping.retrievePage(amazonLink)
                        break

                    elif hrefNumber == 10:
                        print('Not Available')
                        break

                except IndexError:
                    pass

        hrefNumber = 1

        URL = (url[0]+game+'+'+platform) # Adds the game and platform to the search link
        print(URL) # Prints the bing search link

        getBingPage = requests.get(URL) # Retrieves the bing page      
        rawBingPage = html.fromstring(getBingPage.content) # Prepares the bing page for parsing

        amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[1]/h2/a/@href') # Grabs the first link from the bing results
        print(amazonLink) # prints the first link in a list

        try:
            if ('amazon' in amazonLink[0]):

                Scraping.retrievePage(amazonLink)

            else:
                print('parsing')
                parseForLink(amazonLink, hrefNumber)

        except IndexError:
            print(getBingPage)
            print('Index Error line 78')

    def retrievePage(amazonLink):

        def getTitle():

            rawTitle = amazonContent.xpath('//*[@id="productTitle"]/text()')
            titleSplit = rawTitle[0].split()
            gameTitle = ' '.join(titleSplit)

            return gameTitle

        print('retrieve page')
        print(amazonLink)
        getAmazonPage = requests.get(amazonLink[0], headers= header)
        amazonContent = html.fromstring(getAmazonPage.content)

        title = getTitle()

        Utility.getPrice(amazonContent, title)

class Utility:

    priceSpecs = ["priceblock_ourprice", "digital-button-price", "priceblock_usedprice"]

    def getPrice(amazonPage, title, n= 0):

        if (n in list(range(0, 3))):
            price1 = amazonPage.xpath('//*[@id="{}"]/span[2]/text()' .format(Utility.priceSpecs[n]))
            price2 = amazonPage.xpath('//*[@id="{}"]/span[3]/text()' .format(Utility.priceSpecs[n]))

            if price1 == []: # If the price is an empty list, try the next index in priceSpecs
                n += 1
                Utility.getPrice(amazonPage, title, n= n)

            else: # If price1 is != [], pass all parameters to be set and ready to send to backend
                Utility.setPriceandTitle(n, title, price1, price2)

        elif (n == 3):
            price = amazonPage.xpath('//*[@id="buybox"]/div[1]/span/a/text()')
            Utility.setPriceandTitle(n, title, usedPrice=price)

    def setPriceandTitle(n, title, price1=None, price2=None, usedPrice=None):

        if n == 0:
            priceType = "Amazon Price"
        
        elif n == 1:
            priceType = "Digital Price"

        elif n == 2:
            priceType = "Used Price"

        elif n == 3:
            priceType = "Used and New From"

        if (n in list(range(0,3))):
            price = ('${}.{}' .format(price1[0], price2[0]))
            SCRAPER_IO.sendToBackend(title, price, priceType)

        if (n == 3):
            price = usedPrice[0].split()[-1]
            SCRAPER_IO.sendToBackend(title, price, priceType)
