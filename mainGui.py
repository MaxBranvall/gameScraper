# GUI of the program. User inputs will be sent to backend.py to be handled.
# Prices, titles, etc. will be recieved from backend.py ready to be displayed.

# BUG light grey/default background is bugged and doesn't clear textbox and combo box properly..

# This is in empty price list branch

import sys, backend, random, linecache, Untitled
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton,
                            QLabel, QLineEdit, QComboBox, QMainWindow, 
                            QWidget, QApplication, QMessageBox, QDesktopWidget, QStackedWidget, QStackedLayout)
from PyQt5.QtGui import QFont


# testtest

# This class will handle all input and output for the GUI
class GUI_IO:

    def sendToBackend(game, platform):

        backend.BACKEND_IO.inputFromGUI(game, platform)

    def fromBackend(title=None, price=None):

        gameTitle = title
        gamePrice = price

        priceAndTitleScreen = PriceandTitleScreen()

        priceAndTitleScreen.fromGUI_IO(gameTitle, gamePrice)


# The frame and main window.
class Main(QMainWindow):

    def __init__(self):
        
        super().__init__()
        
        self.windowPreferences()
        self.showMainMenuScreen()

    def showMainMenuScreen(self):

        self.mainMenuScreen = MainMenuScreen()
        self.setCentralWidget(self.mainMenuScreen)

        self.mainMenuScreen.testButton.clicked.connect(self.showPriceandTitleScreen)
        self.mainMenuScreen.searchButton.clicked.connect(self.showPriceandTitleScreen)
        self.show()

    def showPriceandTitleScreen(self):

        self.priceAndTitleScreen = PriceandTitleScreen()
        self.setCentralWidget(self.priceAndTitleScreen)
        
        self.priceAndTitleScreen.testButton1.clicked.connect(self.showMainMenuScreen)
        self.show()

    def windowPreferences(self):

        # self.setStyleSheet('{background : black}')
        self.setStyleSheet("QMainWindow {background-image: url(Images_and_HTML/carbonBG.jpg)}")

        self.resize(600, 400)
        self.center()
        
        self.setWindowTitle('The Frugal Gamer')

        self.show()

    def center(self):  # Centers window on screen

        windowFrame = self.frameGeometry()
        centerOfMonitor = QDesktopWidget().availableGeometry().center()

        windowFrame.moveCenter(centerOfMonitor)
        self.move(windowFrame.topLeft())

# holds all widgets


class MainMenuScreen(QWidget):

    PLATFORMS = ['Selections:', 'Xbox One', 'PlayStation 4', 'PC', 'Nintendo Switch']

    def __init__(self, layout=1):

        super().__init__()

        self.mainFontColor = 'color: #d3d3d3'  # Light grey font color

        self.mainTitleFont = QFont('Sans Serif', 40, 30)  # Font Name, Size, Weight, Italics
        self.subTitleFont = QFont('Sans Serif', 30, 10)

        self.initUI()
        # self.show()

        mainScreenLayout = QVBoxLayout()
        mainScreenLayout.addLayout(self.welcomeTitleHbox)
        mainScreenLayout.addLayout(self.topVBox)
        mainScreenLayout.addLayout(self.chooseGameHbox)
        mainScreenLayout.addLayout(self.gameTextboxHox)
        mainScreenLayout.addLayout(self.choosePlatformHbox)
        mainScreenLayout.addLayout(self.platformSelectorHbox)
        mainScreenLayout.addLayout(self.middleVBox)
        mainScreenLayout.addLayout(self.bottomVBox)
        mainScreenLayout.addLayout(self.searchAndClearHbox)

        self.setLayout(mainScreenLayout)

    def initUI(self):
        
        # All widgets will be created here

        self.welcomeTitle = QLabel('Welcome Frugal Gamer!')
        self.chooseGameLabel = QLabel('Type a Game: ')
        self.choosePlatformLabel = QLabel('Choose a Platform: ')

        self.searchButton = QPushButton('Search')
        self.savedSearchesButton = QPushButton('Coming Soon\nSaved Searches')
        self.clearTextboxButton = QPushButton('Clear')
        self.testButton = QPushButton('Switch Layout', self)

        self.chooseGameTextbox = QLineEdit()
        self.choosePlatformBox = QComboBox()

        # Modify and add widget functionality here

        self.welcomeTitle.setFont(self.mainTitleFont)
        self.chooseGameLabel.setFont(self.subTitleFont)
        self.choosePlatformLabel.setFont(self.subTitleFont)
        self.choosePlatformBox.addItems(self.PLATFORMS)

        self.welcomeTitle.setStyleSheet(self.mainFontColor)
        self.chooseGameLabel.setStyleSheet(self.mainFontColor)
        self.choosePlatformLabel.setStyleSheet(self.mainFontColor)

        self.searchButton.clicked.connect(self.resultsToGUI_IO)
        self.clearTextboxButton.clicked.connect(self.clearTextbox)

        self.testButton.move(10, 10)
        self.testButton.resize(self.testButton.sizeHint())

        # self.savedSearchesButton.disconnect()

        # Call layout methods here
        self.labelLayout()
        self.buttonAndInputLayout()
        self.extraVBoxes()

    # Functionality Methods

    def changeText(self):
        print('button clicked')
        # self.welcomeTitle.setText('Changed')

    def switchLayoutTest(self):
        pass

    # def closeWindow(self):
    #     # self.close()
    #     pass

    def clearTextbox(self):
        self.chooseGameTextbox.clear()

    def statusBarHandling(self, message=None):

        pass

    # Layout Methods

    def labelLayout(self):

        welcomeTitleForm = QFormLayout()
        welcomeTitleForm.addRow(self.welcomeTitle)

        self.welcomeTitleHbox = QHBoxLayout()
        self.welcomeTitleHbox.addStretch()
        self.welcomeTitleHbox.addLayout(welcomeTitleForm)
        self.welcomeTitleHbox.addStretch()

        chooseGameForm = QFormLayout()
        chooseGameForm.addRow(self.chooseGameLabel)

        self.chooseGameHbox = QHBoxLayout()
        self.chooseGameHbox.addStretch()
        self.chooseGameHbox.addLayout(chooseGameForm)
        self.chooseGameHbox.addStretch()

        choosePlatformForm = QFormLayout()
        choosePlatformForm.addRow(self.choosePlatformLabel)

        self.choosePlatformHbox = QHBoxLayout()
        self.choosePlatformHbox.addStretch()
        self.choosePlatformHbox.addLayout(choosePlatformForm)
        self.choosePlatformHbox.addStretch()

    def buttonAndInputLayout(self):

        chooseGameTextboxForm = QFormLayout()
        chooseGameTextboxForm.addRow(self.chooseGameTextbox)

        self.gameTextboxHox = QHBoxLayout()
        self.gameTextboxHox.addStretch(3)
        self.gameTextboxHox.addLayout(chooseGameTextboxForm)
        self.gameTextboxHox.addWidget(self.clearTextboxButton)
        self.gameTextboxHox.addStretch(3)

        choosePlatformBoxForm = QFormLayout()
        choosePlatformBoxForm.addRow(self.choosePlatformBox)

        self.platformSelectorHbox = QHBoxLayout()
        self.platformSelectorHbox.addStretch()
        self.platformSelectorHbox.addLayout(choosePlatformBoxForm)
        self.platformSelectorHbox.addStretch()

        self.searchAndClearHbox = QHBoxLayout()
        self.searchAndClearHbox.addWidget(self.savedSearchesButton)
        self.searchAndClearHbox.addStretch()
        self.searchAndClearHbox.addWidget(self.searchButton)

    def extraVBoxes(self):

        self.topVBox = QVBoxLayout()
        self.topVBox.addStretch()

        self.middleVBox = QVBoxLayout()
        self.middleVBox.addStretch()

        self.bottomVBox = QVBoxLayout()
        self.bottomVBox.addStretch()    # Sends choices to GUI_IO

    def resultsToGUI_IO(self):

        try:
            gameChoice = self.chooseGameTextbox.text()
            platFormChoice = self.choosePlatformBox.currentText()

            if (platFormChoice == self.PLATFORMS[0]):
                raise ValueError
        
        except ValueError:
            # display warning message in window
            warningMessages(warning='invalidPlatform')
        
        else:
            GUI_IO.sendToBackend(gameChoice, platFormChoice)
            self.chooseGameTextbox.clear()
            self.switchLayoutTest()


class PriceandTitleScreen(QWidget):

    cacheFile = 'gameCache.txt'

    def __init__(self):

        super().__init__()

        self.mainFontColor = 'color: #d3d3d3'  # Light grey font color

        self.mainTitleFont = QFont('Sans Serif', 40, 30)  # Font Name, Size, Weight, Italics
        self.subTitleFont = QFont('Sans Serif', 30, 10)

        # self.setLabels()
        self.initUI()
        # self.show()

        mainScreenLayout = QVBoxLayout()
        mainScreenLayout.addLayout(self.gameTitleHbox)
        mainScreenLayout.addLayout(self.listPriceHbox)
        mainScreenLayout.addLayout(self.gamePriceHbox)
        mainScreenLayout.addLayout(self.bottomVBox)

        self.setLayout(mainScreenLayout)

    def initUI(self):

        cacheLine1 = linecache.getline(self.cacheFile, 1)

        # Create widgets here
        self.gameTitleLabel = QLabel(cacheLine1)
        self.listPriceLabel = QLabel('List Price:')
        self.gamePriceLabel = QLabel('Price')
        self.testButton = QPushButton('change text')
        self.testButton1 = QPushButton('change layout', self)

        # Modify widgets here
        self.gameTitleLabel.setFont(self.mainTitleFont)
        self.listPriceLabel.setFont(self.subTitleFont)
        self.gamePriceLabel.setFont(self.subTitleFont)

        self.gameTitleLabel.setStyleSheet(self.mainFontColor)
        self.listPriceLabel.setStyleSheet(self.mainFontColor)
        self.gamePriceLabel.setStyleSheet(self.mainFontColor)

        self.testButton1.resize(self.testButton1.sizeHint())
        self.testButton1.move(10, 10)

        # self.testButton.clicked.connect(self.testFunc)

        # Call layout methods here
        self.labelLayout()
        self.extraVBoxes()

    def labelLayout(self):

        gameTitleForm = QFormLayout()
        gameTitleForm.addRow(self.gameTitleLabel)
        gameTitleForm.addRow(self.testButton)

        self.gameTitleHbox = QHBoxLayout()
        self.gameTitleHbox.addStretch()
        self.gameTitleHbox.addLayout(gameTitleForm)
        self.gameTitleHbox.addStretch()

        listPriceForm = QFormLayout()
        listPriceForm.addRow(self.listPriceLabel)

        self.listPriceHbox = QHBoxLayout()
        self.listPriceHbox.addStretch()
        self.listPriceHbox.addLayout(listPriceForm)
        self.listPriceHbox.addStretch()

        gamePriceForm = QFormLayout()
        gamePriceForm.addRow(self.gamePriceLabel)

        self.gamePriceHbox = QHBoxLayout()
        self.gamePriceHbox.addStretch()
        self.gamePriceHbox.addLayout(gamePriceForm)
        self.gamePriceHbox.addStretch()

    def extraVBoxes(self):

        self.topVBox = QVBoxLayout()
        self.topVBox.addStretch()

        self.middleVBox = QVBoxLayout()
        self.middleVBox.addStretch()

        self.bottomVBox = QVBoxLayout()
        self.bottomVBox.addStretch()

    def fromGUI_IO(self, *args):
        
        try:
            title = args[0]
            price = args[1]
            platform = args[2]
        
        except IndexError:
            title = args[0]
            price = args[1]

        finally:
            self.setLabels(title, price)

    def redirect(self):
        pass
            
    def setLabels(self, *args):

        gameTitle = args[0]
        gamePrice = args[1]

        writeToCacheFile = open(self.cacheFile, 'w')

        writeToCacheFile.write('{}\n{}' .format(gameTitle, gamePrice))

        cacheLine1 = linecache.getline(self.cacheFile, 1)

        print(gameTitle, gamePrice)

        # self.initUI(cacheLine1)
        self.closeFiles(writeToCacheFile)

    def closeFiles(self, *args):
        args[0].close()

# displays error messages


def warningMessages(warning=None):

    oopsMessages = ['Oops!', 'Whoops!', 'Uh-Oh!', 'Well..', 'Hmm..']
    randNum = random.randint(0, len(oopsMessages) - 1)
    randomMessage = (oopsMessages[randNum])

    platformWarningBox = QMessageBox()
    platformWarningBox.setIcon(QMessageBox.Warning)
    platformWarningBox.setText('{} It looks like you forgot to select a platfom!' .format(randomMessage))
    platformWarningBox.setStandardButtons(QMessageBox.Retry)

    gameWarningBox = QMessageBox()
    gameWarningBox.setIcon(QMessageBox.Warning)
    gameWarningBox.setText('{} We couldn\'t gather any results\
 for that game.' .format(randomMessage))

    if (warning == 'invalidGame'):
        gameWarningBox.exec_()

    if (warning == 'invalidPlatform'):
        platformWarningBox.exec_()


def main():
    app = QApplication(sys.argv)
    mainProgram = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()