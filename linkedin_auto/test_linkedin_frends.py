import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.linkedin.com/'

try:
    def test_cklick_button_accept_quke(autch):
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

        # Получаю стоку с общим количеством контактов
        friends_list = autch.find_element(By.CSS_SELECTOR, 'h1[class="t-18 t-black t-normal"]').text
        # Очищаем текст
        number = []
        for i in friends_list:
            if i.isdigit():
                number.append((int(i)))
        b = " ".join(map(str, number))
        for i in b:
            friends_list = b.replace(' ', '')
        friends_list = int(friends_list) # Перевел в int

        print()
        print('*'*30)
        print(f'Всего контактов: {friends_list}')

        # Узнаем путь к корневой папке с файлом
        p = os.path.abspath('db_frends.txt ')
        print(p)
        # Проверяем наличие файла db_frends.txt
        if os.path.exists(p):
            print("Файл db_frends.txt найден")

        else:
            print("Файл db_frends.txt не найден, и будет создан")
            db_frends = open("db_frends.txt", "w+")

            # Скролим страницу пока не будет видно все контакты.
            amount_elements = 0  # Получаю количество элементов c линками на профили.

            # Условие цикла: скролить вниз, пока на странице не будет всего списка контактов.
            while (friends_list - 9) != amount_elements:
                autch.execute_script('window.scrollBy(0, 500);')
                amount_elements = len(autch.find_elements_by_xpath('(//a[@class="ember-view mn-connection-card__picture"])'))

                button_load_more = WebDriverWait(autch, 60).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@class="display-flex p5"]')))
                button_load_more.click()


            # Получаем ссылку на профиль и добавляем в файл db_frends.txt
            for i in range(1, amount_elements + 1):
                # autch.find_element(By.XPATH, '//a[@class="ember-view mn-connection-card__picture"]')
                friends_link = WebDriverWait(autch, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, f'(//a[@class="ember-view mn-connection-card__picture"])[{i}]'))).get_attribute('href')
                db_frends = open("db_frends.txt", "a+")
                db_frends.write(f'\n{friends_link}')
            db_frends.close()

            print(f'Найденно элементов: {amount_elements}')
            print('*' * 30, end='\n\n')












finally:
    pass









