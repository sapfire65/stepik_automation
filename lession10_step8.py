import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Получение значения 'x'
    s_result = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = s_result.text
    y = calc(x)

    # Находим поле ввода и вводим полученные данные
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(y)

    # Поиск чек бокса и нажатие
    bocks1 = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    bocks1.click()

    # Поиск радио кнопки и клик по нужной
    radio1 = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    radio1.click()

    # Находим кнопку и нажимаем
    buton = browser.find_element(By.CLASS_NAME, 'btn')
    buton.click()

finally:
    time.sleep(15)
    browser.quit()
