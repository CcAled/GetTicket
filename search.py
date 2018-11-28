from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #期望的条件
from selenium.webdriver.common.by import By
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from tickets import  *

#Ticket类中的变量
'''
fr='北京'
to='成都'
iTime=[2018,12,19]#输入的日期
isStudent=0
'''
tInfo=lot.l_tickets[0].getInfo()
fr=tInfo[0]
to=tInfo[1]
iTime=tInfo[2].split('-')
tn=tInfo[3]
pg=tInfo[4]
st=tInfo[5]
isStudent=tInfo[6]

#成员变量
fT="fromStationText"
tT="toStationText"

def clickStation(driver,te,station):#填写车站 点击下拉框选择
    driver.find_element_by_id(te).click()
    driver.find_element_by_id(te).send_keys(station)
    table = driver.find_element_by_id('panel_cities')
    table_rows = table.find_elements_by_tag_name('div')
    for i in range(len(table_rows)):
        a=table_rows[i].find_elements_by_tag_name('span')[0]
        if station==a.text:
#            print("YES")
            b=i
    table = driver.find_element_by_id('panel_cities')
    table_rows = table.find_elements_by_tag_name('div')
    table_rows[b].find_elements_by_tag_name('span')[0].click()

def fillStations(driver):#填写出发和到达站
    clickStation(driver,fT,fr)
    clickStation(driver,tT,to)

#选择日期  农历日历cal-wrap
def chooseTime(driver):
    driver.find_element_by_id("train_date").click()
    if iTime[1]!=QDateTime.currentDateTime().toString("MM"):#当前的月份
        driver.find_element_by_xpath('//*[@class="cal cal-right"]/div[1]/a[2]').click()#下个月
    dx='//*[@class="cal-cm"]/div['+iTime[2]+']/div'#选择哪一天的xpath
    driver.find_element_by_xpath(dx).click()#选择日期
    if isStudent==1:
        driver.find_element_by_id("sf2").click()
    driver.find_element_by_xpath('//*[@class="btn-area"]/a').click()#点击查询

def fillInfo(driver):#填写车票信息
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
    print(tInfo)
    fillStations(driver)
    chooseTime(driver)


#driver = webdriver.Chrome()
#fillInfo(driver)
