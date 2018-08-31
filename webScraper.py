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

        foo = 0

        URL = (url[0]+game+'+'+platform) # Adds the game and platform to the search link
        print(URL) # Prints the bing search link

        getBingPage = requests.get(URL, headers= header) # Retrieves the bing page      
        rawBingPage = html.fromstring(getBingPage.content) # Prepares the bing page for parsing

        amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[1]/h2/a/@href') # Grabs the first link from the bing results
        print(amazonLink) # prints the first link in a list

        if ('amazon' in amazonLink[0]):

            Extra.retrievePage(amazonLink)

        else:

            while ('amazon' not in amazonLink[0]): # this will keep searching hrefs until it finds Amazon

                foo += 1

                amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[{}]/h2/a/@href' .format(foo))

                try:
                    if 'amazon' in amazonLink[0]:

                        print(amazonLink)
                        print('in link')

                        Extra.retrievePage(amazonLink)

                    elif foo == 10:
                        print('Not Available')
                        break

                except IndexError: #TODO this prints if the game isn't on amazon
                    print('empty amazon list')
                    break

    def scrapeContents(newUrl):

        amazonPage = newUrl

        def getTitle():

            rawTitle = amazonPage.xpath('//*[@id="productTitle"]/text()')
            titleSplit = rawTitle[0].split()
            gameTitle = ' '.join(titleSplit)

            return gameTitle

        title = getTitle()

        Extra.getPrice(amazonPage)

        # try: # This price will be shown if it is a physical copy
        #     print('amazon price') 
        #     price1 = amazonPage.xpath('//*[@id="priceblock_ourprice"]/span[2]/text()')
        #     price2 = amazonPage.xpath('//*[@id="priceblock_ourprice"]/span[3]/text()')

        #     price = ('${}.{}' .format(price1[0], price2[0]))

        # except (IndexError): # This price will be shown if it is a digital copy
        #     print('digital price')
        #     price1 = amazonPage.xpath('//*[@id="digital-button-price"]/span[2]/text()')
        #     price2 = amazonPage.xpath('//*[@id="digital-button-price"]/span[2]/text()')

        #     if (price1 == []): # This price will be shown if it is a used copy
        #         print('used price')
        #         price1 = amazonPage.xpath('//*[@id="priceblock_usedprice"]/span[2]/text()')
        #         price2 = amazonPage.xpath('//*[@id="priceblock_usedprice"]/span[3]/text()')

        # try:
        #     price = ('${}.{}' .format(price1[0], price2[0]))
        #     SCRAPER_IO.sendToBackend(title, price)

        # except IndexError:
        #     print(title)
        #     print(price1, price2)

        # else:

        # SCRAPER_IO.sendToBackend(title, price)

        
        # finally:
            # print(getTitle())
            # print('$'+price1[0]+'.'+price2[0])
            # pass

class Extra:

    priceSpecs = ["priceblock_ourprice", "digital-button-price", "priceblock_usedprice"]

    def retrievePage(amazonLink):

        print('retrieving..')
        getAmazonPage = requests.get(amazonLink[0], headers= header)
        getAmazonContent = html.fromstring(getAmazonPage.content)

        Scraping.scrapeContents(getAmazonContent)

    def getPrice(amazonPage):

        n = 0 

        try:
            price1 = amazonPage.xpath('//*[@id="{}"]/span[2]/text()' .format(Extra.priceSpecs[n]))
            price2 = amazonPage.xpath('//*[@id="{}"]/span[3]/text()' .format(Extra.priceSpecs[n]))

            if price1 == []:
                raise IndexError

        except IndexError:
            n += 1
            print(n)
            Extra.getPrice(n)
        
        else:
            Extra.setPrice(n, price1, price2)

    def setPrice(n, price1, price2):

        if n == 0:
            print('Amazon Price')
        
        elif n == 1:
            print('Digital Price')

        else:
            Print('Used Price')

        price = ('${}.{}' .format(price1, price2))
        print(price)