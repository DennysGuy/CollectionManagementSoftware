
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget, QFrame, QMainWindow, QLabel

class IdentificationForm(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Entry Window")
    self.setObjectName("identifcationform")
    self.setFixedHeight(600)
    self.setFixedWidth(800)
    
    windowWidth = self.frameGeometry().width()
    windowHeight = self.frameGeometry().height()
    
    #self.setStyleSheet("QWidget#identification{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
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
    
    self.consoleLabel = QLabel(self)
    self.consoleLabel.setText("Console:")
    self.consoleLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"")
    self.consoleLabel.move(int(windowWidth/8), int(windowHeight/3))
    
    self.developerLabel = QLabel(self)
    self.developerLabel.setText("Dev:")
    self.developerLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.developerLabel.move(int(windowWidth/8), int(windowHeight/2.4))

    self.publisherLabel = QLabel(self)
    self.publisherLabel.setText("Pub:")
    self.publisherLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.publisherLabel.move(int(windowWidth/8), int(windowHeight/2))
    
    self.seriesLabel = QLabel(self)
    self.seriesLabel.setText("Series:")
    self.seriesLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.seriesLabel.move(int(windowWidth/8), int(windowHeight/1.7))
    
    self.genreLabel = QLabel(self)
    self.genreLabel.setText("Genre:")
    self.genreLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.genreLabel.move(int(windowWidth/8), int(windowHeight/1.5))
    
    self.titleInput = QtWidgets.QLineEdit(self)
    self.titleInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.titleInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.titleInput.setObjectName("titleinput")
    self.titleInput.move(int(windowWidth/8)+70, int(windowHeight/6)-5)
    
    self.isbnInput = QtWidgets.QLineEdit(self)
    self.isbnInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.isbnInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.isbnInput.setObjectName("isbninput")
    self.isbnInput.move(int(windowWidth/8)+70, int(windowHeight/4)-5)
    
    self.consoleInput = QtWidgets.QLineEdit(self)
    self.consoleInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.consoleInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.consoleInput.setObjectName("developerinput")
    self.consoleInput.move(int(windowWidth/8)+70, int(windowHeight/3)-5)
    
    
    self.developerInput = QtWidgets.QLineEdit(self)
    self.developerInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.developerInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.developerInput.setObjectName("developerinput")
    self.developerInput.move(int(windowWidth/8)+70, int(windowHeight/2.4)-5)
    
    self.publisherInput = QtWidgets.QLineEdit(self)
    self.publisherInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.publisherInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.publisherInput.setObjectName("publisherinput")
    self.publisherInput.move(int(windowWidth/8)+70, int(windowHeight/2)-5)
    
    self.seriesInput = QtWidgets.QLineEdit(self)
    self.seriesInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.seriesInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.seriesInput.setObjectName("seriesinput")
    self.seriesInput.move(int(windowWidth/8)+70, int(windowHeight/1.7)-5)
    
    self.genreInput = QtWidgets.QLineEdit(self)
    self.genreInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.genreInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.genreInput.setObjectName("genreinput")
    self.genreInput.move(int(windowWidth/8)+70, int(windowHeight/1.5)-5)
    
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
    self.backbutton.setDisabled(True)
  
class PricesDatesForm(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Entry Window")
    self.setObjectName("pricesdatesform")
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
    
    self.pruchasePriceLabel = QLabel(self)
    self.pruchasePriceLabel.setText("Purchase Price:")
    self.pruchasePriceLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.pruchasePriceLabel.move(int(windowWidth/8), int(windowHeight/6))
  
    self.purchaseDateLabel = QLabel(self)
    self.purchaseDateLabel.setText("Purchase Date:")
    self.purchaseDateLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.purchaseDateLabel.move(int(windowWidth/8), int(windowHeight/3))
    
    self.releaseDateLabel = QLabel(self)
    self.releaseDateLabel.setText("Release Date(s):")
    self.releaseDateLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.releaseDateLabel.move(int(windowWidth/8), int(windowHeight/2))

    
    self.pruchasePriceInput = QtWidgets.QLineEdit(self)
    self.pruchasePriceInput.setGeometry(QtCore.QRect(0,0, 430, 30))
    self.pruchasePriceInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.pruchasePriceInput.setObjectName("purchasepriceinput")
    self.pruchasePriceInput.move(int(windowWidth/8)+170, int(windowHeight/6)-5)
    
    self.releaseDateInput = QtWidgets.QLineEdit(self)
    self.releaseDateInput.setGeometry(QtCore.QRect(0,0, 430, 30))
    self.releaseDateInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.releaseDateInput.setObjectName("releasedateinput")
    self.releaseDateInput.move(int(windowWidth/8)+170, int(windowHeight/3)-5)
    
    self.developerInput = QtWidgets.QLineEdit(self)
    self.developerInput.setGeometry(QtCore.QRect(0,0, 430, 30))
    self.developerInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.developerInput.setObjectName("developerinput")
    self.developerInput.move(int(windowWidth/8)+170, int(windowHeight/2)-5)
  
    
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
  
class ContributorsForm(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Entry Window")
    self.setObjectName("contributorsform")
    self.setFixedHeight(600)
    self.setFixedWidth(800)
    
    windowWidth = self.frameGeometry().width()
    windowHeight = self.frameGeometry().height()
    
    self.setStyleSheet("QWidget#entryform{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
    self.inputwindow = QWidget(self)
    
    widthOffSet = 80
    heightOffSet = 200
    
    self.title = QLabel(self)
    self.title.setText("Contributors")
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
    
    self.directorLabel = QLabel(self)
    self.directorLabel.setText("Director(s):")
    self.directorLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.directorLabel.move(int(windowWidth/8), int(windowHeight/6))
  
    self.producerLabel = QLabel(self)
    self.producerLabel.setText("Producer(s):")
    self.producerLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.producerLabel.move(int(windowWidth/8), int(windowHeight/4))
    
    self.composerLabel = QLabel(self)
    self.composerLabel.setText("Composer(s):")
    self.composerLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.composerLabel.move(int(windowWidth/8), int(windowHeight/3))

    self.programmerLabel = QLabel(self)
    self.programmerLabel.setText("Programmer(s):")
    self.programmerLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.programmerLabel.move(int(windowWidth/8), int(windowHeight/2.4))
    
    self.artistLabel = QLabel(self)
    self.artistLabel.setText("Artist(s):")
    self.artistLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.artistLabel.move(int(windowWidth/8), int(windowHeight/2))
    
    self.otherLabel = QLabel(self)
    self.otherLabel.setText("Other:")
    self.otherLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.otherLabel.move(int(windowWidth/8), int(windowHeight/1.7))
    
    self.directorInput = QtWidgets.QLineEdit(self)
    self.directorInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.directorInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.directorInput.setObjectName("directorinput")
    self.directorInput.move(int(windowWidth/8)+160, int(windowHeight/6)-5)
    
    self.producerInput = QtWidgets.QLineEdit(self)
    self.producerInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.producerInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.producerInput.setObjectName("producerinput")
    self.producerInput.move(int(windowWidth/8)+160, int(windowHeight/4)-5)
    
    self.composerInput = QtWidgets.QLineEdit(self)
    self.composerInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.composerInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.composerInput.setObjectName("composerinput")
    self.composerInput.move(int(windowWidth/8)+160, int(windowHeight/3)-5)
    
    self.publisherInput = QtWidgets.QLineEdit(self)
    self.publisherInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.publisherInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.publisherInput.setObjectName("publisherinput")
    self.publisherInput.move(int(windowWidth/8)+160, int(windowHeight/2.4)-5)
    
    self.artistInput = QtWidgets.QLineEdit(self)
    self.artistInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.artistInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.artistInput.setObjectName("artistinput")
    self.artistInput.move(int(windowWidth/8)+160, int(windowHeight/2)-5)
    
    self.otherInput = QtWidgets.QLineEdit(self)
    self.otherInput.setGeometry(QtCore.QRect(0,0, 490, 30))
    self.otherInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.otherInput.setObjectName("otherinput")
    self.otherInput.move(int(windowWidth/8)+160, int(windowHeight/1.7)-5)
    
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

class DescriptionLinksForm(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("Entry Window")
    self.setObjectName("descriptionlinksform")
    self.setFixedHeight(600)
    self.setFixedWidth(800)
    
    windowWidth = self.frameGeometry().width()
    windowHeight = self.frameGeometry().height()
    
    self.setStyleSheet("QWidget#entryform{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
    self.inputwindow = QWidget(self)
    
    widthOffSet = 80
    heightOffSet = 200
    
    self.title = QLabel(self)
    self.title.setText("Description and Links")
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
    
    self.descriptionLabel = QLabel(self)
    self.descriptionLabel.setText("Description:")
    self.descriptionLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.descriptionLabel.move(int(windowWidth/8), int(windowHeight/6))
  
    
    self.linkLabel = QLabel(self)
    self.linkLabel.setText("Link(s):")
    self.linkLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
    self.linkLabel.move(int(windowWidth/8), int(windowHeight/2))

    
    self.descriptionInput = QtWidgets.QLineEdit(self)
    self.descriptionInput.setGeometry(QtCore.QRect(0,0, 430, 30))
    self.descriptionInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.descriptionInput.setObjectName("descriptioninput")
    self.descriptionInput.move(int(windowWidth/8)+170, int(windowHeight/6)-5)
       
    self.linkInput = QtWidgets.QLineEdit(self)
    self.linkInput.setGeometry(QtCore.QRect(0,0, 430, 30))
    self.linkInput.setStyleSheet("font: 14px \"MS Shell Dlg 2\"")
    self.linkInput.setObjectName("linkinput")
    self.linkInput.move(int(windowWidth/8)+170, int(windowHeight/2)-5)
  
    
    self.submitbutton = QtWidgets.QPushButton(self)
    self.submitbutton.setText("Submit")
    self.submitbutton.setStyleSheet("background-color: white; font: 18pt \"MS Shell Dlg 2\"")
    self.submitbutton.setGeometry(QtCore.QRect(0,0, 105, 55))
    self.submitbutton.move(int(windowWidth/2)+50, 500)
    
    self.backbutton = QtWidgets.QPushButton(self)
    self.backbutton.setText("Back")
    self.backbutton.setStyleSheet("background-color: white; font: 18pt \"MS Shell Dlg 2\"")
    self.backbutton.setGeometry(QtCore.QRect(0,0, 100, 50))
    self.backbutton.move(int(windowWidth/2)-150, 500)
    self.backbutton.setEnabled(True)
    
class EntryPane(QWidget):
    def __init__(self):
      super().__init__()
      self.page1 = IdentificationForm()
      self.page2 = PricesDatesForm()
      self.page3 = ContributorsForm()
      self.page4 = DescriptionLinksForm()
      
      self.widget = QStackedWidget(self)
      self.widget.setObjectName("stackedwidget")
  
      self.widget.addWidget(self.page1)
      self.widget.addWidget(self.page2)
      self.widget.addWidget(self.page3)
      self.widget.addWidget(self.page4)
      self.widget.setStyleSheet("QStackedWidget#stackedwidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
      self.widget.setFixedHeight(600)
      self.widget.setFixedWidth(800)

      #page 1 button setup
      self.page1.nextbutton.clicked.connect(self.goToNextPage)
      #page 2 button setup
      self.page2.nextbutton.clicked.connect(self.goToNextPage)
      self.page2.backbutton.clicked.connect(self.goToPreviousPage)
      #page 3 button setup
      self.page3.nextbutton.clicked.connect(self.goToNextPage)
      self.page3.backbutton.clicked.connect(self.goToPreviousPage)
      #page 4 button setup
      self.page4.submitbutton.clicked.connect(self.goToNextPage)
      self.page4.backbutton.clicked.connect(self.goToPreviousPage)
    
    def goToNextPage(self):
      self.widget.setCurrentIndex(self.widget.currentIndex()+1)
      
    def goToPreviousPage(self):
      self.widget.setCurrentIndex(self.widget.currentIndex()-1)

def next():
  widget.setCurrentIndex(widget.currentIndex()+1)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  page1 = IdentificationForm()
  page2 = PricesDatesForm()
    
  widget = QStackedWidget()
  widget.setObjectName("stackedwidget")
  widget.addWidget(page1)
  widget.addWidget(page2)
  widget.setStyleSheet("QStackedWidget#stackedwidget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.948864, y2:1, stop:0 rgba(72, 113, 139, 255), stop:1 rgba(255, 255, 255, 255));}")
  
  page1.nextbutton.clicked.connect(next)
  widget.setFixedHeight(600)
  widget.setFixedWidth(800)
  widget.show()
    
  try:
    sys.exit(app.exec())
  except:
    print("Exiting")

