import sys
from PyQt5 import QtWidgets as Qw


class Program(Qw.QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

        self.resize(750, 650)
        self.setWindowTitle('Game Scraper')

        self.center()
        self.show()

    def initUI(self):
        pass

    def center(self):

        windowFrame = self.frameGeometry()
        centerOfMonitor = Qw.QDesktopWidget().availableGeometry().center()

        windowFrame.moveCenter(centerOfMonitor)
        self.move(windowFrame.topLeft())


if __name__ == '__main__':

    app = Qw.QApplication(sys.argv)
    mainProgram = Program()
    sys.exit(app.exec_())