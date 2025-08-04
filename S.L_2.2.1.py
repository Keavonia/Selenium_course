import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

url = 'http://suninjuly.github.io/selects1.html'

def calc(x,y):
    return str(int(x) + int(y))

try:
    browser = webdriver.Chrome()
    browser.get(url)

    valx = browser.find_element(By.ID, 'num1')
    x = valx.text
    valy = browser.find_element(By.ID, 'num2')
    y = valy.text
    z = calc(x,y)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(z)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(5)
    browser.quit()
