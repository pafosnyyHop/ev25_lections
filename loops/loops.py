# Циклы- это конструкция при помощи которых можно
#  организовать многократное исполнение определенного кода

# while <expression>: 
#     <body>
# <else>:
#     <body>

# i = 1
#     while i <= 10:
#         print(f'цикл выполнился {i} раз!')
#         i += 1
#     else:
#         print('Конец цикла!')

#     print('Начало кода!')

# new_func(i)

# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('Vvedite imya1: ')
#     name2 = input('Vvedite imya2: ')
#     i += 1
#     if i > 4:
#         print('Цикл остановлен!!')
#         break
# else:
#     print('Vi vveli pravilnoe imya!')

# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# username = None
# password = None

# while username != admin[0] or password != admin[1]:
#     username = input('Vvedite username: ')
#     password = input('Vvedite parol: ')
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany na 5 minut!')
#         break
# else:
#     print(f'{admin[0]} vy uspeshno zashli v sistemu!')

# for <variable> in <iterable object>:
#     <body>

# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for x in list_:
#     print(x)

# ---------------------------------
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # for x in ls:
# #     print(f'Element: {x}')

# i = 0
# while i < len(ls):
#     print(f'Element: {ls[i]}')
#     i += 1

# -------------------------------------

# secret_list = ['DeltaViski', 'LOTOR123', 'JohnSnow']
# word = input('Vvedite secret kod: ')

# while word not in secret_list:
#     print('Incorect word! Try one more time!')
#     word = input('Vvedite secred kod: ')

# print(f'You\'re welcome my friend, {word}')

# ------------------------------------------------------
# 1)
# step = 8
# path = 'UDDDUDUU'
# res = 1

# 2)
# steps = 11
# path = 'UDDUUDDUUDU'

# s,c=0,0
# for i in range(len(path)):
#     if path[i]=='U':
#         s+=1
#     else:
#         s-=1
#     if s==-1 and path[i+1]=='U':
#         c+=1
# print(c)

# ----------------------------------------
# range(start, stop, [step]) - возвращает последовательность 
# из целых чисел начиная с start до stop, возвращает итерируемый тип данных renge
    
x = range(1, 10)
print(list(x))
# print (x)
# for num in x:
#     print(num) 







