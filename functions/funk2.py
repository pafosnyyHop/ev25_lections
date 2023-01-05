# def sum_of_args(a, b, c, d): # параметры
#     return a + b + c + d

# result = sum_of_args(1, 2, 3, 4)
# print(result)

# -----------------------------------
# Дефолтные параметры(default params)

# def print_hello(name='Guest'):
#     print(f'Welcome {name}!')

# print_hello()

# def introduce(name, last_name, work=None):
#     print(f'The Users name is {name}')
#     print(f'The Users last_name is {last_name}')
#     if work:
#         print(f'The Users work is {work}')

# introduce('John', 'Snow')
# print()
# introduce('Larry', 'Page', 'Police officer')

# --------------------------------------------
# позиционные и именнованые аргументы

# def printParams(a = None, b = None, c = None):
#     print(a, 'is stored in a')
#     print(b, 'is stored in b')
#     print(c, 'is stored in c')

# printParams(1 , 2)
# printParams(b = 2, a = 1, c = 3)

# -----------------------------------------------

# оператор *

# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)

# ----------------------------------------------
# *args, **kwargs в функциях
# args = arguments( позиционные аргументы)
# kwargs = keywords arguments (именнованные аргуmенты)

# def printScores(students, *args):
#     print(f'Student name: {students}!')
#     # print(args)
#     # print(type(args))
#     for x in args:
#         print(f'Score: {x}')
# printScores('John', 90, 100, 85, 62, 75)

# def print_pet_names(owner, **pets):
#     print('Owner name:', owner)
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')


# print_pet_names('John Snow', wolf='Ghost', dog = 'Rex', fish=['Nemo', 'Dori', 'Alex'], turtle = 'Mbappe')


# def get_some_data(a, b, *args, **kwargs):
#     print('параметры:', a, b)
#     print('Arguments:', args)
#     print('Kwargs:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs.keys())

# get_some_data(1,2,3,4,5,6,7,8,9, language = 'Python', name = 'John Snow', car = 'BMW 7 series')

# -----------------------------------------------------------------------------------------------

# def generate_random_string(len_):
#     import string as s
#     import random
#     random_string = ''.join(
#         random.choice(s.ascii_letters + s.digits ) for i in range(0, len_)
#     )
#     return random_string

# print(generate_random_string(50))

# --------------------------------------------------------------------------

# def add(a, b): return a + b

# def subtract(a, b): return a - b

# def multiply(a, b): return a * b

# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'
# def calc(num1, num2):
#     operator = input('Ввeдите ператор (+, -, *, /): ')
#     if operator == '+': return add(num1, num2)
#     elif operator == '-': return subtract(num1, num2)
#     elif operator == '*': return multiply(num1, num2)
#     elif operator == '/': return divide(num1, num2)
#     else: return 'Вы ввeли неправильный оператор!'

# def main():
#     try:
#         num1 = input('Ввeдите первое число: ')
#         num1 = float(num1) if '.' in num1 else int(num1)
#         num2 = input('Ввeдите второе число: ')
#         num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('Вы ввели некоректные данные!')
#         main()

#     while True:    
#         result = calc(num1, num2) 
#         if type(result) == str:   
#             print(f'Error: {result}')  
#         else:
#             print(f'Result: {round(result,2)}')
#             break

#     question = input('Хотите продолжить?(Yes/No): ')
#     if question.lower().strip() == 'yes':
#         main()
#     else:
#         print('Bye Bye!')

# main()

# --------------------------------------------

# lambda
# map()
# filter()
# enumerate()
# zip()
# all(), any()

# Анонимные функции - lambda(обычные функции с одной особенностью, у них нет имён)

# lambda функции могут принимать сколько угодно параметров,
# но всегда возвращают одно выражение

# def hello(): return 'hello'

# print(hello())

# x = lambda: 'hello'
# print(x())

# ------------------------------------

# x = lambda a, b, c: a * b % c
# print(x(5, 5, 2))

# x = lambda num1, num2, degree = None: (num1 * num2) ** degree if degree else num1 * num2
# print(x(2,2,3))
# print(x(5, 5))

# def myFunc(n): return lambda num: num * n

# my_doubler = myFunc(2)
# my_tripler = myFunc(3)

# print(my_doubler(50))
# print(my_doubler(150))
# print(my_doubler(500))
# print(my_tripler(1000))
# print(my_tripler(4000))

# dict_ = {'John': 500, 'Tirion': 170_000, 'Tom': 150, 'Sanzhar': 20}
# new_dict = sorted(dict_.items(), key=lambda x: x[1], reverse= True)
# print(dict(new_dict))

# -------------------------------------------------------------------

# map(function, iterable) - применяет к каждому элементу внутри iterable функцию которую  мы ей передаем, закидывая в результат те данные которые возвращает функция, в результате мы получим mapobject(iterator) в котором хранятся все наши данные

# Hапример, с помощью  map можно преобразовать все элемнтры внутри списка. Перевести все строки в верхний регистр.

# ls = ['one', 'two', 'three', 'four', 'five']
# new_ls = list(map(str.capitalize, ls))
# print(new_ls)

# names = ['John', 'Aokol', 'Aizirek', 'Nurayim', 'Sanzhar']

# # def chage_str(name):
# #     result = f'Hello, mr/mrs {name}'
# #     return result

# new_ls = list(map(lambda x: f'Hello, mr/mrs {x}', names))
# print(new_ls)

# dict_ = {1:2, 3:4, 5:6}
# list_ = dict(map(lambda x: (x[0],str(x[1])), dict_.items()))

# print(list_)

# ------------------------------------------------------------

# filter(function, iterable) - применяет ко всем элементам iterable функцию которую мы передали и возвращает iterableobject(итератор) только с теми элементами, для которых функция вернула True

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ls = ['one', 'two', '3', '', '1', '100', 'john99']
# res = list(filter(str.isdigit, ls))
# print(res)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# ls = ['John', 'one', 'two', 'list', 'makers', 'ev.25', 'fanta']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)

# ----------------------------------------------------------------

# enumerate(iterable) - она пронумеровывает каждый элемент внутри iterable, ее собственным индексом

# ls = ['str1', 'str2', 'str3']

# x = dict(enumerate(ls))

# print(x)

# for i, x in enumerate(ls):
#     print(f'index: {i}, Element: {x}')

# --------------------------------------

# zip (iterables) - она соединет каждый элемент итерируемых элементов между собой, соединет в тип данных tuple() и возвращает его

# ls1 = [1,2,3]
# ls2 = [100,200,300]
# result = list(zip(ls1, ls2))
# print(result)

# zip - для создания словарей
# x = [(1, 2), (3, 4)]
# dict_ = dict(x)
# print(dict_)

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# d_values = ['castle_r1', 'winterfell', 'Starks', 'Cisco R1', '10.255.101.10']

# res = dict(zip(d_keys, d_values))
# print(res)


# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'r1': ['london_r1', '21 New Globe Walk', 'Cisco', 'DYR-25', '10.255.101.10'] , 
#     'r2':['london_r2', 'Greenwith', 'Cisco', 'pir-21', '98.255.101.11'] , 
#     'sw2': ['london_sw2', 'Mercyside', 'Cisco', '3850', '101.255.20.10']

# }

# res = {}
# for key in data:
#     res[key] = dict(zip(d_keys, data[key]))

# print(res)

# -------------------------------------------
# all(), any()

# all(iterable) - Bозвращает True, если все элементы внутри iterable имеют значение True, иначе False


# ls = [[5,6], '5', 'stroka', True, 1]
# print(all(ls))

# ip = '10.255.1y.108'
# ip1 = '10.255.18.108'
# ip2 = '118.20.101.108'

# res = all(i.isdigit() for i in ip.split('.'))
# res1 = all(i.isdigit() for i in ip1.split('.'))
# res2 = all(i.isdigit() for i in ip2.split('.'))
# print(res)
# print(res1)
# print(res2)

# any - возвращает True, если хотябы 1 из элементов дает True 


# ls = [0, 0, [], (), '', [1,2]]
# print(any(ls))


# ignor = ['rm -rf', 'reset', 'chmot']
# command = input('Vvedite comandu: ')


# if any(word in command for word in ignor):
#     raise Exception('Invalid command!')
    
# else:
#     print('vse ok!')




































