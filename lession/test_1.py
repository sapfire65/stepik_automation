import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Тестируем две разные страницы с формой регистрации

class MyTestCase(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'label + input[placeholder="Input your first name"]')
        input1.send_keys('Alexandr')

        input2 = browser.find_element(By.CSS_SELECTOR, 'label + input[placeholder="Input your last name"]')
        input2.send_keys('Tcherenkov')

        input3 = browser.find_element(By.CSS_SELECTOR, 'label + input[placeholder="Input your email"]')
        input3.send_keys('sansani4@yandex.ru')

        # Отправляем заполненную форму
        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")  # add assertion here

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'label + input[placeholder="Input your first name"]')
        input1.send_keys('Alexandr')

        input2 = browser.find_element(By.CSS_SELECTOR, 'label + input[placeholder="Input your last name"]')
        input2.send_keys('Tcherenkov')

        input3 = browser.find_element(By.CSS_SELECTOR, 'label + input[placeholder="Input your email"]')
        input3.send_keys('sansani4@yandex.ru')

        # Отправляем заполненную форму
        button = browser.find_element(By.CLASS_NAME, "btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")  # add assertion here


if __name__ == '__main__':
    unittest.main()

