import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    linck = 'http://suninjuly.github.io/selects2.html'
    browser.get(linck)

    # Находим два значения и их сумму
    num1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]').text
    num2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]').text
    result = str(int(num1) + int(num2))
    print(result)

    # Нахрдим и раскрываем список Select
    select = Select(browser.find_element(By.ID, "dropdown"))

    # Находим вариант с текстом найденной суммы 'result'
    select.select_by_value(result)

    # Нажимаем кнопку
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    time.sleep(15)
    browser.quit()