# Handles all I/O between files. Modifies and formats text as needed before
# sending off to appropriate file.
import webScraper, mainGui

class inputOutputHandling:

    def recieveUserInput(text):
        gameChoice = text
        modifyText.prepareTextForWebSearch(gameChoice)

    def sendToScraper(text):
        webScraper.Example.printHelloWithInput(text)

class modifyText:

    def prepareTextForWebSearch(text):
        addPlus = text + '+'
        try:
            inputOutputHandling.sendToScraper(addPlus)

        except TypeError:
            print('nothing sent')
        