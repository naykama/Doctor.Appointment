from PyQt5 import QtWidgets
from CourseWorkQt import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject
from Patient import Ui_DialogPatientName
from Fix import Ui_DialogFix
from Doctor import Ui_DialogDoctor
from Lunch import Ui_DialogLunch
import sys
import csv
from datetime import datetime as DT, timedelta
import subprocess
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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
        for i in patientDict:
            self.ui.comboBoxPatient.addItem(patientDict[i].surname+' '+patientDict[i].name+' '
                                            +patientDict[i].patronimic + ' '
                                            +patientDict[i].birthday)
        self.ui.comboBoxPatient.activated[str].connect(self.onActivated)
        
    def onActivated(self,text):
        for i in patientDict:
            if (patientDict[i].surname+' '+patientDict[i].name+' '
                +patientDict[i].patronimic + ' '
                +patientDict[i].birthday == text):
                self.ui.lineEditSurname.setText(patientDict[i].surname)
                self.ui.lineEditName.setText(patientDict[i].name)
                self.ui.lineEditPatron.setText(patientDict[i].patronimic)
                self.ui.lineEditBirthday.setText(patientDict[i].birthday)
                self.ui.lineEditPhone.setText(patientDict[i].phone)
                pass
        
    def show_doctor_window(self):
        if (self.ui.lineEditSurname.text()=='' or self.ui.lineEditName.text()==''
            or self.ui.lineEditBirthday.text()==''
            or self.ui.lineEditPhone.text()==''):
                QMessageBox.about(self, "Некорректный ввод", "Не все обязательные поля заполнены! (Фамилия, имя, дата рождения, телефон)")
        else:
            self.doctorW = doctorwindow()
            self.doctorW.exec()
        
    def button_click(self):        
        surname = self.ui.lineEditSurname.text()
        name = self.ui.lineEditName.text()
        patronimic = self.ui.lineEditPatron.text()
        bdate = self.ui.lineEditBirthday.text()
        phone = self.ui.lineEditPhone.text()
        p_key = max(patientDict.keys())+1
        global new_patient
        new_patient = Patient(str(p_key), surname, name, patronimic, bdate, phone)
        self.show_doctor_window()

class fixwindow(QtWidgets.QDialog):
    def __init__(self):
        super(fixwindow, self).__init__()
        self.ui = Ui_DialogFix()
        self.ui.setupUi(self)
        self.ui.buttonLunch.clicked.connect(self.show_lunch_window)
        self.ui.buttonDoctors.clicked.connect(self.show_file_doctors)
        self.ui.buttonShedule.clicked.connect(self.show_file_shedule)
        self.ui.buttonPatients.clicked.connect(self.show_file_patients)
        self.ui.buttonRecord.clicked.connect(self.show_file_record)
    def show_lunch_window(self):
        self.lunchW = lunchwindow()
        self.lunchW.exec()
    def show_file_doctors(self):
        subprocess.Popen(('start', 'C:\\Ucheba\\course_2\\TechProg\\CourseWork\\Doctors.csv'),
                         shell = True)
    def show_file_shedule(self):
        subprocess.Popen(('start', 'C:\\Ucheba\\course_2\\TechProg\\CourseWork\\Reception_shedule.csv'),
                         shell = True)
    def show_file_patients(self):
        subprocess.Popen(('start', 'C:\\Ucheba\\course_2\\TechProg\\CourseWork\\Patient.csv'),
                         shell = True)
    def show_file_record(self):
        subprocess.Popen(('start', 'C:\\Ucheba\\course_2\\TechProg\\CourseWork\\Reception.csv'),
                         shell = True)

class doctorwindow(QtWidgets.QDialog):
    d_id = -1
    r_date = ""
    n_time = ""
    def __init__(self):
        super(doctorwindow, self).__init__()
        self.ui = Ui_DialogDoctor()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.come_back_patient)
        self.ui.writeButton.clicked.connect(self.do_record)
        profile_set = set()
        for i in doctorDict:
            if ( doctorDict[i].profile in profile_set):
                pass
            else:
                self.ui.comboBoxProf.addItem(doctorDict[i].profile)
                profile_set.add(doctorDict[i].profile)
        self.ui.comboBoxProf.activated[str].connect(self.onActivatedProf)
    def onActivatedProf(self, text):
        if (self.ui.comboBoxFIO.count != 0):
            self.ui.comboBoxFIO.clear()
        for i in doctorDict:
            if (doctorDict[i].profile == text):
                self.ui.comboBoxFIO.addItem(doctorDict[i].surname +' '+ doctorDict[i].name[0] +
                                            '. ' + doctorDict[i].patronimic[0]+'.')
        self.ui.comboBoxFIO.activated[str].connect(self.onActivatedFIO)
    def onActivatedFIO(self,text):
        if (self.ui.comboBoxDay.count != 0):
            self.ui.comboBoxDay.clear()
        for i in doctorDict:
            if (doctorDict[i].surname +' '+ doctorDict[i].name[0] +
                '. ' + doctorDict[i].patronimic[0]+'.' == text):
                global d_id
                d_id = doctorDict[i].ID        
        for i in sheduleDict:
            if (sheduleDict[i].doctorID == d_id):
                self.ui.comboBoxDay.addItem(sheduleDict[i].date)
        self.ui.comboBoxDay.activated[str].connect(self.onActivatedDay)
        
    def onActivatedDay(self,text):
        if (self.ui.comboBoxTime.count != 0):
            self.ui.comboBoxTime.clear()
##        Время начала приёма
        beginT = DT.strptime('00:00', '%H:%M')
        endT = DT.strptime('00:00', '%H:%M')
        global r_date
        r_date = text
        for i in sheduleDict:
            if (sheduleDict[i].date == text and sheduleDict[i].doctorID == d_id):
                beginT = DT.strptime(sheduleDict[i].beginTime, '%H:%M')
                endT = DT.strptime(sheduleDict[i].endTime, '%H:%M')
        breaktime = DT.strptime('12:00', '%H:%M')
        r_time = beginT
        r_min = int(doctorDict[d_id].time)
        while (r_time +timedelta(minutes=r_min)<=endT):
            if (str(d_id)+r_date+r_time.strftime('%H:%M') in receptionDict.keys()):
                r_time = r_time + timedelta(minutes=int(doctorDict[d_id].time))
                pass
            else:
                if(r_time +timedelta(minutes=r_min)>breaktime and
                    r_time +timedelta(minutes=r_min)<=breaktime+timedelta(hours = 1)):
                    r_time = breaktime+timedelta(hours = 1)
                else:
                    self.ui.comboBoxTime.addItem(r_time.strftime('%H:%M'))
                    r_time = r_time + timedelta(minutes=int(doctorDict[d_id].time))
        self.ui.comboBoxTime.activated[str].connect(self.onActivatedTime)
    def onActivatedTime(self,text):
        global n_time
        n_time = text
        global new_reception
        new_reception = Reception(str(d_id), str(new_patient.ID), r_date, text)
                
    def come_back_patient(self):
        self.close()
        
    def do_record(self):
        is_new_p = True
        p_id = new_patient.ID
        for i in patientDict:
            if (new_patient.surname == patientDict[i].surname and
                new_patient.name == patientDict[i].name and
                new_patient.patronimic == patientDict[i].patronimic and
                new_patient.birthday == patientDict[i].birthday and
                new_patient.phone == patientDict[i].phone):
                is_new_p = False
                p_id = i
                pass
        if (is_new_p):
            patientDict[max(patientDict.keys())+1] = new_patient
        else:
            global new_reception
            new_reception = Reception(str(d_id), str(p_id), r_date, n_time)
        receptionDict[str(new_reception.doctorID)+new_reception.date
                      +new_reception.time] = new_reception
        patientWrite()
        receptionWrite()
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
##        count = 0;
        for row in file_reader:
            reception = Reception( row["Врач_ID"], row["Пациент_ID"],row["Дата"],row["Время"])
            receptionDict[str(reception.doctorID) + reception.date + reception.time] = reception
##            count+=1

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
new_patient = Patient("0","","","","","")
new_reception = Reception("0","0","","")
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

