import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import math

class DistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grados')
        self.resize(400,200)
        self.setStyleSheet("background-color: white;")
        self.initUI()

    def initUI(self):
        # Labels
        self.label1 = QLabel('Introduzca la calificacion:')
        self.labelResult = QLabel()

        # LineEdits
        self.lineEdit1 = QLineEdit()

        # Button
        self.btnCalculate = QPushButton('Obtener Grado')
        self.btnCalculate.setStyleSheet("background-color: #4CAF50; color: white; border: 2px solid #4CAF50;")
        self.btnCalculate.clicked.connect(self.calculateDistance)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.btnCalculate)
        layout.addWidget(self.labelResult)
        self.setLayout(layout)

    def calculateDistance(self):
        grad = ''
        cal = int(self.lineEdit1.text())
        if cal <=10 and cal >= 0:
             if cal == 10:
                grad = 'A'
                self.labelResult.setText(f"Grado: {grad}")
             elif cal == 9:
                grad = 'B'
                self.labelResult.setText(f"Grado: {grad}")
             elif cal == 8 or 7 or 6 :
                grad = 'C'
                self.labelResult.setText(f"Grado: {grad}")
             elif cal <=5:
                grad = 'F'
                self.labelResult.setText(f"Grado: {grad}")
             else:
                grad = 'Introduzca un numero valido'
        else:
            self.labelResult.setText('Introduzca un numero del 1 al 10 ')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DistanceCalculator()
    window.show()
    sys.exit(app.exec_())