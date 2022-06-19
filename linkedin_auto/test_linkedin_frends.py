import pytest
import time
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.linkedin.com/'
login = 'cherenkova-iylia@mail.ru'
password = 'Iy1ia123'

login1 = 'sapfiretrey@gmail.com'
password1 = '!K153ON34rus!'

try:
    def test_cklick_button_accept_quke(autch):
        # Открываю ссылку в браузере
        autch.get(link)
        try:
            #  | нахожу кнопку | кликаю по кнопке согласия
            button_accept = WebDriverWait(autch, 60).until(EC.element_to_be_clickable((By.XPATH, '[action-type="ACCEPT"]')))
        except:
            pass

        autch.find_element(By.XPATH, '//input[@autocomplete="username"]').send_keys(login1)
        autch.find_element(By.XPATH, '//input[@autocomplete="current-password"]').send_keys(password1)
        autch.find_element(By.XPATH, '//button[@class="sign-in-form__submit-button"]').click()


        # Явное ожидание элемента после авторизации. Свернуть чат.
        button_chat = WebDriverWait(autch, 120).until(EC.element_to_be_clickable(
            (By.XPATH, '(//div[@class="msg-overlay-bubble-header__controls display-flex"]/button)[2]')))
        button_chat.click()


        # находим раздел с контактами
        autch.find_element(By.XPATH, '(//nav[@class="global-nav__nav"]//li)[2]').click()
        autch.find_element(By.XPATH, '(//div[@class="mn-community-summary__sub-section artdeco-dropdown__item"])[1]').click()

        # # Получаю значение с общим количеством контактов
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

        # Узнаем путь к корневой папке с файлом
        p = os.path.abspath('db_frends.txt ')
        print(p)
        # Проверяем наличие файла db_frends.txt
        if os.path.exists(p):
            print("Файл db_frends.txt найден")
            with open("db_frends.txt") as file:
                text = file.readline()
                file.close()
                if len(text) != 0:
                    print('Файл не пустой')
                else:
                    os.remove("db_frends.txt")
                    print('Пустой файл был удален')



        else:
            print("Файл db_frends.txt не найден, и будет создан")
            db_frends = open("db_frends.txt", "w+")

            # Скролим страницу пока не будет видно все контакты.
            # Условие цикла: скролить вниз, пока на странице не перестанет обнаруживатся кнопака в футере.
            # Пока список не кончится.
            amount_elements = 0

            for i in range(0, friends_list + 1):
                # Проверка наличия следующего элемента. Если он есть, скролить и проверять на наличие кнопки в футере списка.
                # Получаю первый элемент
                amount_elements = len(autch.find_elements_by_xpath(f'(//a[@class="ember-view mn-connection-card__picture"])[{i}]'))

                # Если элемент найден и равен одному экземпляру, скролить на 50 пикселей вниз
                if amount_elements == 1:
                    autch.execute_script('window.scrollBy(0, 50);')
                    try:
                        button_load_more = WebDriverWait(autch, 5).until(
                                EC.element_to_be_clickable((By.XPATH, '//div[@class="display-flex p5"]')))
                        button_load_more.click()
                    except:
                        break

            # Получаем общее количество найденых объектов
            amount_elements = len(autch.find_elements_by_xpath('(//a[@class="ember-view mn-connection-card__picture"])'))
            print(f'Найденно {amount_elements} контактов.')

            # Получаем ссылку на профиль и добавляем в файл db_frends.txt
            for i in range(1, amount_elements + 1):
                autch.find_element(By.XPATH, '//a[@class="ember-view mn-connection-card__picture"]')
                friends_link = WebDriverWait(autch, 10).until(EC.visibility_of_element_located(
                        (By.XPATH, f'(//a[@class="ember-view mn-connection-card__picture"])[{i}]'))).get_attribute('href')

                db_frends = open("db_frends.txt", "a+")
                db_frends.write(f'{friends_link}\n')
                db_frends.close()
            print('*' * 30, end='\n\n')





finally:
    pass








