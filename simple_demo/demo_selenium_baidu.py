
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
exe_path = os.path.join(script_dir, '../chromedriver')

## initialize, executable_path arg removed from webdriver, use service and options
service = Service(executable_path = exe_path)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service = service, options = options)

## 10 seconds timeout
wait = WebDriverWait(browser, 10)

try:
    browser.get('https://www.baidu.com/')

    ## wait 5s to load the page
    time.sleep(5)

    ## type in 'google'
    baidu_input_tag = browser.find_element(By.CSS_SELECTOR,'#kw')
    key = baidu_input_tag.send_keys('google')

    ## click search button
    baidu_button_tag = browser.find_element(By.CSS_SELECTOR,'#su')
    baidu_button_tag.click()

    ## wait for 10s observe results
    time.sleep(10)

finally:
    ## end session
    browser.quit()


## this can delay until the webpage is loaded to the state of capable of sending keys
# baidu_input_tag = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '#kw'))
#     )
