import sys
from PyQt5 import QtWidgets as Qw
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip)
from PyQt5.QtGui import (QIcon, QFont)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('Meiryo', 12))
        self.setToolTip('Tooltip Here')

        self.btn = Qw.QPushButton('Process', self)
        self.btn.setToolTip('This is a QPushButton widget')
        self.btn.move(210, 185)
        self.btn.clicked.connect(self.setGame)

        self.quitBtn = Qw.QPushButton('Quit', self)
        self.quitBtn.clicked.connect(QApplication.instance().quit)
        self.quitBtn.move(150, 150)
        
        self.textbox = Qw.QLineEdit(self)


        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Icon")
        self.show()
    
    def setGame(self):
        gameChoice = self.textbox.text()
        
               
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Images_and_HTML/cover.jpg'))
    ex = Example()
    sys.exit(app.exec_())