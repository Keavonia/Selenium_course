import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

url = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Kolodin")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ik@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    option1 = browser.find_element(By.CSS_SELECTOR, "#file")
    option1.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
