from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import math

class Imagenes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Imagenes')
        self.resize(400,200)
        self.setStyleSheet("background-color: orange;")
        self.initUI()

    def initUI(self):
        # Labels
        self.label1 = QLabel()
        pixmap = QPixmap("pepe-the-frog-1272162_640.jpg")
        self.labelResult = QLabel()
        self.label1.setPixmap(pixmap)
    

        # LineEdits
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit1.setAlignment(20,200)
        

        # Button
        self.btnCalculate = QPushButton('Calculate Distance')
        self.btnCalculate.setStyleSheet("background-color: #4CAF50; color: white; border: 2px solid #4CAF50;")
        self.btnCalculate.clicked.connect(self.calculateDistance)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.lineEdit1)
        
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.btnCalculate)
        layout.addWidget(self.labelResult)
        self.setLayout(layout)

    def calculateDistance(self):
        try:
            x1, y1 = map(float, self.lineEdit1.text().split(','))
            x2, y2 = map(float, self.lineEdit2.text().split(','))
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            self.labelResult.setText(f"Distance between the points: {distance:.2f}")
        except ValueError:
            self.labelResult.setText("Ingrese las coordenadas 'x, y'.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Imagenes()
    window.show()
    sys.exit(app.exec_())