# Типы данных -> числа int(), float()
# -------------------------------------------------------------------------------------------------------
# text = input ( 'Что делаем (+ ; - ; / ; * )?: ')

# a = float ( input ( 'Введите первое число: '))
# b = float ( input ( 'Введите второе число: '))

# if text == '+' : 
#     c = a + b 
#     print ('Ответ:' + str(c))

# elif text == '-' :
#     c = a - b
#     print ('Ответ:' + str(c))

# elif text == '/' :
#     c = a / b 
#     print ('Ответ:' + str(c)) 

# elif text == '*' :
#     c = a * b
#     print('Ответ:' + str(c))

# else :
#     print('Выбрана неправильная операция!!!')
# ----------------------------------------------------------------------------------------------------------
#  / - обычное деление
#  // - деление без остатка
#  % - остаток от деления

# ** - возведение в степень

# a = 1
# while a < 10 :
#     print (' цикл выполнился', a , 'раз(а)' )
#     a = a + 1
# print(' цикл окончен')

# pow(a , b, <mod>) - функция возведения числа а в степень b

# print(pow(5, 2, 10))  5 ** 2 % 10 

# divmod(a, b) - она выводит 2 числа , первое число это результат целочисленного деления (//), а второе число это модульное деление(%) двух чисел
# res = divmod(4, 5)
# print(res)

# round() - функция округления числа
# res = 24 / 13
# print(round(res, 2))

# abs() - фбсолютное значение abs(-5) = 5 -> |-5| = 5

# print(abs(-101))
# print(abs(50))

# import math

# print(math.pi)
# math.sqrt - корень числа 
# print(math.sqrt(25))
# print(math.sqrt(6))

# from math import pi, sqrt
# print(pi) 
# print(sqrt(45))

# dir() - возвращает методы обьекта или функции определенного модуля 

# import math
# print (dir(math))

# множественное присваивание

# v = 5
# n = 7
# d = 3

# v, n, d = d, v, n

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print (num1,num2)

# print('hello' * 3) дублирование строк 

# str1 = '12'
# num = 2

# print = (str1 + str(num))

# инкремент и дикремент

# инкремент - увеличение значения какой-либо переменной (а = 1 -> a += 1 -> a = a+1)

# a = 0
# a += 1
# print(a)

# дикремент - уменьшение значения какой-либо переменной. (a -= 1 -> a = a - 1)

# a = 0
# a -= 1
# print (a)

# a = 5
# a *= a
# print (a)

# a = 10
# a /= 2
# print(a)

# id() - номер в ячейке памяти

# a = 1
# b = a 
# print(id(a))
# print(id(b))

# type() - выводит тип заданной переменной
# a = 9
# d = 'hel'
# print (type(a), type(d))

# var = float(input(''))

# a = int(input('введите число: '))
# b = int(input('введите степень: '))
# c = a ** b

# print(c)

#  модуль random  -  предоставляет функции для генерации случайных чисел, букв, символы

# import random

# print(dir(random))

# num = random.randint(11111, 99999)
# print(num)

# from random import choice
# import string

# # print(string.ascii_letters)
# a = choice(string.ascii_letters)
# print(a)

# import math

# class krug():
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius**2)
#     def perimeter(self):
#         return 2 * math.pi * self.radius
 
# r = int(input("Введите радиус круга: "))
# obj = krug(r)
# print("Площадь круга:", round(obj.area(), 2))
# print("Длина окружности:", round(obj.perimeter(), 2))

# from math import pi

# r = int(input('Ввудите радиус: '))
# p = 2 * r * pi
# s = pi * (r ** 2)
# print( 's =', round(s))
# print('p =', round(p))

