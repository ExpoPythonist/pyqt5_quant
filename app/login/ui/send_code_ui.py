# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_code.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelegrameAccountLogin(object):
    def setupUi(self, TelegrameAccountLogin):
        TelegrameAccountLogin.setObjectName("TelegrameAccountLogin")
        TelegrameAccountLogin.resize(776, 600)
        font = QtGui.QFont()
        font.setItalic(False)
        TelegrameAccountLogin.setFont(font)
        self.groupBoxTelegram = QtWidgets.QGroupBox(TelegrameAccountLogin)
        self.groupBoxTelegram.setGeometry(QtCore.QRect(110, 170, 531, 211))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxTelegram.setFont(font)
        self.groupBoxTelegram.setObjectName("groupBoxTelegram")
        self.label = QtWidgets.QLabel(self.groupBoxTelegram)
        self.label.setGeometry(QtCore.QRect(140, 90, 121, 17))
        self.label.setObjectName("label")
        self.sendCodeButton = QtWidgets.QPushButton(self.groupBoxTelegram)
        self.sendCodeButton.setGeometry(QtCore.QRect(210, 150, 89, 25))
        self.sendCodeButton.setObjectName("sendCodeButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBoxTelegram)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(260, 90, 171, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(TelegrameAccountLogin)
        QtCore.QMetaObject.connectSlotsByName(TelegrameAccountLogin)

    def retranslateUi(self, TelegrameAccountLogin):
        _translate = QtCore.QCoreApplication.translate
        TelegrameAccountLogin.setWindowTitle(_translate("TelegrameAccountLogin", "Telegram Account Login"))
        self.groupBoxTelegram.setTitle(_translate("TelegrameAccountLogin", "Telegram Account Login"))
        self.label.setText(_translate("TelegrameAccountLogin", "Phone Number"))
        self.sendCodeButton.setText(_translate("TelegrameAccountLogin", "Send Code "))
