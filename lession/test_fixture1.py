import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
link1 = 'http://ya.ru/'


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(3)
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope='function')
def print_messeg():
    print('  << БАСНЯ')
    print('Мартышка и очки')

# class TestMainPage1():
#
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         print("start test1")
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#         print("finish test1")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         print("start test2")
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#         print("finish test2")

class TestMainPageYandex():

    def test_super_text(self, print_messeg):
        print('\nМартышка к старости слаба глазами стала .....\n')
