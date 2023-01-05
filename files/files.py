# file1 = open('makers.txt', 'r')
# print(file1.read())

"""
r - read
r+ - read + write
w - write
w+ - read + write
a - append
a+ - append + read
x - write если файла нет, но если есть генерирует исключение
b - binary открытие файла в двоичном режиме
t - text
rt -> r
rb -> rb

r - только для чтения.

w - только для записи, создаст новый файл, если не найдет файл с указанным именем.

r+ - для чтения и записи.

w+ - для чтения и записи, создаст новый файл для записи, если не найдет с указанным именем.

a - откроет для добавления нового содержимого, создаст новый файл для записи, если не найдет с указанным именем.
"""

# file1 = open('makers.txt', 'r')
# print(file1.read(10))
# file1.seek(0)
# print(file1.read(5))
# print(file1.read(10))
# data = file1.read()
# print(data)
# seek

# -------------------------------

# file1 = open('makers.txt', 'r')
# list_ = file1.readlines()
# print(file1.readline())
# print(file1.readline())
# list_ = [line.replace('\n', '') for line in list_]
# # for line in list_:
# #     print(line)
# print(list_)
# for line in file1:
#     print(line)

# -------------------------------

# file2 = open('bootcamp.txt', 'w')
# file2.write('Its such a beautiful day today\n')
# file2.write('Today is my birthday\n')
# list_mottos = ['Taste the Rainbow', 'Red Bull Gives You Wings', "Maybe She’s Born With it, Maybe it’s Maybelline"]
# list_mottos = [motto + '\n' for motto in list_mottos]
# file2.writelines(list_mottos)

# ------------------------------

# file3 = open('files.txt', 'a')
# list_mottos = ['Taste the Rainbow', 'Red Bull Gives You Wings', "Maybe She’s Born With it, Maybe it’s Maybelline"]
# list_mottos = [motto + '\n' for motto in list_mottos]

# file3.write('Mottos of big commpanies' + '\n')
# for motoo in list_mottos:
#     file3.write(motoo)

# file3.close()
# print(file3.closed)

# --------------------------

# with - автоматически закрывает файл при окончании работы с ним

# with open('files.txt', 'r+') as my_file:
#     print(my_file.read())
#     my_file.write('Additional string\n')
# # my_file.write('HelloWorld') # ошибка
# print(my_file.closed)

# ---------------------------------

# Модули 
# math, random, datatime, itertools
# import math

# from math import * -> импортирует абсолютно все функции

# from math import pi as P
# print(P)
# as - alias

# import square
# print(square.circle(5))

# from square import circle, triangle, rectangle

# circle_erea = circle(8)
# rtiangle_area = triangle(9, 6)


# Работа с файлами
# каретка -указатель -курсор
# open (<путь до файла>)
# file=open('/home/darika/Desktop/ev.py/files/lections/files.py') -абсолютный путь
# file =open('files.py') - относительный путь(относительно той директории в которой мы находимся)
#_-------------------------------------------
# режимы работы сфайлами
# 1 чтение r/r+(read)
# 2 записи w/w+(write)
# 3 добавление a/a+(append)
# b x t
# file =open('test.txt', 'r')
# data=file.read()
# data =data.split('\n')
# print(data)
# print(len(data))
# file.close()
# контекстный менеджер(with)-можно не закрывать
# with open('test.txt') as file:
#     print(file.tell())
#     data = file.read()
#     index = data.index('My')
#     print(file.tell())
#     file.seek(index)
#     print(file.read())
#     print(file.tell())
# file.tell()-возвращает индекс где находится коретка
# file.seek(<index>)-перемещает коретку на index котрый вы передали
    
    

# ___________________________________________________________________


    #  открыть как переменную
# with open('test.txt','r') as file:
#     print(file.readlines())
#     file.seek(0)
#     print(file.readline())
#print(file.read())#Value Erorr т.к файл закрыт
# with open('test.txt' ,'a+') as f:
#     f.write('\nHe is bastard of Ned Stark ')
#     f.write('\nThis is lection')
#     f.seek(0)
#     print(f.read())
   
    
# with open('test.txt','w') as file:
#     file.write('Hello, file was opened with open')
#--------------------------------------
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re
# def get_imei_codes(image):
#     string = pytesseract.image_to_string(image)
# # print(string)
#     list_of_imei = re.findall(r'IME.\d.\s\d+',string)
#     print(list_of_imei)
#     with open('imei_codes.txt','w') as file:
#         for x in list_of_imei:
#             file.write(f'{x}\n')
# ls ='lections/imei.jpg'
# get_imei_codes(ls)

