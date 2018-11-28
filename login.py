from selenium import webdriver
from selenium.webdriver.common.by import By # 定位
from selenium.webdriver.support.ui import WebDriverWait #显性等待库
import time
from w_login import User

def login(driver):
#    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
#自动输入账号密码
    driver.find_element_by_xpath('//*[@class="login-hd-account"]/a').click()
    driver.find_element_by_xpath('//*[@id="J-userName"]').send_keys(User[0])
    driver.find_element_by_xpath('//*[@id="J-password"]').send_keys(User[1])
    return driver

#driver = webdriver.Chrome()
#login(driver)
