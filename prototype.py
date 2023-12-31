import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QFrame, QMainWindow, QLabel
from entryform import EntryPane
from utilities.linkedlist import LinkedList

class EntryScreen(QMainWindow):
  
  def __init__(self):
    super(EntryScreen, self).__init__()
    self.setWindowTitle("Collection Management")
    self.setGeometry(300,300,800,600)
    self.centralWidget = QWidget()
    self.layout = QtWidgets.QVBoxLayout()
    #self.layout.setSpacing(50)
    self.centralWidget.setLayout(self.layout)
    self.setCentralWidget(self.centralWidget)
    
    
    self.initUI()
    
    self.lList = LinkedList()
    print(self.lList.size)
  
    cur = self.lList.head
    
    if (self.lList.size > 0):
      while (cur.data != None):
        self.layout.addWidget(cur.data)
        cur = cur.next
    
    
    
  def initUI(self):
    #self.layout.addWidget(self.initHeadLabel())
    self.layout.addWidget(self.initCreateButton())
    

  def initHeadLabel(self):
    self.headlabel = QLabel(self)
    self.headlabel.setText("Entries")
    self.headlabel.setGeometry(QtCore.QRect(0, 0, 800, 120))
    self.headlabel.setAlignment(QtCore.Qt.AlignCenter)
    self.headlabel.setStyleSheet("background-color: rgb(7, 156, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 26pt \"MS Shell Dlg 2\";")

  def initCreateButton(self):
    self.createbutton = QtWidgets.QPushButton(self)
    self.createbutton.setGeometry(QtCore.QRect(720, 540, 40, 40))
    self.createbutton.setStyleSheet("border-radius:20px;\n" "background-color: rgb(7, 156, 255)")
    self.createbutton.setText("+")
    self.createbutton.setCheckable(True)
    self.createbutton.setAutoExclusive(False)
    self.createbutton.setObjectName("createbutton")
    self.createmenu = self.initCreateMenu()
    self.createmenu.move(690,430)
    self.createmenu.setEnabled(False)
    self.createmenu.hide()
    self.createbutton.toggled['bool'].connect(self.createmenu.setEnabled)
    self.createbutton.toggled['bool'].connect(self.createmenu.setVisible)
   
    '''
    self.entryform = QWidget(self)
    self.entryform.setGeometry(QtCore.QRect(0, 0, 611, 361))
    self.entryform.setStyleSheet("QWidget#entryform{\n""border-radius:15px;\n""background-color: rgb(226, 226, 226);\n""border:1px dotted;""}")
    self.entryform.setObjectName("entryform")
    
    return self.entryform 
    
    '''
  def initCreateMenu(self) -> QWidget:
    self.createmenu = QWidget(self)
    self.createmenu.setGeometry(QtCore.QRect(0, 0, 101, 101))
    self.createmenu.setStyleSheet("QWidget#createmenu{\n""border-radius:15px;\n""background-color: rgb(226, 226, 226);\n""border:1px dotted;""}")
    self.createmenu.setObjectName("createmenu")
    
    self.layoutwidget = QtWidgets.QWidget(self.createmenu)
    self.layoutwidget.setGeometry(QtCore.QRect(10, 10, 79, 83))
    self.layoutwidget.setObjectName("layoutWidget")
    
    self.verticallayout = QtWidgets.QVBoxLayout(self.layoutwidget)
    self.verticallayout.setContentsMargins(0, 0, 0, 0)
    self.verticallayout.setObjectName("verticalLayout")
    
    self.entrybutton = QtWidgets.QPushButton(self.layoutwidget)
    self.entrybutton.setText("New Entry")
    self.entrybutton.setCheckable(False)
    self.entrybutton.setAutoExclusive(True)
    self.entrybutton.setObjectName("entrybutton")
    self.entrybutton.clicked.connect(self.createmenu.close)
    self.entrybutton.clicked.connect(self.initEntryForm)
    self.verticallayout.addWidget(self.entrybutton)
    
    self.categorybutton = QtWidgets.QPushButton(self.layoutwidget)
    self.categorybutton.setText("New Category")
    self.categorybutton.setCheckable(False)
    self.categorybutton.setAutoExclusive(True)
    self.categorybutton.setObjectName("categorybutton")
    self.verticallayout.addWidget(self.categorybutton)
    
    self.collectionbutton = QtWidgets.QPushButton(self.layoutwidget)
    self.collectionbutton.setText("New Collection")
    self.collectionbutton.setCheckable(False)
    self.collectionbutton.setAutoExclusive(True)
    self.collectionbutton.setObjectName("collectionbutton")
    self.verticallayout.addWidget(self.collectionbutton)
    
    return self.createmenu
  
  def initEntryForm(self):
    self.entryform = EntryPane()
    self.entryform.page4.submitbutton.clicked.connect(self.addEntry)
    self.entryform.page4.submitbutton.clicked.connect(self.entryform.close)
    self.entryform.show()
    
    
  def addEntry(self):
      newEntry = self.entryform.getContents()
      self.layout.addWidget(newEntry)
      self.lList.addFirst(newEntry)
      print(self.lList.size)
      
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  entrywindow = EntryScreen()
  entrywindow.setFixedHeight(600)
  entrywindow.setFixedWidth(800)
  entrywindow.show()
 
  
  try:
    sys.exit(app.exec())
  except:
    print("Exiting")