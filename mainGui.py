import sys
from PyQt5 import QtWidgets as Qw
from PyQt5 import (QtCore, QtGui)


class Program(Qw.QMainWindow):

    def __init__(self):

        super().__init__()

        self.resize(750, 600)
        self.setWindowTitle('Game Scraper')
        self.setStyleSheet("background-image: url(Images_and_HTML/bg.jpg)")

        self.initUI()

    def initUI(self):

        titleFont = (QtGui.QFont('Meiryo', 20))

        self.welcomeTitle = Qw.QLabel('Game Scraper', self)
        self.welcomeTitle.setFont(titleFont)
        self.welcomeTitle.adjustSize()

        self.center()
        self.show()

    def center(self):

        windowFrame = self.frameGeometry()
        centerOfMonitor = Qw.QDesktopWidget().availableGeometry().center()

        windowFrame.moveCenter(centerOfMonitor)
        self.move(windowFrame.topLeft())




if __name__ == '__main__':

    app = Qw.QApplication(sys.argv)
    mainProgram = Program()
    sys.exit(app.exec_())