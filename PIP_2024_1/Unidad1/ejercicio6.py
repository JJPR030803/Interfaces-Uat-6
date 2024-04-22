import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import math

class PromCal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora Promedios')
        self.resize(400,600)
        self.setStyleSheet("background-color: orange;")
        self.initUI()

    def initUI(self):
        # Labels
        self.label1 = QLabel('Calificacion 1:')
        self.label2 = QLabel('Calificacion 2:')
        self.label3 = QLabel('Calificacion 3:')
        self.label4 = QLabel('Calificacion 4:')
        self.label5 = QLabel('Calificacion 5:')
        self.labelResult = QLabel()

        # LineEdits
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()

        # Button
        self.btnCalculate = QPushButton('Calcular Promedio')
        self.btnCalculate.setStyleSheet("background-color: #4CAF50; color: white; border: 2px solid #4CAF50;")
        self.btnCalculate.clicked.connect(self.calculateProm)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.lineEdit1)
        layout.addWidget(self.label2)
        layout.addWidget(self.lineEdit2)
        layout.addWidget(self.label3)
        layout.addWidget(self.lineEdit3)
        layout.addWidget(self.label4)
        layout.addWidget(self.lineEdit4)
        layout.addWidget(self.label5)
        layout.addWidget(self.lineEdit5)
        layout.addWidget(self.btnCalculate)
        layout.addWidget(self.labelResult)
        self.setLayout(layout)

    def calculateProm(self):
        try:
            x1 = int(self.lineEdit1.text())
            x2 = int(self.lineEdit2.text())
            x3 = int(self.lineEdit3.text())
            x4 = int(self.lineEdit4.text())
            x5 = int(self.lineEdit5.text())
            prom = (x1+x2+x3+x4+x5)/5
            self.labelResult.setText(f"Promedio = {prom}")
        except ValueError:
            self.labelResult.setText("Ingrese los numeros")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PromCal()
    window.show()
    sys.exit(app.exec_())