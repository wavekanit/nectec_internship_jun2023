#NewTest Page

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGraphicsDropShadowEffect, QComboBox, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QPixmap, QColor

class New_Test(QWidget):
    def __init__(self):
        super().__init__()
                
        self.headLebel = QLabel("Please enter sample information below", self)
        self.headLebel.setGeometry(88, 125, 600, 60)
        self.headLebel.setStyleSheet("background-color: rgba(255,255,255,0); color: #5B3985; font-size: 30px; font-family: 'Mada', serif; font-weight: 700;")
        
        self.lebelTestName = QLabel("Test Name  :", self)
        self.lebelTestName.setGeometry(146, 209, 130, 33)
        self.lebelTestName.setStyleSheet("background-color: rgba(255,255,255,0); font-size: 24px; color: #39174A; font-weight: 700; font-family: 'Mada', serif;")
        
        self.lebelType = QLabel("Type  :", self)
        self.lebelType.setGeometry(205, 275, 70, 33)
        self.lebelType.setStyleSheet("background-color: rgba(255,255,255,0); font-size: 24px; color: #39174A; font-weight: 700; font-family: 'Mada', serif;")
        
        self.lebelCarlibration = QLabel("Carlibration Curves  :", self)
        self.lebelCarlibration.setGeometry(57, 341, 220, 33)
        self.lebelCarlibration.setStyleSheet("background-color: rgba(255,255,255,0); font-size: 24px; color: #39174A; font-weight: 700; font-family: 'Mada', serif;")
        
        self.inputTestName = QLineEdit(self)
        self.inputTestName.setGeometry(301, 213, 356, 29)
        self.inputTestName.setStyleSheet("background-color: #F0D8FF; border-radius: 10px;color: #69647D; font-size: 18px;font-weight: 600;")
        
        self.inputType = QLineEdit(self)
        self.inputType.setGeometry(301, 279, 356, 29)
        self.inputType.setStyleSheet("border-radius: 10px; background: #F0D8FF;color: #69647D; font-size: 18px;font-weight: 600;")
        
        self.inputCarlibration = QComboBox(self)
        self.inputCarlibration.setGeometry(301, 345, 356, 29)
        self.inputCarlibration.addItems(["Select","Assay lot #0543533", "Example 2", "Example 3"])
        self.inputCarlibration.setStyleSheet("background-color: #F0D8FF; border-radius: 10px;color: #69647D; font-size: 18px;font-family: 'Mada',serif;font-weight: 700;text-align: center;")
        
        self.startAnalysisBtn = QPushButton("Start Analysis", self)
        self.startAnalysisBtn.setGeometry(533, 400, 207, 45)
        self.startAnalysisBtn.setStyleSheet('''
                                            background-color:#430B41;
                                            border-radius: 17px; 
                                            color: #FBFAFF; 
                                            font-family: 'Mada', serif;
                                            font-size: 22px;
                                            font-weight: 600;
                                            ''')
        
    def shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(0)  # Adjust the blur radius as needed
        shadow.setColor(QColor(234, 208, 219, 255))
        shadow.setOffset(12, 12)
        return shadow