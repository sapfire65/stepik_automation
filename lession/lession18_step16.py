import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()


    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    text_n = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[id="price"]'), '$100'))

    browser.find_element(By.CSS_SELECTOR, '[id="book"]').click()

    result = calc(browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text)
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '[id="solve"]').click()


finally:
    time.sleep(5)
    browser.quit()