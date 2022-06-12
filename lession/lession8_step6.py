from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.XPATH, '')
    for element in elements:
        element.send_keys("Мой ответ")
    print('Заполнение полей завершено')

    button = browser.find_element(By.CLASS_NAME, 'btn')
    print('Кликаем')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла