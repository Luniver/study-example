# -*- coding: UTF-8-*- #
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
fromEle = driver.find_element_by_id('fromStationText')
    
fromEle.click()
fromEle.clear()

fromlocation = '北京\n'
fromlocation = unicode(fromlocation,"UTF-8")
fromEle.send_keys(fromlocation)