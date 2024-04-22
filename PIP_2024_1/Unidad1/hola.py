import sys
from PyQt5 import uic,QtWidgets
qtcreatorFile = "P_00Plantilla.ui"
UI_MainWindow, QtBaseClass = uic.loadUiType(qtcreatorFile)

class MyApp(QtWidgets,QMainWindow,UI_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_MainWindow.__init__(self)
        self.setupUI(self)
        
        
        
        