# Handles all I/O between files. Modifies and formats text as needed before
# sending off to appropriate file.
import webScraper, mainGui

class BACKEND_IO:

    def inputFromGUI(game, platform):

        gameChoice = game
        platformChoice = platform
        Modification.gameAndPlatformModification(gameChoice, platformChoice)

    def sendToScraper(game, platform):
        
        webScraper.SCRAPER_IO.inputFromBackend(game, platform)

class Modification:

    def gameAndPlatformModification(game, platform):

        try:
            gameSplit = game.split()
            platformSplit = platform.split()

            if (gameSplit == []):
                raise ValueError

        except ValueError:
            print('Invalid Game Choice')

        else:
            gameJoin = '+'.join(gameSplit)
            platformJoin = '+'.join(platformSplit)
            BACKEND_IO.sendToScraper(gameJoin, platformJoin)

        
        