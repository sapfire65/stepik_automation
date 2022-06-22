import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

final = ''
count = 0

@pytest.fixture(scope='function')
def browser():
    global count
    count += 1

    print(f'\nТест №{count}')
    browser = webdriver.Chrome()
    browser.implicitly_wait(10) # неявное ожидание
    yield browser
    time.sleep(2)
    browser.quit()

@pytest.mark.parametrize('number_list', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905' ])
def test_open_linc(browser, number_list):
    global final # Указываю глобальную переменную
    answer = math.log(int(time.time()))
    link = f'https://stepik.org/lesson/{number_list}/step/1'
    browser.get(link)
    browser.find_element(By.XPATH, '//textarea[@autocapitalize="none"]').send_keys(answer)
    browser.find_element(By.XPATH, '//button[@class="submit-submission"]').click()
    text = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text
    assert 'Correct!' == text, f'Ожидаемое значение <Correct!>, фактическое значение <<{text}>>'
    try:
        pass
    except AssertionError:
        final += text  # собираю ответ каждой ошибки

def text_bad_tests_text():
    global final
    print()
    print(f'Предложение: \n\n{final}')
















# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")

