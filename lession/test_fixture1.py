import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

final = ''
count = 0

@pytest.fixture(scope='function')
def browser():
    global count
    count += 1
    print(f'\nТест №{count}')
    # Отключаю отображение браузера
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    browser = webdriver.Chrome(options=options)
    # browser.minimize_window()
    browser.implicitly_wait(10) # неявное ожидание
    yield browser
    time.sleep(2)
    browser.quit()

@pytest.mark.parametrize('number_list', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905' ])
def test_open_link(browser, number_list):
    global final # Указываю глобальную переменную
    answer = math.log(int(time.time()))
    link = f'https://stepik.org/lesson/{number_list}/step/1'
    browser.get(link)
    browser.find_element(By.XPATH, '//textarea[@autocapitalize="none"]').send_keys(answer)
    browser.find_element(By.XPATH, '//button[@class="submit-submission"]').click()
    text = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text
    # assert 'Correct!' == text, f'Ожидаемое значение <Correct!>, фактическое значение <<{text}>>'

    try:
        assert 'Correct!' == text, f'Ожидаемое значение <Correct!>, фактическое значение <<{text}>>'
    except AssertionError:
        final += text  # собираю ответ каждой ошибки

def test_final_text():
    print(f'\n\nПредложение: {final}')





