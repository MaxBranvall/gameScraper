# Handles all I/O between files. Modifies and formats text as needed before
# sending off to appropriate file.
import webScraper, mainGui

class BACKEND_IO:

    def inputFromGUI(game, platform):

        gameChoice = game
        platformChoice = platform
        Modification.gameAndPlatformModification(gameChoice, platformChoice)

    def inputFromScraper(gameTitle, gamePrice, priceType):

        BACKEND_IO.sendToGui(title= gameTitle, price= gamePrice, priceType= priceType)
        

    def sendToScraper(game, platform):

        webScraper.SCRAPER_IO.inputFromBackend(game, platform)

    def sendToGui(title, price, priceType):

        mainGui.GUI_IO.fromBackend(title= title, price= price, priceType= priceType)

class Modification:

    def gameAndPlatformModification(game, platform):


        gameSplit = game.split()
        platformSplit = platform.split()

        gameJoin = '+'.join(gameSplit)
        platformJoin = '+'.join(platformSplit)
        BACKEND_IO.sendToScraper(gameJoin, platformJoin)        