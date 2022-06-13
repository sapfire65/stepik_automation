import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/"

@pytest.fixture()
def target_stepik():
    print('\nЭто сообщение повторяется каждый раз, после запуска фикстуры')
    target_stepik = webdriver.Chrome()
    yield target_stepik
    print('<< Браузер закрыт')
    time.sleep(5)
    target_stepik.quit()

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр 'target_stepik'
    def test_number_1(self, target_stepik):
        target_stepik.get(link)
        target_stepik.find_element(By.CSS_SELECTOR, '[class="navbar"] [aria-label="Search"]').send_keys('Автоматизация Selenium')

    def test_number_2(self, target_stepik):
        target_stepik.get(link)
        target_stepik.find_element(By.CSS_SELECTOR, '[id="ember248"]').click()







