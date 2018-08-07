# GUI of the program. User inputs will be sent to backend.py to be handled.
# Prices, titles, etc. will be recieved from backend.py ready to be displayed.

import sys, backend
from PyQt5 import QtWidgets as Qw
from PyQt5 import (QtCore, QtGui)


class Program(Qw.QWidget):

    def __init__(self):

        super().__init__()

        self.resize(600, 350)
        self.setWindowTitle('Game Scraper')
        # self.setStyleSheet("background-image: url(Images_and_HTML/bg.jpg)")
        self.setStyleSheet("QWidget { background-color: grey }")
        # self.customSheet = 'QLabel {\
            # color: orange;\
            # background-color: blue;\
        # }'

        self.initUI()

    def initUI(self):

        titleFont = (QtGui.QFont('Meiryo', 20))

        # self.welcomeTitle = Qw.QLabel('Game Scraper', self)
        # self.welcomeTitle.setFont(titleFont)
        # # self.welcomeTitle.setStyleSheet(self.customSheet)
        # self.welcomeTitle.adjustSize()

        self.textBox = Qw.QLineEdit(self)
        self.textBox.resize(110, 20)

        self.enter = Qw.QPushButton('Submit', self)
        self.enter.move(20, 60)
        self.enter.clicked.connect(self.sendToBackend)

        self.clear = Qw.QPushButton('Clear', self)
        self.clear.resize(40, 30)
        self.clear.move(20, 40)
        self.clear.clicked.connect(self.clearTextBox)

        # vbox = Qw.QVBoxLayout()
        # vbox.addWidget(self.enter)
        # vbox.addWidget(self.clear)
        # self.setLayout(vbox)
        
        self.center()
        self.show()

    def sendToBackend(self):

        gameChoice = self.textBox.text()
        backend.inputOutputHandling.recieveUserInput(gameChoice)

    def clearTextBox(self):
        self.textBox.clear()


    def center(self):

        windowFrame = self.frameGeometry()
        centerOfMonitor = Qw.QDesktopWidget().availableGeometry().center()

        windowFrame.moveCenter(centerOfMonitor)
        self.move(windowFrame.topLeft())




if __name__ == '__main__':

    app = Qw.QApplication(sys.argv)
    mainProgram = Program()
    sys.exit(app.exec_())