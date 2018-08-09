import requests
import urllib
from lxml import html
from time import sleep
import subprocess

# Disguises our bot
header = {'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

# Url we append user selections to
url = [
    'https://www.bing.com/search?q='
    ]

# User inputs
game = input(str("Choose a game: "))
platform = input(str("Choose a platform: "))

space = " "

# Configure user entries to work with url
if space in game and platform:
    gameSplit = game.split()
    platSplit = platform.split()
    gameJoin = "+".join(gameSplit)
    platJoin = "+".join(platSplit)
    newUrl = (url[0] + gameJoin + '+' + platJoin)

if space in game:
    gameSplit = game.split()
    gameJoin = "+".join(gameSplit)
    newUrl = (url[0] + gameJoin + '+' + platform)

if space in platform:
    platSplit = platform.split()
    platJoin = "+".join(platSplit)
    newUrl = (url[0] + game + '+' + platJoin)

# newUrl = (url[0] + gameJoin + '+' + platJoin)

    
# Retrieves page and content to parse
getPage = requests.get(newUrl)
htmlContent = html.fromstring(getPage.content)

# Scrapes for the amazon link
amazonLink = htmlContent.xpath('//*[@id="b_results"]/li[1]/h2/a/@href')
# Gets the amazon page
amazonPage = requests.get(amazonLink[0], headers= header)
# Downloads the amazon page to parse
amazonContent = html.fromstring(amazonPage.content)

# Retrieves items title, price, and cover
getTitle = amazonContent.xpath('//*[@id="productTitle"]/text()')
price1 = amazonContent.xpath('//*[@id="priceblock_ourprice"]/span[2]/text()')
price2 = amazonContent.xpath('//*[@id="priceblock_ourprice"]/span[3]/text()')
# sourcePic = amazonContent.xpath('//div[@id="imgTagWrapperId"]/img/@src')

# Gets the link to download the cover picture
# cover = sourcePic[0]

# Removes \n and white space from title
def fixTitle(t):
    titleSplit = t.split()
    title = ' '.join(titleSplit)
    print(title)

# Downloads the picture to our chosen location
# urllib.request.urlretrieve(cover, filename= 'Images_and_HTML/cover.jpg')

# Prints the title and price in our format
fixTitle(getTitle[0])
print("Price: ${}.{}" .format(price1[0], price2[0]))


# with open('url.html', 'wb') as test:
#     test.write(amazonPage.content)
#     subprocess.call(['open', 'url.html'])