
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

exe_path = './chromedriver'
service = Service(executable_path=exe_path)
browser = webdriver.Chrome(service=service)

try:
    browser.get('https://www.baidu.com/')
    time.sleep(5)
    baidu_input_tag = browser.find_element_by_id('kw')
    key = baidu_input_tag.send_keys('google')

    baidu_button_tag = browser.find_element_by_id('su')
    baidu_button_tag.click()

finally:
    time.sleep(5)
    browser.close()

