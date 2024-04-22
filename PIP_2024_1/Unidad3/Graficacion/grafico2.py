from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QVBoxLayout,QPushButton,QGridLayout
from PyQt6.QtCore import Qt,QRect
import sys

class MyApp(QWidget):
    
        
        
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("App1")
        self.setFixedHeight(200)
        self.setFixedWidth(200)
        self.texto = QLineEdit("Texto")
        self.boton = QPushButton(text="Oprimir",)
        self.boton.clicked.connect(self.funcion_boton)
        self.boton.setGeometry(QRect(500,500,500,500))
        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(self.funcion_salir)
        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.boton)
        layout.addWidget(self.boton_salir)
        self.setLayout(layout)
        
    def funcion_boton(self):
        print("Hola mundo")
        self.texto.setText("Hola Mundo")
    def funcion_salir(self):
        self.close()
    

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = MyApp()
    application.show()
    sys.exit(app.exec())
    
    
     