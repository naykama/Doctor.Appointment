from PyQt5 import QtWidgets
from CourseWorkQt import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
from Patient import Ui_DialogPatientName
from Fix import Ui_DialogFix
from Doctor import Ui_DialogDoctor
from Lunch import Ui_DialogLunch
import sys
 
class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.appointButton.clicked.connect(self.show_patient_window)
        self.ui.fixButton.clicked.connect(self.show_fix_window)
       
    def show_patient_window(self):
        self.patientW = patientwindow()
        self.patientW.show()

    def show_fix_window(self):
        self.fixW = fixwindow()
        self.fixW.show()
        
class patientwindow(QtWidgets.QDialog):
    def __init__(self):
        super(patientwindow, self).__init__()
        self.ui = Ui_DialogPatientName()
        self.ui.setupUi(self)
        self.ui.continueButton.clicked.connect(self.button_click)
##        self.patientwindow.setWindowModality(QtCore.Qt.WindowModal)

    def show_doctor_window(self):
        self.w2 = doctorwindow()
        self.w2.show()
        
    def button_click(self):        
        surname = self.ui.lineEditSurname.text()
        name = self.ui.lineEditName.text()
        patronimic = self.ui.lineEditPatron.text()
        bdate = self.ui.lineEditBirthday.text()
        phone = self.ui.lineEditPhone.text()
        self.show_doctor_window()

class fixwindow(QtWidgets.QDialog):
    def __init__(self):
        super(fixwindow, self).__init__()
        self.ui = Ui_DialogFix()
        self.ui.setupUi(self)
        self.ui.buttonLunch.clicked.connect(self.show_lunch_window)
        
    def show_lunch_window(self):
        self.w2 = lunchwindow()
        self.w2.show()

class doctorwindow(QtWidgets.QDialog):
    def __init__(self):
        super(doctorwindow, self).__init__()
        self.ui = Ui_DialogDoctor()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.close)
        self.ui.writeButton.clicked.connect(self.close_windows)
        
    def close_windows(self):
        self.close()
        mainW.patientW.close()
        mainW.patientW.close()
        
            
class lunchwindow(QtWidgets.QDialog):
    def __init__(self):
        super(lunchwindow, self).__init__()
        self.ui = Ui_DialogLunch()
        self.ui.setupUi(self)        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = mainwindow()
    mainW.show()
    sys.exit(app.exec_())
