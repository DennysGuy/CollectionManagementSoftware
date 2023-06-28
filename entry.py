
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QFrame, QMainWindow, QPushButton, QLabel

class Entry(QWidget):
  def __init__(self):
    super(Entry, self).__init__()
    self.initVars()
    self.setGeometry(QtCore.QRect(300, 300, 650, 128))
    #self.setFixedWidth(550)
    #self.setFixedHeight(90)
    self.setStyleSheet("QWidget#entry{background-color: rgb(255, 255, 255);" "border: 1px dotted;}")
    self.setObjectName("entry")
    
    self.image = QtWidgets.QLabel(self)
    self.image.setGeometry(QtCore.QRect(0,0,128,128))
    self.image.setStyleSheet("border: 1px solid")
    self.image.setText("+")
    self.image.setAlignment(QtCore.Qt.AlignCenter)
    self.image.setPixmap(self.pic)
    self.image.setScaledContents(True)
    
    self.titleText = QtWidgets.QLabel(self)
    self.titleText.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\"")
    self.titleText.setText(str(self.title)) 
    self.titleText.move(135,0)
    
    self.categoryText = QtWidgets.QLabel(self)
    self.categoryText.setStyleSheet("font: 12pt \"MS Shell Dlg2\"")
    self.categoryText.setText(str(self.console))
    self.categoryText.move(135,30)
    
    self.dateAddedText = QtWidgets.QLabel(self)
    self.dateAddedText.setStyleSheet("font: 10pt \"MS Shell Dlg2\"")
    self.dateAddedText.setText("Date Added: " + str(self.dateAdded))
    self.dateAddedText.move(470, 10)
    
    self.isbnText = QtWidgets.QLabel(self)
    self.isbnText.setStyleSheet("font: 10pt \"MS Shell Dlg2\"")
    self.isbnText.setText(str(self.isbn))
    self.isbnText.move(525, 110)
    
    self.infoButton = QPushButton(self)
    self.infoButton.setGeometry(QtCore.QRect(615, 0, 35, 128))
    self.infoButton.setStyleSheet("background-color: rgb(7, 156, 255)")
    self.infoButton.setText("+")
  
  def initVars(self):
    self.title = "Mario Party"
    self.isbn = "064123000064"
    self.console = "Nintendo 64"
    self.dev  = None
    self.pub = None 
    self.series = None
    self.genre  = None 
    self.pPrice = None 
    self.pDate = None 
    self.rDate = None
    self.director = None 
    self.producer = None 
    self.programmer = None 
    self.artist = None
    self.other = None 
    self.description = None 
    self.link = None
    self.pCategory = "Nintendo 64 Games"
    #file = open(, "r")
    self.pic = QtGui.QPixmap("mario_party_cover.jpg")
    self.dateAdded = "06/27/2023"

if __name__ == '__main__':
  app = QApplication(sys.argv)
  entry = Entry()
  #entry.setFixedHeight(100)
  #entry.setFixedWidth(200)
  entry.show()
  
  try:
    sys.exit(app.exec())
  except:
    print("Exiting")
  