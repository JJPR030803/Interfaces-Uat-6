import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit,QMessageBox,QDialog
from PyQt6.QtCore import QTimer, QTime,Qt

class ClockApp(QWidget):
    def __init__(self):
        super().__init__()
        current_time = "12:00:00"
        alarm_time = "00:00:00"
        

        self.setWindowTitle("Reloj y Alarma")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Clock label
        self.clock_label = QLabel()
        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.clock_label)
        

        self.alarm_input = QLineEdit()
        self.alarm_input.setPlaceholderText("Ingrese tiempo de alarma (HH:MM)")
        layout.addWidget(self.alarm_input)
        

        self.set_alarm_button = QPushButton("Set Alarm")
        self.set_alarm_button.clicked.connect(self.activar_alarma(actual=current_time,alarma=alarm_time))
        layout.addWidget(self.set_alarm_button)

        self.setLayout(layout)


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time(current_times=current_time))
        self.timer.start(1000) 
        self.update_time(current_times=current_time)
       

    def update_time(self,current_times):
        current_times = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_times)
        self.alarm_input.clear()
        
        
    def activar_alarma(self,alarma,actual):
        print(alarma)
        if ":" not in alarma:
            return  
        else:
            self.alarma(alarma,actual)
            
            
    def alarma(time_alarma,time_actual,self):
        if time_alarma == time_actual:
            print("Exito")
            self.alarm_triggered()

        

    def alarm_triggered(self):
      alarm_window = QDialog(self)
      alarm_window.setWindowTitle("Alarm")
      layout = QVBoxLayout()
      label = QLabel("Alarm triggered!")
      label.setAlignment(Qt.AlignmentFlag.AlignCenter)
      layout.addWidget(label)
      alarm_window.setLayout(layout)
      alarm_window.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock_app = ClockApp()
    clock_app.show()
    sys.exit(app.exec())
