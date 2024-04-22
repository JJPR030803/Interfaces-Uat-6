qtCreatorFile = "P_00Plantilla.ui"  # Nombre del archivo aquí.
uifile = QFile(qtCreatorFile)
Ui_MainWindow, QtBaseClass = uic.loadUiType(uifile)
