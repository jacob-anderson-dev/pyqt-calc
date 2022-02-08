import sys
from PyQt5 import QtCore, QtWidgets, uic

#Load ui file
Form, _ = uic.loadUiType('calcMainWindow.ui')

#Create MainWindow class
class MainWindow(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Setup ui file in the MainWindow
        self.setupUi(self)

        #Connect all buttons to respective functions
        self.buttonEQL.clicked.connect(self.action_equal)
        self.buttonPLS.clicked.connect(lambda: self.action_change(" + "))
        self.buttonMIN.clicked.connect(lambda: self.action_change(" - "))
        self.buttonDIV.clicked.connect(lambda: self.action_change(" / "))
        self.buttonMLT.clicked.connect(lambda: self.action_change(" * "))
        self.buttonDEC.clicked.connect(lambda: self.action_change("."))
        self.button0.clicked.connect(lambda: self.action_change("0"))
        self.button1.clicked.connect(lambda: self.action_change("1"))
        self.button2.clicked.connect(lambda: self.action_change("2"))
        self.button3.clicked.connect(lambda: self.action_change("3"))
        self.button4.clicked.connect(lambda: self.action_change("4"))
        self.button5.clicked.connect(lambda: self.action_change("5"))
        self.button6.clicked.connect(lambda: self.action_change("6"))
        self.button7.clicked.connect(lambda: self.action_change("7"))
        self.button8.clicked.connect(lambda: self.action_change("8"))
        self.button9.clicked.connect(lambda: self.action_change("9"))
        self.buttonCLR.clicked.connect(self.action_clear)
        self.buttonLPR.clicked.connect(lambda: self.action_change("("))
        self.buttonRPR.clicked.connect(lambda: self.action_change(")"))
        self.buttonDEL.clicked.connect(self.action_del)

    #Define equal button function
    def action_equal(self):
        equation = self.answer.text()  
        try:
            ans = eval(equation)
            self.answer.setText(str(ans))
        except:
            self.answer.setText("Wrong Input")

    #Define general button function
    def action_change(self, value):
        text = self.answer.text()
        self.answer.setText(text + value)  

    #Define clear button function
    def action_clear(self):
        self.answer.setText("")
  
    #Define delete button function
    def action_del(self):
        text = self.answer.text()
        self.answer.setText(text[:len(text)-1])

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
