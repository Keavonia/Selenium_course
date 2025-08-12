from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket(browser):

    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-add-to-basket")

    assert button.is_displayed(), "Кнопка добавления в корзину не найдена или не отображается"

    time.sleep(10)
