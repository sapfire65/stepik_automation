import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.google.com/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск поля ввода
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[class="gLFyf gsfi"]')
    input1.send_keys('привет мир я тут')

    button = browser.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@class="gNO89b"][@name="btnK"]')

    button.click()

    # рандомно кликаем на выдачу гугла
    #
    num = random.randrange(4, 10)
    print(num)
    click_random = browser.find_element(By.XPATH, '(//div[@class ="yuRUbf"]/a/h3)["num"]')
    click_random.click()





finally:
    time.sleep(15)
        # закрываем браузер после всех манипуляций
    browser.quit()





# закрываем браузер после всех манипуляций


