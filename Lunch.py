# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lunch.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLunch(object):
    def setupUi(self, DialogLunch):
        DialogLunch.setObjectName("DialogLunch")
        DialogLunch.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogLunch)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineBeginH = QtWidgets.QLineEdit(DialogLunch)
        self.lineBeginH.setGeometry(QtCore.QRect(40, 110, 31, 20))
        self.lineBeginH.setObjectName("lineBeginH")
        self.lineBeginM = QtWidgets.QLineEdit(DialogLunch)
        self.lineBeginM.setGeometry(QtCore.QRect(110, 110, 31, 20))
        self.lineBeginM.setObjectName("lineBeginM")
        self.lineEndH = QtWidgets.QLineEdit(DialogLunch)
        self.lineEndH.setGeometry(QtCore.QRect(250, 110, 31, 20))
        self.lineEndH.setObjectName("lineEndH")
        self.lineEndM = QtWidgets.QLineEdit(DialogLunch)
        self.lineEndM.setGeometry(QtCore.QRect(320, 110, 31, 20))
        self.lineEndM.setObjectName("lineEndM")
        self.label = QtWidgets.QLabel(DialogLunch)
        self.label.setGeometry(QtCore.QRect(80, 80, 47, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogLunch)
        self.label_2.setGeometry(QtCore.QRect(290, 80, 47, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogLunch)
        self.label_3.setGeometry(QtCore.QRect(86, 110, 16, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DialogLunch)
        self.label_4.setGeometry(QtCore.QRect(300, 110, 16, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(DialogLunch)
        self.buttonBox.accepted.connect(DialogLunch.accept)
        self.buttonBox.rejected.connect(DialogLunch.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogLunch)

    def retranslateUi(self, DialogLunch):
        _translate = QtCore.QCoreApplication.translate
        DialogLunch.setWindowTitle(_translate("DialogLunch", "Обеденный перерыв"))
        self.label.setText(_translate("DialogLunch", "Начало"))
        self.label_2.setText(_translate("DialogLunch", "Конец"))
        self.label_3.setText(_translate("DialogLunch", ":"))
        self.label_4.setText(_translate("DialogLunch", ":"))
