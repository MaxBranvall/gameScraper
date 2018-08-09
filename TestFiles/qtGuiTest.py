import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QPushButton, QMainWindow)

from PyQt5 import QtWidgets as Qw
from PyQt5 import QtCore, QtGui


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.show() 

        mainlayout = Qw.QVBoxLayout()
        mainlayout.addLayout(self.hbox)

        self.setLayout(mainlayout)
        
    def initUI(self):
        self.statusBar().showMessage('hello')

        self.button = QPushButton('hello button', self)

        self.lay()

    def lay(self):

        self.hbox = Qw.QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.button)

        
       
if __name__ == '__main__':
    
    app = QApplication(sys.argv) #TODO move these lines to a main function and call that function here
    ex = Example()
    sys.exit(app.exec_())