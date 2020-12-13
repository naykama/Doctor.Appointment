from PyQt5 import QtWidgets
from CourseWorkQt import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
from Patient import Ui_DialogPatientName
from Fix import Ui_DialogFix
from Doctor import Ui_DialogDoctor
from Lunch import Ui_DialogLunch
import sys
import csv
 
class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.appointButton.clicked.connect(self.show_patient_window)
        self.ui.fixButton.clicked.connect(self.show_fix_window)
       
    def show_patient_window(self):
        self.patientW = patientwindow()
        self.patientW.exec()

    def show_fix_window(self):
        self.fixW = fixwindow()
        self.fixW.exec()
        
class patientwindow(QtWidgets.QDialog):
    def __init__(self):
        super(patientwindow, self).__init__()
        self.ui = Ui_DialogPatientName()
        self.ui.setupUi(self)
        self.ui.continueButton.clicked.connect(self.button_click)

    def show_doctor_window(self):
        self.doctorW = doctorwindow()
        self.doctorW.exec()
        
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
        self.lunchW = lunchwindow()
        self.lunchW.exec()

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
        
            
class lunchwindow(QtWidgets.QDialog):
    def __init__(self):
        super(lunchwindow, self).__init__()
        self.ui = Ui_DialogLunch()
        self.ui.setupUi(self)

class Patient (object):
    def __init__(self, ID, surname, name, patronimic, birthday, phone):
        """Constructor"""
        self.ID = int(ID)
        self.surname = surname
        self.name = name
        self.patronimic = patronimic
        self.birthday = birthday
        self.phone = phone

class Doctor (object):
    def __init__(self, ID, surname, name, patronimic, profile, time):
        """Constructor"""
        self.ID = int(ID)
        self.surname = surname
        self.name = name
        self.patronimic = patronimic
        self.profile = profile
        self.time = time

class Shedule (object):
    def __init__(self, doctorID, date, beginTime, endTime):
        """Constructor"""
        self.doctorID = int(doctorID)
        self.date = date
        self.beginTime = beginTime
        self.endTime = endTime

class Reception (object):
    def __init__(self, doctorID, patientID, date, time):
        """Constructor"""
        self.doctorID = int(doctorID)
        self.patientID = int(patientID)
        self.date = date
        self.time = time    

def patientRead():
    with open("Patient.csv") as rpatientF:
        file_reader = csv.DictReader(rpatientF, delimiter = ";")
        for row in file_reader:
            patient = Patient( row["Пациент_ID"], row["Фамилия"],row["Имя"],row["Отчество"],row["Дата_рождения"],row["Телефон"])
            patientDict[patient.ID] = patient

def patientWrite():
    with open("Patient.csv", mode="w", newline='') as wpatientF:
        names = ["Пациент_ID", "Фамилия", "Имя", "Отчество", "Дата_рождения", "Телефон"]
        file_writer = csv.DictWriter(wpatientF, delimiter = ";", fieldnames=names)
        file_writer.writeheader()
        for i in patientDict:
            file_writer.writerow({"Пациент_ID": str(patientDict.get(i).ID), "Фамилия": patientDict.get(i).surname, "Имя": patientDict.get(i).name,
                                  "Отчество": patientDict.get(i).patronimic, "Дата_рождения": patientDict.get(i).birthday,
                                  "Телефон": patientDict.get(i).phone})                  
def doctorRead():
    with open("Doctors.csv") as r_f:
        file_reader = csv.DictReader(r_f, delimiter = ";")
        for row in file_reader:
            doctor = Doctor( row["Врач_ID"], row["Фамилия"],row["Имя"],row["Отчество"],row["Специальность"],row["Время_приёма_одного_пациента(мин)"])
            doctorDict[doctor.ID] = doctor

def sheduleRead():
    with open("Reception_shedule.csv") as r_f:
        file_reader = csv.DictReader(r_f, delimiter = ";")
        count = 0;
        for row in file_reader:
            shedule = Shedule( row["Врач_ID"], row["Дата"],row["Начало_приёма"],row["Конец_приёма"])
            sheduleDict[count] = shedule
            count+=1

def receptionRead():
    with open("Reception.csv") as r_f:
        file_reader = csv.DictReader(r_f, delimiter = ";")
        count = 0;
        for row in file_reader:
            reception = Reception( row["Врач_ID"], row["Пациент_ID"],row["Дата"],row["Время"])
            receptionDict[count] = reception
            count+=1

def receptionWrite():
    with open("Reception.csv", mode="w", newline='') as wreceptionF:
        names = ["Врач_ID", "Пациент_ID", "Дата", "Время"]
        file_writer = csv.DictWriter(wreceptionF, delimiter = ";", fieldnames=names)
        file_writer.writeheader()
        for i in receptionDict:
            file_writer.writerow({"Врач_ID": str(receptionDict[i].doctorID), 
                                  "Пациент_ID": str(receptionDict[i].patientID),
                                  "Дата": receptionDict[i].date,
                                  "Время": receptionDict[i].time})                  
            
patientDict = {}
doctorDict = {}
sheduleDict = {}
receptionDict = {}

patientRead()
doctorRead()
sheduleRead()
receptionRead()
receptionWrite()
##keymax = max(receptionDict.keys())
##print(keymax)
patientWrite()
##for i in patientDict:
##    print(patientDict.get(i).surname)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = mainwindow()
    mainW.show()
    sys.exit(app.exec_())
