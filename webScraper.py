# Recieves and scrapes specified webpages. Will recieve properly handled user inputs
# from backend. Scraping results will be sent to backend.py.
import requests, urllib, backend
from lxml import html

#TODO Refactor

url = [
    'https://www.bing.com/search?q=',
]

header = { 
    'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


class SCRAPER_IO:

    def inputFromBackend(game, platform):

        Scraping.getURL(game, platform)

    def sendToBackend(gameTitle, gamePrice):

        backend.BACKEND_IO.inputFromScraper(gameTitle, gamePrice)


class Scraping:

    def getURL(game, platform):

        hrefNumber = 0

        URL = (url[0]+game+'+'+platform) # Adds the game and platform to the search link
        print(URL) # Prints the bing search link

        getBingPage = requests.get(URL, headers= header) # Retrieves the bing page      
        rawBingPage = html.fromstring(getBingPage.content) # Prepares the bing page for parsing

        amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[1]/h2/a/@href') # Grabs the first link from the bing results
        print(amazonLink) # prints the first link in a list

        if ('amazon' in amazonLink[0]):

            Scraping.retrievePage(amazonLink)

        else:

            while ('amazon' not in amazonLink[0]): # this will keep searching hrefs until it finds Amazon

                hrefNumber += 1

                amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[{}]/h2/a/@href' .format(hrefNumber))

                try:
                    if 'amazon' in amazonLink[0]:

                        print(amazonLink)
                        print('in link')

                        Scraping.retrievePage(amazonLink)

                    elif hrefNumber == 10:
                        print('Not Available')
                        break

                except IndexError: #TODO this prints if the game isn't on amazon
                    print('empty amazon list')
                    break

    def retrievePage(amazonLink):

        def getTitle():

            rawTitle = amazonContent.xpath('//*[@id="productTitle"]/text()')
            titleSplit = rawTitle[0].split()
            gameTitle = ' '.join(titleSplit)

            return gameTitle

        getAmazonPage = requests.get(amazonLink[0], headers= header)
        amazonContent = html.fromstring(getAmazonPage.content)

        title = getTitle()

        Utility.getPrice(amazonContent, title)

class Utility:

    priceSpecs = ["priceblock_ourprice", "digital-button-price", "priceblock_usedprice"]

    def getPrice(amazonPage, title, n= 0):
        
        price1 = amazonPage.xpath('//*[@id="{}"]/span[2]/text()' .format(Utility.priceSpecs[n]))
        price2 = amazonPage.xpath('//*[@id="{}"]/span[3]/text()' .format(Utility.priceSpecs[n]))

        if price1 == []:
            n += 1
            Utility.getPrice(amazonPage, title, n= n)

        else:
            Utility.setPriceandTitle(n, title, price1, price2)

    def setPriceandTitle(n, title, price1, price2):

        if n == 0:
            print('Amazon Price')
        
        elif n == 1:
            print('Digital Price')

        else:
            print('Used Price')

        price = ('${}.{}' .format(price1[0], price2[0]))
        
        SCRAPER_IO.sendToBackend(title, price)