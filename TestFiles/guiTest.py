from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QMainWindow
import sys

class W1(QWidget):

    def __init__(self):
        
        super().__init__()

        self.button1 = QPushButton('test', self)
        self.button1.move(80, 80)

        self.initUI()

    def initUI(self):

        self.label = QLabel('original', self)
        self.label.move(120, 140)

        self.changeTextButton = QPushButton('Change Text', self)
        self.changeTextButton.move(100, 100)

        self.changeTextButton.clicked.connect(self.changeTextFunc)

    def changeTextFunc(self):
        testString = 'hello'

        self.label.setText('changed')
        self.update()
        

class W2(QWidget):

    def __init__(self):
        
        super().__init__()
        
        self.button2 = QPushButton('test 2', self)
        self.button2.move(60, 60)

class Main(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setGeometry(300, 300, 300, 220)

        self.openWindow1()

    def openWindow1(self):
        self.window1 = W1()
        self.setWindowTitle('window 1')
        self.setCentralWidget(self.window1)
        self.window1.button1.clicked.connect(self.openwindow2)

        self.show()
    
    def openwindow2(self):
        self.window2 = W2()
        self.setWindowTitle('window 2')
        self.setCentralWidget(self.window2)
        self.window2.button2.clicked.connect(self.openWindow1)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())