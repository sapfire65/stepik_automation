import os
import re


# Узнаем путь к корневой папке с файлом
p = os.path.abspath('db_frends.txt ')
print(p)
# Проверяем наличие файла db_frends.txt
if os.path.exists(p):
    print("Файл db_frends.txt найден")


else:
    print("Файл db_frends.txt не найден, и будет создан")
    db_frends = open("db_frends.txt", "w+")
    db_frends.close()

# db_frends = open('db_frends.txt', 'r+')
# db_frends.seek(0) # Указатель начала файла

# начинаем читать построчно
# print(db_frends.readline())

# with open('db_frends.txt', 'r+') as file:
#     print(file.readlines())
#     # file.write("test")


# with open("db_frends.txt", 'r+') as file:
#     for db_frends in file:
#         print(db_frends, end='')

with open("db_frends.txt") as file:
    a = file.readline()
    print(a)






























