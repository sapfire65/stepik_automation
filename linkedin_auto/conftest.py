import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def autch():
    print(f'\n-== СТАРТ: ==- ')
    oll = webdriver.Chrome()
    oll.implicitly_wait(30) # Не явное ожидание прогрузки каждого элемента на странице

    yield oll
    print('<< Браузер закрыт')
    time.sleep(5000)
    oll.quit()





