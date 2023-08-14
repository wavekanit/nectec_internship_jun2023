#Homepage

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QColor

class Home_Page(QWidget):
    def __init__(self):
        super().__init__()
        
        self.newTestBtn = QPushButton("NEW\nTEST", self)
        self.newTestBtn.setGeometry(496, 147, 236, 236)
        self.newTestBtn.setGraphicsEffect(self.shadow())
        self.newTestBtn.setStyleSheet('''background-color: #39174A;
                                      border-radius: 118px; 
                                      color: #F2F0F5;
                                      font-size: 47px; font-family: 'Mada', serif; 
                                      font-weight: 700;''')
        
                
        self.headLebel = QLabel("MycoSMART\nReader", self)
        self.headLebel.setGeometry(48, 94, 360, 140)
        self.headLebel.setStyleSheet('''color: #403042;
                                     font-size: 50px; 
                                     font-family: Mada; 
                                     font-weight: 700; 
                                     ''')
       
        self.pastResultsBtn = QPushButton("     Past Results", self)
        self.pastResultsBtn.setGeometry(117, 241, 260, 45)
        self.pastResultsBtn.setStyleSheet('''
                                          background-color:#F0D8FF;
                                          border-radius: 19px; 
                                          color: #4F0C59; 
                                          font-size: 24px;
                                          font-weight: 700;
                                          ''')
        self.pastResultsIcon = QLabel(self)
        self.pastResultsIcon.setGeometry(142, 249, 30, 30)
        self.pastResultsIcon.setStyleSheet("background-color:rgba(255,255,255,0);")
        
        self.settingBtn = QPushButton("  Setting", self)
        self.settingBtn.setGeometry(115, 320, 260, 45)
        self.settingBtn.setStyleSheet('''
                                      background-color:#F0D8FF;
                                      border-radius: 19px; 
                                      color: #4F0C59;
                                      font-size: 24px;
                                      font-weight: 700;
                                      ''')
        self.settingIcon = QLabel(self)
        self.settingIcon.setGeometry(137, 328, 30, 30)
        self.settingIcon.setStyleSheet("background-color:rgba(255,255,255,0);")
        
        self.calirationBth = QPushButton("     Calibration Curves", self)
        self.calirationBth.setGeometry(121, 402, 270, 45)
        self.calirationBth.setStyleSheet('''background-color:#F0D8FF; 
                                         border-radius:19px;
                                         color: #4F0C59;
                                         font-size: 22px;
                                         font-weight: 700;''')
        self.calirationIcon = QLabel(self)
        self.calirationIcon.setGeometry(133, 411, 26, 26)
        self.calirationIcon.setStyleSheet("background-color:rgba(255,255,255,0);")
        

    def shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)  # Adjust the blur radius as needed
        shadow.setColor(QColor(199, 178, 146, 255))
        shadow.setOffset(12, 12)
        return shadow
    