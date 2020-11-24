from PyQt5 import QtWidgets
from CourseWorkQt import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
from Patient import Ui_DialogPatientName
import sys
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.appointButton.clicked.connect(self.show_patient_window)
        
    def show_patient_window(self):
        self.w2 = patientwindow()
        self.w2.show()
        
class patientwindow(QtWidgets.QDialog):
    def __init__(self):
        super(patientwindow, self).__init__()
        self.ui = Ui_DialogPatientName()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())
