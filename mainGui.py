# GUI of the program. User inputs will be sent to backend.py to be handled.
# Prices, titles, etc. will be recieved from backend.py ready to be displayed.

#TODO WARNING light grey/default background is bugged and doesn't clear textbox and combo box properly..

import sys, backend, random
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton,
                            QLabel, QLineEdit, QComboBox, QMainWindow, 
                            QWidget, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont

# This class will handle all input and output for the GUI
class GUI_IO:

    def sendToBackend(game, platform):
        
        backend.BACKEND_IO.inputFromGUI(game, platform)

    def fromBackend(title, price):

        gameTitle = title
        gamePrice = price

        print(gameTitle, gamePrice)

# The frame and main window.
class Frame(QMainWindow):

    def __init__(self):
        
        super().__init__()
        
        self.mainWindow = Program()
        # other windows will go here
        self.setCentralWidget(self.mainWindow)

        self.initUI()

    def initUI(self):

        self.setStyleSheet("QMainWindow {background-image: url(Images_and_HTML/carbonBG.jpg)}")

        self.resize(600, 400)
        self.center()
        
        self.setWindowTitle('The Frugal Gamer')

        self.show()

    def center(self): # Centers window on screen

        windowFrame = self.frameGeometry()
        centerOfMonitor = QDesktopWidget().availableGeometry().center()

        windowFrame.moveCenter(centerOfMonitor)
        self.move(windowFrame.topLeft())

# holds all widgets
class Program(QWidget):

    PLATFORMS = ['Selections:', 'Xbox One', 'PlayStation 4', 'PC', 'Nintendo Switch']

    def __init__(self):

        super().__init__()

        self.mainFontColor = 'color: #d3d3d3' # Light grey font color

        self.mainTitleFont = QFont('Sans Serif', 40, 30) # Font Name, Size, Weight, Italics
        self.subTitleFont = QFont('Sans Serif', 30, 10)

        self.initUI()
        self.show()

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

        self.savedSearchesButton.disconnect()

        # Call layout methods here
        self.labelLayout()
        self.buttonAndInputLayout()
        self.extraVBoxes()

    # Functionality Methods

    def clearTextbox(self):
        self.chooseGameTextbox.clear()

    def statusBarHandling(self, message= None):

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
        self.bottomVBox.addStretch()

    # Sends choices to GUI_IO 

    def resultsToGUI_IO(self):

        try:
            gameChoice = self.chooseGameTextbox.text()
            platFormChoice = self.choosePlatformBox.currentText()

            if (platFormChoice == self.PLATFORMS[0]):
                raise ValueError
        
        except ValueError:
            # display warning message in window
            warningMessages(warning= 'invalidPlatform')
        
        else:
            GUI_IO.sendToBackend(gameChoice, platFormChoice)
            self.chooseGameTextbox.clear()

class PriceandTitleScreen(QWidget):

    def __init__(self):
        
        super().__init__()

        self.initUI()
        self.show()

    def initUI(self):
        
        self.gameTitleLabel = QLabel()

# displays error messages

def warningMessages(warning= None):

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
    mainProgram = Frame()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()