from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import time

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teatimer")
        self.setGeometry(1500, 500, 200, 100)
        self.grid = QGridLayout()
        self.initUI()  
        self.show()

    def initUI(self):
        self.setLayout(self.grid)

        self.b1 = QPushButton("2", self)
        self.b2 = QPushButton("3", self)
        self.b3 = QPushButton("4", self)
        self.b4 = QPushButton("5", self)
        
        self.grid.addWidget(self.b1, 1, 1)
        self.grid.addWidget(self.b2, 1, 2)
        self.grid.addWidget(self.b3, 2, 1)
        self.grid.addWidget(self.b4, 2, 2)
        self.grid.addWidget(self.label, 3, 1 )

    def start(self):
        t = 5
        while t >= 0:
            print(t)
            t -= 1
            time.sleep(1)
        exit()

if __name__ == "__main__":
    # create pyqt5 app
    app = QApplication(sys.argv)
    
    # create the instance of our Window
    window = Window()
    
    # start the app
    sys.exit(app.exec())





