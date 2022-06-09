import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'trollface').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    result = calc(browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text)
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(result)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


finally:
    time.sleep(7)
    browser.quit()