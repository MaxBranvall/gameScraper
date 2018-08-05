import requests
import urllib
from lxml import html
from time import sleep
import subprocess
import qtGui

# getPage, getPrice, getTitle.
# setPage, setPrice, setTitle

url = [
    'https://www.bing.com/search?q=',
]

class GetSetSite:

    def __init__(self, userUrl):
        self.userUrl = userUrl
        self.game = None
        self.platform = None
        print(userUrl)

    def chooseGameandPlatform(self):
        self.game = input(str('Enter a game: '))
        self.platform = input(str("Choose a platform: "))

        self._addToLink(self.game, self.platform)
    
    def _addToLink(self, game, platform):
        newUrl = (self.userUrl[0] + game + platform)
        print(newUrl)

        self._getPage(newUrl)

    def _getPage(self, urlPage):
        # Download the webPage
        page = requests.get(urlPage)
        # Pass the page to be set
        self._setPage(page)

    def _setPage(self, pageSet):
        # extract raw html elements from page
        rawPage = html.fromstring(pageSet.content)
        print('Page Set')
        

class1 = GetSetSite(url)
class2 = GetSetSite(url)


if __name__ == '__main__':
    