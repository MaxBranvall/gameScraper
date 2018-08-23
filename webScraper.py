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

    def sendToBackend(gameTitle, gamePrice):

        backend.BACKEND_IO.inputFromScraper(gameTitle, gamePrice)


class Scraping:

    def getURL(game, platform):

        URL = (url[0]+game+'+'+platform)
        print(URL)

        getBingPage = requests.get(URL, headers= header)       
        rawBingPage = html.fromstring(getBingPage.content)

        amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[2]/h2/a/@href')

        print(amazonLink)

        if ('amazon' in amazonLink[0]):

            getAmazonPage = requests.get(amazonLink[0], headers= header)
            getAmazonContent = html.fromstring(getAmazonPage.content)

            Scraping.scrapeContents(getAmazonContent)
        else:

            while ('amazon' not in amazonLink[0]): # this will keep searching hrefs until it finds Amazon

                n = 0
                n += 1

                amazonLink = rawBingPage.xpath('//*[@id="b_results"]/li[{}]/h2/a/@href' .format(n))

                if 'amazon' in amazonLink[0]:

                    print(amazonLink)
                    print('in link')

                    getAmazonPage = requests.get(amazonLink[0], headers= header)
                    getAmazonContent = html.fromstring(getAmazonPage.content)

                    Scraping.scrapeContents(getAmazonContent)

                else:

                    print('Not available')

    def scrapeContents(newUrl):

        # print('scrape')
        amazonPage = newUrl

        def getTitle():

            rawTitle = amazonPage.xpath('//*[@id="productTitle"]/text()')
            titleSplit = rawTitle[0].split()
            gameTitle = ' '.join(titleSplit)

            return gameTitle

        title = getTitle()

        try:
            print('amazon price') 
            price1 = amazonPage.xpath('//*[@id="priceblock_ourprice"]/span[2]/text()')
            price2 = amazonPage.xpath('//*[@id="priceblock_ourprice"]/span[3]/text()')

            price = ('${}.{}' .format(price1[0], price2[0]))

        except (IndexError):
            print('digital price')
            price1 = amazonPage.xpath('//*[@id="digital-button-price"]/span[2]/text()')
            price2 = amazonPage.xpath('//*[@id="digital-button-price"]/span[2]/text()')

            if (price1 == []):
                print('used price')
                price1 = amazonPage.xpath('//*[@id="priceblock_usedprice"]/span[2]/text()')
                price2 = amazonPage.xpath('//*[@id="priceblock_usedprice"]/span[3]/text()')

            try:
                price = ('${}.{}' .format(price1[0], price2[0]))
                SCRAPER_IO.sendToBackend(title, price)

            except IndexError:
                print(title)
                print(price1, price2)

        else:

            SCRAPER_IO.sendToBackend(title, price)

        
        finally:
            # print(getTitle())
            # print('$'+price1[0]+'.'+price2[0])
            pass   