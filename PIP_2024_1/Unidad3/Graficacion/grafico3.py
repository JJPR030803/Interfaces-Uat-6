from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QVBoxLayout,QPushButton,QMainWindow,QLabel,QHBoxLayout
from PyQt6.QtCore import Qt,QRect
import sys

class MyApp(QMainWindow):
    
        
        
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("App1")
        self.setGeometry(100,100,800,600)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        #layout = QHBoxLayout(central_widget)
        self.label1 = QLabel(parent=self,text="A:")
        self.label2 = QLabel(parent=self,text="B:")
        self.label1.setGeometry(150,175,100,100)
        self.label2.setGeometry(150,275,100,100)
        self.texto_edit1 = QLineEdit(self)
        self.texto_edit1.setGeometry(200,200,100,50)
        self.texto_edit2 = QLineEdit(self)
        self.texto_edit2.setGeometry(200,300,100,50)
        self.resultado_label = QLineEdit(parent=self,text="")
        self.resultado_label.setGeometry(500,400,200,100)
        
        self.boton_suma = QPushButton(parent=self,text= "SUMAR")
        self.boton_suma.setGeometry(200,400,200,100)
        self.boton_suma.clicked.connect(self.funcion_boton)
        
        #layout.setSpacing(10)
        ##   layout.addWidget(widget)
        
        #elf.setLayout(layout)
        
    def funcion_boton(self):
        print(int(self.texto_edit1.text) == int)
        #resultado = self.texto_edit1.text + self.texto_edit2.text
        #self.resultado_label.setText(str(resultado))
        #print(resultado)
        #return resultado
    
    def funcion_salir(self):
        self.close()
        
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = MyApp()
    application.show()
    sys.exit(app.exec())
    
    
     