# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_phone_code.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(779, 601)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(150, 170, 451, 231))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.codeLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.codeLineEdit.setGeometry(QtCore.QRect(120, 100, 241, 25))
        self.codeLineEdit.setObjectName("codeLineEdit")
        self.codeLabel = QtWidgets.QLabel(self.groupBox)
        self.codeLabel.setGeometry(QtCore.QRect(70, 100, 41, 17))
        self.codeLabel.setObjectName("codeLabel")
        self.LoginpushButton = QtWidgets.QPushButton(self.groupBox)
        self.LoginpushButton.setGeometry(QtCore.QRect(120, 140, 89, 25))
        self.LoginpushButton.setObjectName("LoginpushButton")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(220, 140, 141, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Enter phone code"))
        self.codeLabel.setText(_translate("Dialog", "Code"))
        self.LoginpushButton.setText(_translate("Dialog", "Login now"))
        self.pushButton.setText(_translate("Dialog", "Back to Send Code"))
