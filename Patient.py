# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Patient.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogPatientName(object):
    def setupUi(self, DialogPatientName):
        DialogPatientName.setObjectName("DialogPatientName")
        DialogPatientName.resize(647, 281)
        self.label = QtWidgets.QLabel(DialogPatientName)
        self.label.setGeometry(QtCore.QRect(60, 60, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogPatientName)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogPatientName)
        self.label_3.setGeometry(QtCore.QRect(290, 60, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DialogPatientName)
        self.label_4.setGeometry(QtCore.QRect(390, 60, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(DialogPatientName)
        self.label_5.setGeometry(QtCore.QRect(540, 60, 91, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditSurname = QtWidgets.QLineEdit(DialogPatientName)
        self.lineEditSurname.setGeometry(QtCore.QRect(20, 90, 113, 20))
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.lineEditName = QtWidgets.QLineEdit(DialogPatientName)
        self.lineEditName.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditPatron = QtWidgets.QLineEdit(DialogPatientName)
        self.lineEditPatron.setGeometry(QtCore.QRect(260, 90, 113, 20))
        self.lineEditPatron.setObjectName("lineEditPatron")
        self.lineEditBirthday = QtWidgets.QLineEdit(DialogPatientName)
        self.lineEditBirthday.setGeometry(QtCore.QRect(380, 90, 113, 20))
        self.lineEditBirthday.setObjectName("lineEditBirthday")
        self.lineEditPhone = QtWidgets.QLineEdit(DialogPatientName)
        self.lineEditPhone.setGeometry(QtCore.QRect(500, 90, 113, 20))
        self.lineEditPhone.setObjectName("lineEditPhone")
        self.comboBoxPatient = QtWidgets.QComboBox(DialogPatientName)
        self.comboBoxPatient.setGeometry(QtCore.QRect(50, 150, 551, 22))
        self.comboBoxPatient.setObjectName("comboBoxPatient")
        self.continueButton = QtWidgets.QPushButton(DialogPatientName)
        self.continueButton.setGeometry(QtCore.QRect(510, 220, 111, 41))
        self.continueButton.setObjectName("continueButton")

        self.retranslateUi(DialogPatientName)
        QtCore.QMetaObject.connectSlotsByName(DialogPatientName)

    def retranslateUi(self, DialogPatientName):
        _translate = QtCore.QCoreApplication.translate
        DialogPatientName.setWindowTitle(_translate("DialogPatientName", "Пациент"))
        self.label.setText(_translate("DialogPatientName", "Фамилия"))
        self.label_2.setText(_translate("DialogPatientName", "Имя"))
        self.label_3.setText(_translate("DialogPatientName", "Отчество"))
        self.label_4.setText(_translate("DialogPatientName", "Дата рождения"))
        self.label_5.setText(_translate("DialogPatientName", "Телефон"))
        self.continueButton.setText(_translate("DialogPatientName", "Далее"))
