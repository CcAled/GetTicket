
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)
from tickets import Tickets
import sys
from w_ticket import w_ticket,lot
from w_newTicket import w_newTicket
from w_login import w_login,User

app = QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
lg = w_login()
lg.setupUi(MainWindow)

tc = w_ticket()
nt = w_newTicket()

def loginEvent():
    tc.show()
#    lg.close()
#    lg.showMinimized()

def newTicketEvent():
    nt.getTicketInfo()
#    nt.hide()

#lg.pushButton.clicked.connect(loginEvent)
lg.pushButton.clicked.connect(tc.show)
tc.b_addTickets.clicked.connect(nt.show)
#nt.b_finish.clicked.connect(newTicketEvent)
nt.b_finish.clicked.connect(nt.getTicketInfo)
nt.b_cancel.clicked.connect(nt.cancel)

if __name__ == "__main__":
    MainWindow.show()
    app.aboutToQuit.connect(app.deleteLater)

    app.exit(app.exec_())

