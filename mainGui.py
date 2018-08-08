# GUI of the program. User inputs will be sent to backend.py to be handled.
# Prices, titles, etc. will be recieved from backend.py ready to be displayed.

import sys, backend
from PyQt5 import QtWidgets as Qw
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QLabel, QLineEdit, QComboBox)
from PyQt5 import (QtCore, QtGui)


class Program(Qw.QWidget):

    PLATFORMS = ['Selections:', 'Xbox One', 'PlayStation 4', 'PC', 'Nintendo Switch']

    def __init__(self):

        super().__init__()

        # self.setStyleSheet("background-image: url(Images_and_HTML/bg.jpg)")
        # self.setStyleSheet("QWidget { background-color: grey }")
        # self.customSheet = 'QLabel {\
            # color: orange;\
            # background-color: blue;\
        # }'


        self.mainTitleFont = QtGui.QFont('Sans Serif', 40, 30) # Font Name, Size, Weight, Italics
        self.subTitleFont = QtGui.QFont('Sans Serif', 30, 10)

        self.resize(1, 1) # W x H
        self.center() # centers window on screen
        self.setWindowTitle('The Frugal Gamer')

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
        self.savedSearchesButton = QPushButton('Saved Searches')
        self.clearTextboxButton = QPushButton('Clear')

        self.chooseGameTextbox = QLineEdit()
        self.choosePlatformBox = QComboBox()

        # Modify and add widget functionality here

        self.welcomeTitle.setFont(self.mainTitleFont)
        self.chooseGameLabel.setFont(self.subTitleFont)
        self.choosePlatformLabel.setFont(self.subTitleFont)
        self.choosePlatformBox.addItems(self.PLATFORMS)

        self.searchButton.clicked.connect(self.printResults)
        self.clearTextboxButton.clicked.connect(self.clearTextbox)

        # Call layout methods here
        self.labelLayout()
        self.buttonAndInputLayout()
        self.extraVBoxes()

    def printResults(self):

        try:
            gameChoice = self.chooseGameTextbox.text()
            platFormChoice = self.choosePlatformBox.currentText()

            if (platFormChoice == self.PLATFORMS[0] or gameChoice == '' or ' '):
                raise ValueError
        
        except ValueError:
            # display warning message in window
            print('Error.. No platform selected')
        
        else:
            print(gameChoice, platFormChoice)
            self.chooseGameTextbox.clear()


    def clearTextbox(self):
        self.chooseGameTextbox.clear()

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

    def center(self): # Centers window on screen

        windowFrame = self.frameGeometry()
        centerOfMonitor = Qw.QDesktopWidget().availableGeometry().center()

        windowFrame.moveCenter(centerOfMonitor)
        self.move(windowFrame.topLeft())

class GUI_IO:
    
    def sendToBackend(self):

        gameChoice = self.textBox.text()
        backend.inputOutputHandling.recieveUserInput(gameChoice)

def main():
    app = Qw.QApplication(sys.argv)
    mainProgram = Program()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()