#Start Analysis Page

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton

#XY point
xPoint = 300
yPoint = 200
# sizeInRadius = 20

class Start_Analysis(QWidget):
    def __init__(self):
        super().__init__()
        self.progress = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)
        self.progressCount = QLabel("0 %",self)
        self.progressCount.setGeometry(358, 274, 100, 51)
        self.progressCount.setStyleSheet('''background-color: rgba(255, 255, 255, 0); 
                                        color:#8B3A6A; 
                                        font-size: 30px; 
                                        font-family: 'Mada', sans-serif; 
                                        font-weight: 700;
                                        ''')
       # self.progressCount.move(384,291)

        self.headLebelStartAnalys = QLabel("Measurement in progress...", self)
        self.headLebelStartAnalys.setGeometry(192, 125, 600, 60)
        self.headLebelStartAnalys.setStyleSheet('''background-color: rgba(255,255,255,0); 
                                                color: #3E3744; 
                                                font-size: 32px; 
                                                font-family: 'Mada', serif;
                                                font-weight: 700;
                                                ''')

        self.titleLebelStartAnalys = QLabel("Please wait", self)
        self.titleLebelStartAnalys.setGeometry(352, 167, 100, 30)
        self.titleLebelStartAnalys.setStyleSheet('''background-color: rgba(255,255,255,0); 
                                                color: #3E3744; 
                                                font-size: 20px; 
                                                font-family: 'Mada', serif; 
                                                font-weight: 300;''')

        self.canclebtn = QPushButton("Cancel", self)
        self.canclebtn.setGeometry(527, 422, 215, 44)
        self.canclebtn.setStyleSheet('''background-color: #CB3333; 
                                    color: #FBFAFF; 
                                    font-size: 26px;
                                    font-family: 'Mada', sans-serif; 
                                    font-weight: 700; border-radius: 19px;
                                    ''')
    
    def startAnimation(self, interval=100):
        self.timer.start(interval)

    def stopAnimation(self):
        self.timer.stop()

    def setProgress(self, value):
        self.progress = value
        self.update()

    def updateProgress(self):
        self.progress = (self.progress + 1) % 101
        temp = str(self.progress)
        self.progressCount.setText(temp + " %")
        self.update()

        if self.progress == 100:
            self.stopAnimation()

    def paintEvent(self, event):

        # Configure the painter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        
        # Draw the background circle
        bg_color = QColor(139, 58, 106,100)
        painter.setBrush(bg_color)
        painter.drawEllipse(xPoint, yPoint, 200, 200)

        # Draw the blank center
        blank_color = QColor(255,241,254)
        blank_radius = 200 - (32 * 2)  # Adjust the radius of the blank center
        painter.setBrush(blank_color)
        painter.drawEllipse(32 + xPoint, 32 + yPoint, int(blank_radius), int(blank_radius))

        # Draw the progress arc
        progress_color = QColor(255, 87, 117)
        painter.setBrush(progress_color)
        pen = QPen(progress_color, 32)
        pen.setCapStyle(Qt.RoundCap)  # Set round cap style
        painter.setPen(pen)
        
        radius = 200 - 32  # Adjust the radius of the progress bar
        start_angle = 90 * 16  # 90 degrees
        span_angle = -self.progress * 3.6 * 16  # 3.6 degrees per unit
        painter.drawArc(xPoint + 16, yPoint + 16, int(radius), int(radius), int(start_angle), int(span_angle))