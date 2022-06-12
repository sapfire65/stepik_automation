import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    linck = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(linck)

    # Найти картинку и взять значение элемента
    pic1 = browser.find_element(By.ID, 'treasure')
    pic1_number = pic1.get_attribute('valuex') # Получаем значение для 'x'
    result = calc(pic1_number)

    # Вводим ответ в тестовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(result)

    # находим и активируем чекбокс
    chek1 = browser.find_element(By.ID, 'robotCheckbox')
    chek1.click()

    # Находим и активируем радио-кнопку
    radio1 = browser.find_element(By.ID, 'robotsRule')
    radio1.click()

    # Находим кнопку и кликаем
    buton = browser.find_element(By.CLASS_NAME, 'btn')
    buton.click()

finally:
    time.sleep(15)
    browser.quit()
