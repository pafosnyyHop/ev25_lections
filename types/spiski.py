# list() - (список массив) - изменяемый, последовательный тип данных,
# который представляет из себя коллекцию каких-либо обьектов(значений).

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# range() - возвращает последовательность элементов (чисел)

# ls = list(range(1, 101))
# print(ls)
# print(type(ls))

# ls1 = list(range(0, 101, 2))
# print(ls1)

# ls = list(range(1, 101))
# for num in ls:
#     # print(num ** 2 if num % 2 == 0 else num ** 3)
#     if num % 2 == 0:
#         print(f'Chislo {num} chotnoe, kvadrat: {num ** 2}')
#     else:
#         print(f'Chislo {num} ne chotnoe, kub: {num ** 3}')
# print('Finished for!')
# --------------------------------------------------------------------
# Методы списков: 

# print(dir([]))

# append(element) - Добавляет element в конец списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(5)
# ls.append([6, 7, 8])
# ls. append(True)
# print(ls)

# extend(iterable) - расширяет список элементами из iterable object

# ls = []
# # ls.append('Hello')
# # print(ls)
# ls.extend('Hello')
# print(ls)

# ls = [1, 2, 3]
# ls.append([4, 5, 6])
# print(ls)
# ls.extend([4, 5, 6])
# print(ls)

# insert(<index>, <element>) - Добавляет элемент по указаному index

# ls = ['string', 2, 3, False]
# ls.insert(1, 4)
# ls.insert(-1, True)
# print(ls)

# index(element, [start], [end]) - Возвращает index элемента в списке.

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John']
# # res = ls.index('name')
# # print(ls[res])

# print(ls[0: 2])
# print(ls[-1][0])

# count(element) - Возвращает кол-во вхождений element в списке

# ls = [1, 2, 3, 4, 5, 6, 5, 5, 5]
# res = ls.count(5)
# print(res)

# ls = ['Hello', 'World', 'my', 'name', 'is', 'John', 'north', 'king', 'queen', 'USA']
# print(ls)
# str1 = input('Введите слово: ')

# if str1 in ls:
#     print(f'"{str1}" есть в списке и его индекс: {ls.index(str1)}')
# else:
#     print('No!')

# sort() - сортирует список, если в аргументах передать reverse=True,
#  то список будет отсортирован в убывающем порядке

# import random

# ls = []
# for x in range(0, 50):
#     ls.append(random.randint(0, 1000))

# print(ls)
# ls.sort(reverse=True)
# print()
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'apple', 'Aikol', 'mekers']

# ls.sort(key=len)
# print(ls)

# remove(element) - удаляет element из списка, если такого нет, то выводится ошибка
# pop([index]) - удаляет и возвращает элемент по index, но если index не указан, то удаляет последний элемент

# ls = [5, 1, 2, 4, 5, 5, 5]
# # ls.remove(5)
# print(ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)

# ls = [5, 1, 2, 4, 5, 5, 5, 99]
# deleted = ls.pop(0)
# print(ls)
# print(deleted)
# ls.pop()
# print(ls)

# update ------------------------------------
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)

# ls = ['Helloworld!']
# print (list(ls[0][(len(ls[0]) + 1) // 2:] + ls[0][:(len(ls[0]) + 1) // 2]))

# list_ = ['world', 'hello'] 
# new_list = sorted(list_)
# print(list_, new_list)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = [nums for nums in nums if nums < 5]
# print (res)














