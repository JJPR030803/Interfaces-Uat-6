import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "PIP_2024_1/Unidad1/P_00_Plantilla.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_saludar.clicked.connect(self.saludar)
        
    def saludar(self):
        msj = QtWidgets.QMessageBox()
        msj.setText("Hola a todos")
        msj.exec_()
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)