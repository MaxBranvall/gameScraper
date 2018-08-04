import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QPushButton)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QPushButton('!')
        authorEdit = QPushButton('4')
        reviewEdit = QPushButton('5')

        # grid = QGridLayout()
        # grid.setSpacing(10)

        # grid.addWidget(titleEdit, 5, 0)
        
        # self.setLayout(grid) 
        
        self.setGeometry(300, 300, 650, 350)
        self.setWindowTitle('Review')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())