import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)


    # первая траница
    browser.find_element(By.CLASS_NAME, 'btn ').click()
    confirm = browser.switch_to.alert # Пререключение на окно типа confirm
    confirm.accept() # Нажимаем подтверждение

    result = calc(browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text)
    browser.find_element(By.CSS_SELECTOR, '[class="form-control"]').send_keys(result)
    browser.find_element(By.CLASS_NAME, 'btn').click()


finally:
    time.sleep(15)
    browser.quit()

    