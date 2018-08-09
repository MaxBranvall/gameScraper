# Recieves and scrapes specified webpages. Will recieve properly handled user inputs
# from backend. Scraping results will be sent to backend.py.
import requests, urllib, backend

url = [
    'https://www.bing.com/search?q=',
]


class SCRAPER_IO:

    def inputFromBackend(game, platform):

        gameChoice = game
        platformChoice = platform

        print(gameChoice, platformChoice)