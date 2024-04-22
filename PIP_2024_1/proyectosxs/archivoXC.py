import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog, QDialog, QTableWidget, QTableWidgetItem, QMessageBox


class DataWindow(QDialog):
    def __init__(self, filename):
        super().__init__()
        self.setWindowTitle("Editar")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()

        self.load_csv(filename)

        self.layout.addWidget(self.table)

        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.save_data)
        self.layout.addWidget(self.save_button)

    def load_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(data[0]))
            self.table.setHorizontalHeaderLabels(["Nombre","Edad","Email"])
            for i, row in enumerate(data[1:]):
                for j, item in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(item))

    def save_data(self):
        data = []
        for i in range(self.table.rowCount()):
            row = []
            for j in range(self.table.columnCount()):
                item = self.table.item(i, j)
                if item is not None:
                    row.append(item.text())
                else:
                    row.append("")
            data.append(row)
        
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV (*.csv)')
        if filename:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)

        QMessageBox.information(self, "Listo", "Datos guardados")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guardar datos")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.inputs = []
        self.labels = ["Nombre", "Edad", "Email"]
        for label in self.labels:
            widget = QWidget()
            widget_layout = QHBoxLayout()
            label_widget = QLabel(label)
            input_widget = QLineEdit()
            widget_layout.addWidget(label_widget)
            widget_layout.addWidget(input_widget)
            widget.setLayout(widget_layout)
            self.layout.addWidget(widget)
            self.inputs.append(input_widget)

        self.save_button = QPushButton("Guardar Archivo")
        self.save_button.clicked.connect(self.save_to_csv)

        self.open_button = QPushButton("Abrir Archivo")
        self.open_button.clicked.connect(self.open_csv)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.open_button)
        self.layout.addLayout(button_layout)

    def save_to_csv(self):
        data = []
        for input_widget in self.inputs:
            data.append(input_widget.text())
        
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV (*.csv)')
        if filename:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)

    def open_csv(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV (*.csv)')
        if filename:
            data_window = DataWindow(filename)
            data_window.exec()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
