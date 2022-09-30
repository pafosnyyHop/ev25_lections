# string - строки

"hello"
'hello'

"""
hello
world
my name is
"""

# строки - это набор последоватетльных символов которые мы исползуем 
# для хранения и предоставления текстовой информации. набор методов и 
# операций которые мы можем использрвать с данными в виде текстаю. 

# индексация в строке
# name = 'abu'
# #         a = 0 = -3
# #         b = 1 = -2
# #         u = 2 = -1

# print(name)
# print(name[1])
# print(name[-1])

# a = 'crit'
# print(a[1], a[2], a[3])
# print(a[-3], a[-2], a[-1])

# срезы по индексам
# [start:end:<step>]
# a = 'birthday'
# b = a[0:5]
# print(b)
# print(a[5:8])
# print(len(a))
# print(a[5:]) #до конца
# print(a[:5])

# text = 'hello world! My name is abu! I\'m North King!'
# print(text)
# print(len(text))

# # print(text[:12])
# # print(text[13:28])
# # print(text[29:])

# # print(text[:12:2])
# # print(text[::2])
# # print(text[::-1]) перевернет текст
# print(text[:12:-1])

# конкатенация строк(слияние, соединение)

# word1 = 'Hello'
# word2 = 'world'
# probel = ' '

# result = word1 + probel + word2
# print(result)

# форматирование строк
# 1. с помощью %
# 2. с помощью .format()
# 3. интерполяция строк (f-строки)

# %
# name = input('Enter yot name: ')
# last_name = input('enter your last name: ')
# print('Hello, My name is', name, last_name)
# print('Hello, My name is' + ' ' + name + ' ' + last_name)
# print('Hello, my name is %s %s' %(name, last_name))

# .format
# name = input('Enter yot name: ')
# last_name = input('Enter your last name: ')

# print('Hello, My name is {} {}'.format(name, last_name))

# f - строки
# name = input('Enter yot name: ')
# last_name = input('Enter your last name: ')

# print(f'Hello, My name is {name} {last_name}')

# Экранирование строк -мехфнизм при помощи которого 
# можно вставлять символы, которые сложно ввести с клавиатуры в строку
# \n - перенос строки
# \t - горизонтальная табуляция
# \v - вертикальная табуляция

# name = 'Abu\nAboba'
# lastName = '\vAboba'
# last_Name = '\tAboba'

# print(name)
# print(lastName)
# print(last_Name)

# заменяет выбранные данные на другие

# string = 'The quick brown fox jumps over the lazy dog'
# res = string.replace('o', '*')
# print(res)
# перевод в верхний регистр 

# string = 'Hello'
# res = string.upper()
# print(res)

# переводит в нижний регистр

# string = 'HELLO'
# res = string.lower()
# print(res)




















