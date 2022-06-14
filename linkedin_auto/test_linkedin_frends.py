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
        # Открываю ссылку в браузере | нахожу кнопку | кликаю по кнопке согласия
        autch.get(link)
        autch.find_element(By.CSS_SELECTOR, '[action-type="ACCEPT"]').click()
        time.sleep(1)
        # Вызываю аллерт с информацией
        autch.execute_script("alert('Ожидание авторизации пользователя');") # Сообщение для пользователя
        time.sleep(3)
        alert = autch.switch_to.alert
        alert.accept()
        # Ставлю курсор в поле ввода E-mail
        autch.find_element(By.XPATH, '//input[@autocomplete="username"]').click()

        # Явное ожидание элемента после авторизации.
        button_chat = WebDriverWait(autch, 60).until(EC.element_to_be_clickable((By.XPATH, '//li-icon[@class="artdeco-button__icon"][@type="chevron-down-icon"]')))
        button_chat.click()

        # находим раздел с контактами
        autch.find_element(By.XPATH, '(//li/a[@class="app-aware-link global-nav__primary-link"])[1]').click()
        autch.find_element(By.XPATH, '(//div[@class="mn-community-summary__sub-section artdeco-dropdown__item"])[1]').click()










