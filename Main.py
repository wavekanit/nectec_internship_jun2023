import sys
import time
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QTimer
from HomePage import Home_Page
from NewTest import New_Test
from StartAnalysis import Start_Analysis
from PastResult import Past_Results
fld_path_doc = "/Users/kanitbunyinkgool/Desktop/NECTEC/Project/raspberrypi-qt/version4/document"

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.setGeometry(0, 0, 800, 480)
        self.setMinimumSize(800, 480)
        self.setMaximumSize(800, 480)
        self.stacked_widget.setStyleSheet("background-color:#FFF1FE;")
        self.setWindowTitle("MycoSMARTReader")
        
        self.homePageBtn = QPushButton(self)
        self.homePageBtn.setGeometry(35, 25, 235, 45)
        self.homePageBtn.setStyleSheet('''
                                       background-color:#E8DAFF;
                                       color: #485C5A;
                                       border-radius: 22px; 
                                       color: #485C5A;
                                       font-family: 'Mada', serif;
                                       font-size: 20px;
                                       font-weight: 700;
                                       ''')
        
        self.returnLabelbtn = QLabel("Return",self)
        self.returnLabelbtn.setGeometry(110, 37, 61, 20)
        self.returnLabelbtn.setStyleSheet('''background-color:rgba(255,255,255,0); color: #485C5A; font-size: 20px; font-family: 'Mada', serif; font-weight: 700;''')

        self.homeLebelbtn = QLabel("Home",self)   
        self.homeLebelbtn.setGeometry(180,37,61,20) 
        self.homeLebelbtn.setStyleSheet('''background-color:rgba(255,255,255,0); color: #6646D9; font-size: 20px; font-family: 'Mada', serif; font-weight: 700;''')

        self.homeIcon = QLabel(self)
        self.homeIcon.setGeometry(62, 33, 29, 29)
        self.homeIcon.setStyleSheet("background-color: rgba(255,255,255,0);")
        self.homeIcon.setPixmap(self.insertPhoto(34 , 34,f'{fld_path_doc}/{"homepage.png"}'))
        self.homePageBtn.clicked.connect(self.goHomePage)
        
        homePage = Home_Page()
        homePage.newTestBtn.clicked.connect(self.goNewTest)
        homePage.pastResultsIcon.setPixmap(self.insertPhoto(30 , 30,f'{fld_path_doc}/{"pastresult.png"}'))
        homePage.settingIcon.setPixmap(self.insertPhoto(30 , 30,f'{fld_path_doc}/{"disruption.png"}'))
        homePage.calirationIcon.setPixmap(self.insertPhoto(26 , 26,f'{fld_path_doc}/{"calibration.png"}'))
        homePage.pastResultsBtn.clicked.connect(self.goPastResults)
        
        self.stacked_widget.addWidget(homePage)
        
        newTest = New_Test()
        newTest.startAnalysisBtn.clicked.connect(self.goStartAnalysis)
        self.stacked_widget.addWidget(newTest)
        
        self.startAnalysis = Start_Analysis()
        self.startAnalysis.canclebtn.clicked.connect(self.goNewTest)
        self.startAnalysis.canclebtn.clicked.connect(self.cancleTest)
        self.stacked_widget.addWidget(self.startAnalysis)
        
        pastResults = Past_Results()
        self.stacked_widget.addWidget(pastResults)
        
        self.timeLebel = QLabel(self)
        self.timeLebel.setGeometry(532, 25, 236, 45)
        self.timeLebel.setStyleSheet('''
                                     background-color:#E8DAFF;
                                     border-radius: 22px; 
                                     color: #512BBD; 
                                     font-size: 20px;
                                     font-family: 'Mada', serif;
                                     font-weight: 700;
                                     ''')
        self.timeIcon = QLabel(self)
        self.timeIcon.setGeometry(544, 32, 30, 30)
        self.timeIcon.setStyleSheet("background-color: rgba(255,255,255,0);")
        self.timeIcon.setPixmap(self.insertPhoto(30 , 30,f'{fld_path_doc}/{"clock.png"}'))

        self.stacked_widget.setCurrentIndex(0)
        
        # Create a QTimer to update the time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1)  # Update every 1000 milliseconds (1 second)

    def insertPhoto(self, width, height, path):
        photo_pixmap = QPixmap(path)
        photo_pixmap = photo_pixmap.scaledToWidth(width)
        photo_pixmap = photo_pixmap.scaledToHeight(height)
        return photo_pixmap
    
    def goNewTest(self):
        self.stacked_widget.setCurrentIndex(1)
        # self.updateTime()

    def cancleTest(self):
        if self.startAnalysis.progress != 0:
            self.startAnalysis.stopAnimation()
            self.startAnalysis.progress = 0
        
    def goHomePage(self):
        self.stacked_widget.setCurrentIndex(0)
        
    def goStartAnalysis(self):
        self.stacked_widget.setCurrentIndex(2)
        if self.stacked_widget.currentIndex() == 2:
            self.startAnalysis.startAnimation()
    
    def goPastResults(self):
        self.stacked_widget.setCurrentIndex(3)
        
    def updateTime(self):
        time_tuple = time.localtime()
        local_time = time.strftime("             %H:%M | %d %b %Y", time_tuple)
        self.timeLebel.setText(local_time)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    iconPath = os.path.join(os.path.dirname(sys.modules[__name__].__file__), f'{fld_path_doc}/{"allergies.png"}')
    app.setWindowIcon(QIcon(iconPath))
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
