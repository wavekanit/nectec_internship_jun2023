#Past_Results Page
#เชื่อมให้ทีน้องพลอยงงงงงงงงงงงงง
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGraphicsDropShadowEffect, QComboBox, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QPixmap, QColor

class Past_Results(QWidget):
    def __init__(self):
        super().__init__()
                
        self.headLebel = QLabel("Results", self)
        self.headLebel.setGeometry(163, 60, 188, 60)
        self.headLebel.setStyleSheet("background-color: rgba(255,255,255,0); color: #5B3985; font-size: 40px; font-family: 'Mada', serif; font-weight: 700;")
        
        self.homeTabBarLabel = QLabel(self)
        self.homeTabBarLabel.setGeometry(33, 45 ,86, 71)
        self.homeTabBarLabel.setStyleSheet('''
                                     background-color:#403042;
                                     border-radius:  24px 24px 0px 0px; 
                                     ''')
        
        self.seleteTabBarLabel = QLabel(self)
        self.seleteTabBarLabel.setGeometry(33, 45 ,86, 390)
        self.seleteTabBarLabel.setStyleSheet('''background-color:#F4E2FF;
                                                border-radius:28px;
                                            ''')

        self.startoverBtn = QPushButton("Start Over", self)
        self.startoverBtn.setGeometry(449, 423, 124, 39)
        self.startoverBtn.setStyleSheet('''background-color:#DDBEFC;
                                            border-radius: 10px;
                                            color: #4F0C59;
                                            font-size: 22px;
                                            font-weight: 700;
                                            font-family: 'Mada', serif;''')
        self.saveBtn= QPushButton("Save", self)
        self.saveBtn.setGeometry(590, 423, 124, 39)
        self.saveBtn.setStyleSheet('''background-color:#D6BEFC; 
                                        border-radius: 10px;
                                        color: #2E0C59;
                                        font-size: 22px;
                                        font-weight: 700;
                                        font-family: 'Mada', serif;''')
        
       
        
    def shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)  # Adjust the blur radius as needed
        shadow.setColor(QColor(234, 208, 219, 255))
        shadow.setOffset(12, 12)
        return shadow
    #kdsomg