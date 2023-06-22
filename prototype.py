import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QFrame, QMainWindow, QLabel


class EntryScreen(QMainWindow):
  
  def __init__(self):
    super(EntryScreen, self).__init__()
    self.setWindowTitle("Collection Management")
    self.setGeometry(300,300,800,600)
    self.initUI()
  
  def initUI(self):
    self.headlabel = QLabel(self)
    self.headlabel.setText("Entries")
    #self.headlabel.move(int(800/2), 0)
    self.headlabel.setGeometry(QtCore.QRect(0, 0, 801, 121))
    self.headlabel.setAlignment(QtCore.Qt.AlignCenter)
    self.headlabel.setStyleSheet("background-color: rgb(7, 156, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 26pt \"MS Shell Dlg 2\";")
    self.createbutton = QtWidgets.QPushButton(self)
    self.createbutton.setGeometry(QtCore.QRect(720, 440, 41, 41))
    self.createbutton.setStyleSheet("border-radius:20px;\n"
                                "background-color: rgb(7, 156, 255)")
    
    self.createbutton.setCheckable(True)
    self.createbutton.setAutoExclusive(False)
    self.createbutton.setObjectName("createmenu")  
  
    
    #self.headlabel.adjustSize()
    
  
    
class CreationScreen(QWidget):
  
  def __init__(self):
    super(CreationScreen, self).__init__()
    loadUi("creationwindow.ui", self)
  

    

if __name__ == '__main__':
  app = QApplication(sys.argv)
  entrywindow = EntryScreen()
  entrywindow.show()
  
  try:
    sys.exit(app.exec())
  except:
    print("Exiting")
  