import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QPushButton)

from PyQt5 import QtWidgets as Qw
from PyQt5 import QtCore, QtGui


class Example(QWidget):

    PLATFORMS = ['Selections:' ,'Xbox One', 'PlayStation 4', 'PC', 'Nintendo Switch']
    
    def __init__(self):
        super().__init__()
        
        self.initUI()    
        
    def initUI(self):
        
        self.titleFont = QtGui.QFont('Sans Serif', 40, 30)
        self.subTitleFont = QtGui.QFont('Sans Serif', 30, 10)

        self.savedButton = Qw.QPushButton('Saved Searches')
        self.searchButton = Qw.QPushButton('Search')
        self.title = Qw.QLabel('Welcome Frugal Gamer!', self)
        self.gameLabel = Qw.QLabel('Type a Game: ')
        self.platformLabel = Qw.QLabel('Choose a Platform: ')
        self.textbox = Qw.QLineEdit()
        self.platformChoice = Qw.QComboBox()
        self.clearButton = Qw.QPushButton('Clear')

        self.title.setFont(self.titleFont)
        self.gameLabel.setFont(self.subTitleFont)
        self.platformLabel.setFont(self.subTitleFont)
        self.platformChoice.addItems(self.PLATFORMS)

        self.addTitle()

        self.mainLayout = Qw.QVBoxLayout()
        self.mainLayout.addLayout(self.hbox)
        self.mainLayout.addLayout(self.vbox2)
        self.mainLayout.addLayout(self.hbox2Game)
        self.mainLayout.addLayout(self.hboxTypeGame)
        self.mainLayout.addLayout(self.hboxPlatform)
        self.mainLayout.addLayout(self.hboxPlatformChoice)
        self.mainLayout.addLayout(self.vbox)
        self.mainLayout.addLayout(self.hboxButttons)
        
        
        

        self.setLayout(self.mainLayout)
        

        self.setGeometry(300, 300, 1, 1)
        self.setWindowTitle('Review')    
        self.show()
    
    def addTitle(self):

        self.vbox2 = Qw.QVBoxLayout()
        self.vbox2.addStretch()

        self.hbox = Qw.QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.title)
        self.hbox.addStretch()

        self.vbox = Qw.QVBoxLayout()
        self.vbox.addStretch()

        self.formLayoutGame = Qw.QFormLayout()
        self.formLayoutGame.addRow(self.gameLabel)

        self.hbox2Game = Qw.QHBoxLayout()
        self.hbox2Game.addStretch()
        self.hbox2Game.addLayout(self.formLayoutGame)
        self.hbox2Game.addStretch()

        self.typeGameForm = Qw.QFormLayout()
        self.typeGameForm.addRow(self.textbox)

        self.hboxTypeGame = Qw.QHBoxLayout()
        self.hboxTypeGame.addStretch(3)
        self.hboxTypeGame.addLayout(self.typeGameForm)
        self.hboxTypeGame.addWidget(self.clearButton)
        self.hboxTypeGame.addStretch(3)
        
       

        self.platformForm = Qw.QFormLayout()
        self.platformForm.addRow(self.platformLabel)

        self.hboxPlatform = Qw.QHBoxLayout()
        self.hboxPlatform.addStretch()
        self.hboxPlatform.addLayout(self.platformForm)
        self.hboxPlatform.addStretch()

        self.platformChoiceForm = Qw.QFormLayout()
        self.platformChoiceForm.addRow(self.platformChoice)

        self.hboxPlatformChoice = Qw.QHBoxLayout()
        self.hboxPlatformChoice.addStretch()
        self.hboxPlatformChoice.addLayout(self.platformChoiceForm)
        self.hboxPlatformChoice.addStretch()

        # self.buttonsForm = Qw.QFormLayout()
        # self.buttonsForm.addRow(self.savedButton, self.searchButton)

        self.hboxButttons = Qw.QHBoxLayout()
        self.hboxButttons.addWidget(self.savedButton)
        self.hboxButttons.addStretch()
        self.hboxButttons.addWidget(self.searchButton)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())