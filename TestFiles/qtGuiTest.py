# GUI of the program. User inputs will be sent to backend.py to be handled.
# Prices, titles, etc. will be recieved from backend.py ready to be displayed.

#TODO WARNING light grey/default background is bugged and doesn't clear textbox and combo box properly..

import sys, random
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton,
                            QLabel, QLineEdit, QComboBox, QMainWindow, 
                            QWidget, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("QMainWindow {background-image: url(Images_and_HTML/bg.jpg)}")

        self.mainWidget = Program()
        self.setCentralWidget(self.mainWidget)

        self.init_UI()

    def init_UI(self):
        self.resize(600, 400)
        self.center()
        self.setWindowTitle('Central Widget')
        self.show()

    def center(self): # Centers window on screen

        windowFrame = self.frameGeometry()
        centerOfMonitor = QDesktopWidget().availableGeometry().center()

        windowFrame.moveCenter(centerOfMonitor)
        self.move(windowFrame.topLeft())

class Program(QWidget):

    def __init__(self):

        super().__init__()

        self.mainTitleFont = QFont('Sans Serif', 40, 30) # Font Name, Size, Weight, Italics
        self.subTitleFont = QFont('Sans Serif', 30, 10)

        self.initUI()
        self.show()

        mainScreenLayout = QVBoxLayout()
        mainScreenLayout.addLayout(self.ratingHbox)
        mainScreenLayout.addLayout(self.gameTitlehbox)
        mainScreenLayout.addLayout(self.priceHbox)
        mainScreenLayout.addLayout(self.emptyVbox)

        self.setLayout(mainScreenLayout)

    def initUI(self):
        
        self.gameTitleLabel = QLabel('Game label will go here')
        self.gameTitleLabel.setFont(self.mainTitleFont)
        self.listPriceLabel = QLabel('List Price:')
        self.listPriceLabel.setFont(self.subTitleFont)
        self.priceLabel = QLabel('$29.99')
        self.priceLabel.setFont(self.subTitleFont)

        self.rating = QLabel('Rating here')

        self.labelLayout()

    def labelLayout(self):

        gameLabelForm = QFormLayout()
        gameLabelForm.addRow(self.gameTitleLabel)

        self.gameTitlehbox = QHBoxLayout()
        self.gameTitlehbox.addStretch()
        self.gameTitlehbox.addLayout(gameLabelForm)
        self.gameTitlehbox.addStretch()

        self.ratingHbox = QHBoxLayout()
        self.ratingHbox.addStretch(3)
        self.ratingHbox.addWidget(self.rating)

        priceLabelForm = QFormLayout()
        priceLabelForm.addRow(self.listPriceLabel)
        priceLabelForm.addRow(self.priceLabel)

        self.priceHbox = QHBoxLayout()
        self.priceHbox.addStretch()
        self.priceHbox.addLayout(priceLabelForm)
        self.priceHbox.addStretch()
        

        self.emptyVbox = QVBoxLayout()
        self.emptyVbox.addStretch(3)


def main():
    app = QApplication(sys.argv)
    mainProgram = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()