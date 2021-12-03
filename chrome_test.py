# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import pandas as pd
driver = webdriver.Chrome()    # Chrome浏览器
driver.get("http://www.baidu.com")
driver.find_element_by_class_name("s_ipt").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)
driver.find_element_by_link_text("Selenium").click()
