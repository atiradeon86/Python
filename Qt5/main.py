from PyQt5 import QtWidgets, uic
import sys
import random
import webbrowser

class Ui(QtWidgets.QFrame):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

        #Find Button, Input element on QFrane
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.inp = self.findChild(QtWidgets.QLineEdit, 'lineEdit')

        #Call Function
        self.button.clicked.connect(self.bryan)    

    def bryan(self):
        text = self.inp.text() 
        url= 'https://github.com/atiradeon86'
        if text !="":
            url = text
        chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

Ui.show

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()