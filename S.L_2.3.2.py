import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

url = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
