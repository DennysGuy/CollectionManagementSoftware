
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QFrame, QMainWindow, QLabel

class EntryForm(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Entry Window")
    self.setObjectName("entryform")
    self.setFixedHeight(600)
    self.setFixedWidth(800)
    
    windowWidth = self.frameGeometry().width()
    windowHeight = self.frameGeometry().height()
    
    #self.setStyleSheet("QWidget#entryform{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
    self.inputwindow = QWidget(self)
    
    widthOffSet = 80
    heightOffSet = 200
    
    self.title = QLabel(self)
    self.title.setText("Identification Descriptors")
    self.title.setGeometry(QtCore.QRect(0, 0, 800, 70))
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    self.title.setStyleSheet("color: rgb(255, 255, 255);\n"
    "font: 26pt \"MS Shell Dlg 2\";")
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    self.inputwindow.setGeometry(QtCore.QRect(40, 60, windowWidth-widthOffSet, windowHeight-heightOffSet))
    self.inputwindow.setStyleSheet("QWidget#labels{background-color: rgb(255, 255, 255);" "border-radius: 15px;" "border: 1px dotted;}")
    self.inputwindow.setObjectName("labels")
    
    '''
    self.verticallayout = QtWidgets.QVBoxLayout(self.inputwindow)
    self.verticallayout.setContentsMargins(50, -500, -200, -500)
    self.verticallayout.setObjectName("verticalLayout")
    '''
    
    self.titleLabel = QLabel(self)
    self.titleLabel.setText("Title:")
    self.titleLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.titleLabel.move(int(windowWidth/8), int(windowHeight/6))
  
    self.isbnLabel = QLabel(self)
    self.isbnLabel.setText("ISBN:")
    self.isbnLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.isbnLabel.move(int(windowWidth/8), int(windowHeight/4))
    
    self.developerLabel = QLabel(self)
    self.developerLabel.setText("Dev:")
    self.developerLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.developerLabel.move(int(windowWidth/8), int(windowHeight/3))

    self.publisherLabel = QLabel(self)
    self.publisherLabel.setText("Pub:")
    self.publisherLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.publisherLabel.move(int(windowWidth/8), int(windowHeight/2.4))
    
    self.seriesLabel = QLabel(self)
    self.seriesLabel.setText("Series:")
    self.seriesLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.seriesLabel.move(int(windowWidth/8), int(windowHeight/2))
    
    self.genreLabel = QLabel(self)
    self.genreLabel.setText("Genre:")
    self.genreLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.genreLabel.move(int(windowWidth/8), int(windowHeight/1.7))
    
    self.titleInput = QtWidgets.QLineEdit(self)
    self.titleInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.titleInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.titleInput.setObjectName("titleinput")
    self.titleInput.move(int(windowWidth/8)+50, int(windowHeight/6)-5)
    
    self.isbnInput = QtWidgets.QLineEdit(self)
    self.isbnInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.isbnInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.isbnInput.setObjectName("isbninput")
    self.isbnInput.move(int(windowWidth/8)+52, int(windowHeight/4)-5)
    
    self.developerInput = QtWidgets.QLineEdit(self)
    self.developerInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.developerInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.developerInput.setObjectName("developerinput")
    self.developerInput.move(int(windowWidth/8)+50, int(windowHeight/3)-5)
    
    self.publisherInput = QtWidgets.QLineEdit(self)
    self.publisherInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.publisherInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.publisherInput.setObjectName("publisherinput")
    self.publisherInput.move(int(windowWidth/8)+50, int(windowHeight/2.4)-5)
    
    self.seriesInput = QtWidgets.QLineEdit(self)
    self.seriesInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.seriesInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.seriesInput.setObjectName("seriesinput")
    self.seriesInput.move(int(windowWidth/8)+60, int(windowHeight/2)-5)
    
    self.genreInput = QtWidgets.QLineEdit(self)
    self.genreInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.genreInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.genreInput.setObjectName("genreinput")
    self.genreInput.move(int(windowWidth/8)+60, int(windowHeight/1.7)-5)
    
    self.nextbutton = QtWidgets.QPushButton(self)
    self.nextbutton.setText("Next")
    self.nextbutton.setStyleSheet("background-color: white; font: 18pt \"MS Shell Dlg 2\"")
    self.nextbutton.setGeometry(QtCore.QRect(0,0, 100, 50))
    self.nextbutton.move(int(windowWidth/2)+50, 500)
    self.nextbutton.clicked.connect(self.goToPage2)
    
    self.backbutton = QtWidgets.QPushButton(self)
    self.backbutton.setText("Back")
    self.backbutton.setStyleSheet("background-color: white; font: 18pt \"MS Shell Dlg 2\"")
    self.backbutton.setGeometry(QtCore.QRect(0,0, 100, 50))
    self.backbutton.move(int(windowWidth/2)-150, 500)
    self.backbutton.setDisabled(True)

  def goToPage2(self):
    widget.setCurrentIndex(widget.currentIndex()+1)
  
class EntryFormPage2(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Entry Window")
    self.setObjectName("entryform2")
    self.setFixedHeight(600)
    self.setFixedWidth(800)
    
    windowWidth = self.frameGeometry().width()
    windowHeight = self.frameGeometry().height()
    
    self.setStyleSheet("QWidget#entryform{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
    self.inputwindow = QWidget(self)
    
    widthOffSet = 80
    heightOffSet = 200
    
    self.title = QLabel(self)
    self.title.setText("Dates and Prices")
    self.title.setGeometry(QtCore.QRect(0, 0, 800, 70))
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    self.title.setStyleSheet("color: rgb(255, 255, 255);\n"
    "font: 26pt \"MS Shell Dlg 2\";")
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    self.inputwindow.setGeometry(QtCore.QRect(40, 60, windowWidth-widthOffSet, windowHeight-heightOffSet))
    self.inputwindow.setStyleSheet("QWidget#labels{background-color: rgb(255, 255, 255);" "border-radius: 15px;" "border: 1px dotted;}")
    self.inputwindow.setObjectName("labels")
    
    '''
    self.verticallayout = QtWidgets.QVBoxLayout(self.inputwindow)
    self.verticallayout.setContentsMargins(50, -500, -200, -500)
    self.verticallayout.setObjectName("verticalLayout")
    '''
    
    self.titleLabel = QLabel(self)
    self.titleLabel.setText("Title:")
    self.titleLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.titleLabel.move(int(windowWidth/8), int(windowHeight/6))
  
    self.isbnLabel = QLabel(self)
    self.isbnLabel.setText("ISBN:")
    self.isbnLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.isbnLabel.move(int(windowWidth/8), int(windowHeight/4))
    
    self.developerLabel = QLabel(self)
    self.developerLabel.setText("Dev:")
    self.developerLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.developerLabel.move(int(windowWidth/8), int(windowHeight/3))

    self.publisherLabel = QLabel(self)
    self.publisherLabel.setText("Pub:")
    self.publisherLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.publisherLabel.move(int(windowWidth/8), int(windowHeight/2.4))
    
    self.seriesLabel = QLabel(self)
    self.seriesLabel.setText("Series:")
    self.seriesLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.seriesLabel.move(int(windowWidth/8), int(windowHeight/2))
    
    self.genreLabel = QLabel(self)
    self.genreLabel.setText("Genre:")
    self.genreLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.genreLabel.move(int(windowWidth/8), int(windowHeight/1.7))
    
    self.titleInput = QtWidgets.QLineEdit(self)
    self.titleInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.titleInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.titleInput.setObjectName("titleinput")
    self.titleInput.move(int(windowWidth/8)+50, int(windowHeight/6)-5)
    
    self.isbnInput = QtWidgets.QLineEdit(self)
    self.isbnInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.isbnInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.isbnInput.setObjectName("isbninput")
    self.isbnInput.move(int(windowWidth/8)+52, int(windowHeight/4)-5)
    
    self.developerInput = QtWidgets.QLineEdit(self)
    self.developerInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.developerInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.developerInput.setObjectName("developerinput")
    self.developerInput.move(int(windowWidth/8)+50, int(windowHeight/3)-5)
    
    self.publisherInput = QtWidgets.QLineEdit(self)
    self.publisherInput.setGeometry(QtCore.QRect(0,0, 500, 30))
    self.publisherInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.publisherInput.setObjectName("publisherinput")
    self.publisherInput.move(int(windowWidth/8)+50, int(windowHeight/2.4)-5)
    
    self.seriesInput = QtWidgets.QLineEdit(self)
    self.seriesInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.seriesInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.seriesInput.setObjectName("seriesinput")
    self.seriesInput.move(int(windowWidth/8)+60, int(windowHeight/2)-5)
    
    self.genreInput = QtWidgets.QLineEdit(self)
    self.genreInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.genreInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.genreInput.setObjectName("genreinput")
    self.genreInput.move(int(windowWidth/8)+60, int(windowHeight/1.7)-5)
    
    self.nextbutton = QtWidgets.QPushButton(self)
    self.nextbutton.setText("Next")
    self.nextbutton.setStyleSheet("background-color: white; font: 18pt \"MS Shell Dlg 2\"")
    self.nextbutton.setGeometry(QtCore.QRect(0,0, 100, 50))
    self.nextbutton.move(int(windowWidth/2)+50, 500)
    
    self.backbutton = QtWidgets.QPushButton(self)
    self.backbutton.setText("Back")
    self.backbutton.setStyleSheet("background-color: white; font: 18pt \"MS Shell Dlg 2\"")
    self.backbutton.setGeometry(QtCore.QRect(0,0, 100, 50))
    self.backbutton.move(int(windowWidth/2)-150, 500)
    self.backbutton.setEnabled(True)
    self.backbutton.clicked.connect(self.goBack)
    
  def goBack(self):
    widget.setCurrentIndex(widget.currentIndex()-1)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  page1 = EntryForm()
  page2 = EntryFormPage2()
  
  #entryform.show()
  widget = QStackedWidget()
  widget.setObjectName("stackedwidget")
  widget.addWidget(page1)
  widget.addWidget(page2)
  widget.setStyleSheet("QStackedWidget#stackedwidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
  widget.setFixedHeight(600)
  widget.setFixedWidth(800)
  widget.show()
  
  
  try:
    sys.exit(app.exec())
  except:
    print("Exiting")