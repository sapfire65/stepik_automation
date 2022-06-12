import time

from selenium import webdriver
from selenium.webdriver.common.by import By


import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    result = calc(browser.find_element(By.ID, 'input_value').text)
    print(result)
    browser.execute_script("window.scrollBy(0, 150);")

    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]').click()
    browser.find_element(By.CLASS_NAME, 'btn').click()


finally:
    time.sleep(15)
    browser.quit()