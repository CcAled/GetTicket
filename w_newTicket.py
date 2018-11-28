

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from tickets import Tickets, lot,seatsList
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)
import sys
import sys

#seatsList=['商务座特等座','一等座','二等座','高级软卧','软卧','动卧','硬卧','软座','硬座','无座']

class w_newTicket(QWidget):
    def __init__(self):
        super().__init__()
        hlayout = QtWidgets.QHBoxLayout()
        self.setLayout(hlayout)
        self.setWindowTitle("添加订单")
        self.setGeometry(300,300,500,300)

        vlayout0 = QtWidgets.QVBoxLayout()
        self.l_from=QtWidgets.QLabel()
        self.l_from.setText("始发站")
        vlayout0.addWidget(self.l_from)
        self.l_to=QtWidgets.QLabel()
        self.l_to.setText("终点站")
        vlayout0.addWidget(self.l_to)
        self.l_date=QtWidgets.QLabel()
        self.l_date.setText("时间(XXXX-X-X)")
        vlayout0.addWidget(self.l_date)
        self.l_train=QtWidgets.QLabel()
        self.l_train.setText("车次")
        vlayout0.addWidget(self.l_train)
        self.l_passenger=QtWidgets.QLabel()
        self.l_passenger.setText("乘客")
        vlayout0.addWidget(self.l_passenger)
        self.r_student = QtWidgets.QRadioButton()
        self.r_student.setText("是否购买学生票")
        vlayout0.addWidget(self.r_student)
        self.b_finish = QPushButton()
        self.b_finish.setText("完成")
        self.b_finish.setFixedSize(60,30)
        vlayout0.addWidget(self.b_finish)
        vwg0 = QtWidgets.QWidget()
        vwg0.setLayout(vlayout0)
        hlayout.addWidget(vwg0)

        vlayout1 = QtWidgets.QVBoxLayout()
        self.i_from=QtWidgets.QLineEdit()
        vlayout1.addWidget(self.i_from)
        self.i_to=QtWidgets.QLineEdit()
        vlayout1.addWidget(self.i_to)
        self.i_date=QtWidgets.QLineEdit()
        vlayout1.addWidget(self.i_date)
        self.i_train=QtWidgets.QLineEdit()
        vlayout1.addWidget(self.i_train)
        self.i_passenger=QtWidgets.QLineEdit()
        vlayout1.addWidget(self.i_passenger)

        self.seatCB = QComboBox(self)
        vlayout1.addWidget(self.seatCB)

        self.b_cancel = QPushButton()
        self.b_cancel.setText("取消")
        self.b_cancel.setFixedSize(60,30)
        vlayout1.addWidget(self.b_cancel)
        vwg1 = QtWidgets.QWidget()
        vwg1.setLayout(vlayout1)
        hlayout.addWidget(vwg1)

        self.init_seatCB()
#        self.b_finish.clicked.connect(self.getTicketInfo)
        self.b_cancel.clicked.connect(self.cancel)

    def cancel(self):
        self.hide()
        self.infoClear()

    def getTicketInfo(self):
        global lot
        p=0#统计信息是否全部填写
        self.isStudent = 0
        if self.i_from.text()!='':
            self.startStation=self.i_from.text()
            p+=1
        if self.i_to.text()!='':
            p+=1
            self.toStation = self.i_to.text()
        if self.i_date.text()!='':
            p+=1
            a = self.i_date.text().split("-")
            for i in range(len(a)):
                a[i] = int(a[i])
            self.date = a
        if self.i_train.text()!='':
            p+=1
            self.train=self.i_train.text()
        if self.i_passenger.text()!='':
            p+=1
            self.passenger=self.i_passenger.text()
        if self.r_student.isChecked():
            self.isStudent=1
        scb=self.seatCB.currentIndex()
        if scb!=0:
            p+=1

        if p==6:
            lot.addTicket(self.startStation,self.toStation,self.date,self.train,self.passenger,scb+4,self.isStudent)
            self.infoClear()
            self.hide()
        else:
            QMessageBox.critical(self, "标题", '<font size="30">信息错误</font>',QMessageBox.Yes)

        for i in lot.l_tickets:
            print(i.getInfo())

    def init_seatCB(self):
        self.seatCB.addItem("请选择坐席")
        self.seatCB.addItems(seatsList)

    def infoClear(self):
        #清空lineEdit和RadioButton
        self.i_from.clear()
        self.i_to.clear()
        self.i_date.clear()
        self.i_train.clear()
        self.i_passenger.clear()
        self.r_student.setChecked(False)
        self.seatCB.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = w_newTicket()
    ex.show()
    app.exit(app.exec_())


