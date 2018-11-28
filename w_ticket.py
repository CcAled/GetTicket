
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from tickets import Tickets, lot
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)
import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QCoreApplication
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from login import login
from search import  fillInfo

timer = QtCore.QTimer()

class myLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, k):
        super().__init__()
        self.n = k
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()
    def showData(self):
        print(self.n)
        if len(lot.l_tickets) > 0:
            if self.n < len(lot.l_tickets):
                timer.stop()
                reply = QMessageBox.information(self,"标题",'<font size="30">确定要删除该订单吗？</font>',QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    del lot.l_tickets[self.n]
                timer.start(1000)#重新启动timer，定时刷新

class w_ticket(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        self.setWindowTitle("订单")
        self.setGeometry(300, 300, 500, 300)

        self.info = myLabel(0)
        self.info.setText("  出发站    终点站        时间       车次    乘客名   坐席  学生票  ")
        self.info.setMaximumHeight(50)
        self.info.setStyleSheet("font:15pt;border:1px solid black")
        grid.addWidget(self.info, 0, 1)

        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setSpacing(0)
        self.labels = [myLabel(0), myLabel(1), myLabel(2), myLabel(3), myLabel(4), myLabel(5)]
        for i in range(6):
            self.labels[i].setText("  ")
            self.vlayout.addWidget(self.labels[i])
            self.labels[i].clicked.connect(self.labels[i].showData)
            self.labels[i].setMinimumHeight(40)
            self.labels[i].setMinimumWidth(400)
            self.labels[i].setStyleSheet('font:70pt;background-color:white')
        vwg = QtWidgets.QWidget()
        vwg.setLayout(self.vlayout)
        grid.addWidget(vwg, 1, 1)

        self.b_addTickets = QPushButton()
        self.b_addTickets.setText("添加订单")
        self.b_addTickets.setFixedSize(60, 30)
        self.b_startBuying = QPushButton()
        self.b_startBuying.setText("开始抢票")
        self.b_startBuying.setFixedSize(60, 30)
        self.l_deleteTickts = myLabel(0)
        self.l_deleteTickts.setText("单击订单可以删除该订单\n 当前只显示前六个订单")
        self.l_deleteTickts.setMaximumWidth(150)
        self.l_deleteTickts.setStyleSheet("border:1px solid black")

        self.hlayout = QtWidgets.QHBoxLayout()
        #        self.hlayout.setSpacing(0)
#        self.hlayout.addWidget(self.l_deleteTickts)
        self.hlayout.addWidget(self.b_addTickets)
        self.hlayout.addWidget(self.b_startBuying)
        hwg = QtWidgets.QWidget()
        hwg.setLayout(self.hlayout)
        grid.addWidget(hwg, 2, 1)
        grid.addWidget(self.l_deleteTickts, 3, 1, 1, 1)

        #每3秒刷新一次车票信息
        #timer要定义在外面，在弹出messageBox后停止，否则messageBox在刷新时会出错
        timer.timeout.connect(self.setLText)
        timer.start(1000)

        self.b_startBuying.clicked.connect(self.startBuying)

    def setLText(self):
        print("111")
        for j in self.labels:
            j.setText("  ")
            j.setStyleSheet("border:0px;background-color:white")
        if len(lot.l_tickets)>6:
            a=6
        else:
            a=len(lot.l_tickets)
        for i in range(a):#只显示前6个订单
            self.labels[i].setText("  ".join(str(c) for c in lot.l_tickets[i].getInfo()))
            self.labels[i].setStyleSheet("font:20pt;border:1px solid black;background-color:white")
            QtWidgets.QApplication.processEvents() #更新页面

    def startBuying(self):
        driver=webdriver.Chrome()
        driver.get('https://kyfw.12306.cn/otn/resources/login.html')
        login(driver)
        WebDriverWait(driver,1000).until(EC.url_to_be("https://kyfw.12306.cn/otn/view/index.html"))
        print("Successfully login!")
        fillInfo(driver)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = w_ticket()
    ex.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())





