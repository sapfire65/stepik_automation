import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link2 = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    # Открываем ссылку
    browser.get(link2)
    link_code = str(math.ceil(math.pow(math.pi, math.e)*10000))
    oppen_linc = browser.find_element(By.PARTIAL_LINK_TEXT, link_code)
    oppen_linc.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(30) # Ждем 30 секунд
    browser.quit() # Закрываем браузер







