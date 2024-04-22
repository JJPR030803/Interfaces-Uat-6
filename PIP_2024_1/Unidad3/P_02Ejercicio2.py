import sys
from archivos import fileFunc
from PyQt6.QtWidgets import QApplication, QMainWindow,QVBoxLayout,QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio 2')
        self.setGeometry(100, 100, 400, 300) 
        self.initUI()
        
    def initUI(self):
        
        layout = QVBoxLayout()
        
        texto = QLabel(str("Hola Mundo"))
        layout.addWidget(texto)
        self.setLayout(layout)

if __name__ == '__main__':
    fileFunc.prueba
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
