# Функции - это именнованная часть программы 
#, которая может вызываться в других частях программы столько раз сколько нужно

# def name_of_function(<a, b> # параметры):
    # <body>
    # [<return>] оператор для возвращения результатов

# name_of_function(5, 6 #аргументы)

# Параметры функции - переменные которые будет принимать ваша функция
# для того чтобы мы смогли работать с данными
# которые попадают в нашу функцию, данные сохраняются в параметрах

#  Аргументы - это данные которые мы передаем для параметров при вызове функции

# return - оператор который нужен чтобы функция возвращала результат,
# если нет return в функции, функция по умолчанию возвращает None



# def sum_two_nums(num1, num2):
#     res = num1 +num2
#     return res
# print(sum_two_nums(5,6))
# def our_len(a):
#     try:
#         res = 0
#         for x in a:
#             res+=1
#         return res
#     except TypeError:
#         return 'value in not inerable!'

# ls = [1,2,3,4,5,6,7,8,9]
# str1 = 'Hello world! My name is John Snow!'
# print(our_len(ls))
# print(our_len(str1))
# print(our_len(True))

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     return False

# b = int(input('Vvedite chislo: '))

# print(isEven(15))
# print(isEven(b))
# print(isEven(98))


# def get_polindroms(words):
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             result.append(x)
#     return result

# some_words = ['John', 'Ono', 'kazak', 'peter', 'Dovod', 'Tenet', 'anna', 'kak', 'piko']
# polindroms = get_polindroms(some_words)
# print(polindroms)