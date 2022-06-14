import pytest
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.linkedin.com/'

class TestLoginPass():
    def test_cklick_button_accept_quke(self, autch):
        autch.get(link)

        autch.find_element(By.CSS_SELECTOR, '[action-type="ACCEPT"]').click()
        time.sleep(1)
        autch.execute_script("alert('Ожидание авторизации пользователя');") # Сообщение для пользователя
        time.sleep(5)
        alert = autch.switch_to.alert
        alert.accept()

        autch.find_element(By.XPATH, '//input[@autocomplete="username"]').click()





