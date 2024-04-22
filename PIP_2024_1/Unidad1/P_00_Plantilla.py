import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_00_Plantilla.ui"  # Nombre del archivo aquí.
uifile = QFile(qtCreatorFile)
Ui_MainWindow, QtBaseClass = uic.loadUiType(uifile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def operacion(self):
        try:
            objeto = sender()
            nombre = objeto.objectName()
            print(nombre)
            if nombre == "btn_sumar":
                r = A+B
            elif nombre == "btn_restar":
                r = A-B
            elif nombre == "btn_multiplicar":
                r = A*B
            else: nombre == "btn_dividir"
    def __init__(self):
        uic.loadUi("P_00_Plantilla.ui",self)
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


