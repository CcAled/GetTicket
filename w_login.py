# -*- coding: utf-8 -*-

# Login implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QCoreApplication
import sys

User=['12','3','342928796@qq.com']
class w_login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 300)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(30, 60, 54, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Login)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 140, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 54, 12))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton.clicked.connect(self.getUserInfo)
        QtCore.QMetaObject.connectSlotsByName(Login)
#用这个的话整个程序被退出
#        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
#        QtCore.QMetaObject.connectSlotsByName(Login)
#        self.pushButton.clicked.connect()
#        QtCore.QMetaObject.connectSlotsByName(Login)

    def getUserInfo(self):
        User[0]=self.lineEdit.text()
        User[1]=self.lineEdit_2.text()
        User[2]=self.lineEdit_3.text()
        print(User)
#        QtWidgets.QWidget.showMinimized()
#        QtWidgets.QWidget.setwindowState(QtCore.Qt.windowMinimized)
#        self.hide()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录"))
        self.label.setText(_translate("Login", "用户名"))
        self.label_2.setText(_translate("Login", "密码"))
        self.label_3.setText(_translate("Login", "电子邮箱"))
        self.pushButton.setText(_translate("Login", "登录"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = w_login()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())












