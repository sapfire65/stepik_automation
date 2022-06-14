import pytest
import time
from selenium import webdriver


@pytest.fixture()
def autch():
    print(f'\n-== ПРОВЕРКА: ==- ')
    oll = webdriver.Chrome()
    oll.implicitly_wait(7) # Не явное ожидание прогрузки каждого элемента на странице
    yield oll
    print('<< Браузер закрыт')
    time.sleep(5)
    oll.quit()

