import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Александр')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Черенков')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('cot65@yandex.ru')

    # Загрузка файла
    link_to_files = os.path.abspath(os.path.dirname(__file__)) # Получаем путь к файлу.py
    file_path = os.path.join(link_to_files, 'file.txt') # Указываем путь к своему файлу
    browser.find_element(By.ID, 'file').send_keys(file_path) # Загружаем файл

    browser.find_element(By.CLASS_NAME, 'btn').click()



finally:
    time.sleep(15)