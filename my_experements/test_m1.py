import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://yandex.ru"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    # Узнаем путь к корневой папке с файлом
    p = os.path.abspath('db_frends.txt ')
    print(p)
    # Проверяем наличие файла
    if os.path.exists(p):
        print("Файл db_frends.txt найден")
    else:
        print("Файл db_frends.txt не найден, и будет создан")
        db_frends = open("db_frends.txt", "w+")


    amount_elements = len(browser.find_elements_by_xpath('//span[@class="news__item-content"]')) # Получаю количество элементов
    print(f'Найденно элементов: {amount_elements}')

    for i in range(1, amount_elements + 1):
        info = browser.find_element(By.XPATH, f'(//span[@class="news__item-content"])[{i}]').text  # поиск элементов
        print(info)

    # db_frends = open("db_frends.txt", "a+")
    # db_frends.close()


finally:
    time.sleep(5)

    browser.quit()
























