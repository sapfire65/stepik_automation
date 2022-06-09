import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    linck = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(linck)

    radio1 = browser.find_element(By.ID, 'peopleRule')

    people_checked = radio1.get_attribute("checked") # Проверяем присутствие атрибута "checked"
    print("value of people radio: ", radio1)
    assert people_checked == "true", "People radio is not selected by default"


    radio2 = browser.find_element(By.ID, 'robotsRule')

    robots_checked = radio2.get_attribute('checked')
    assert robots_checked is None # Если в переменной есть значение атрибута None, всё впорядке.
    # (print('Не активна') if str(robots_checked) == 'None' else print('Активна'))

    buton1 = browser.find_element(By.CLASS_NAME, 'btn')
    buton1_check = buton1.get_attribute('disabled')
    assert buton1_check is None












finally:
    time.sleep(15)
    browser.quit()
