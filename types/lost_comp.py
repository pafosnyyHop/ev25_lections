# list comprehensions - генератор списков

# list comprehension - это упрощенный подход к созданию списков,
#  который задействует в себе цикл for,
#  а так же конструкцию if для определения того,
#  что в итоге окажется добавлено в наш список. 

# list - 0-200 - num % 2 == 0

# ls = []
# for x in range(0, 201):
#     if x % 2 == 0:
#         ls.append(x)
# ls1 = []
# for x in range(0,201,2):
#     ls1.append(x)
# print(ls)
# print()
# print(ls1)


# ls = [x for x in range(0,201) if x % 2 == 0]
# print(ls)

# ls1 = [x for x in range(0,201,2)]
# print()
# print(ls1)

# ls =: 0 - 300 - x % 2 == 0 and x % 3 == 0


# ls = []
# for x in range(0,300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)
# print()
# ls = [x for x in range(0,300) if x % 2 == 0 and x % 3 == 0]
# print(ls)

# list 0 - 100 - x % 2 == 0: x ** 2, x % 3 == 0 : x ** 3

# ls = []
# for x in range(0, 101):
#     if x % 2 ==0:
#         ls.append(x**2)
#     elif x % 3 == 0:
#         ls.append(x**3)
# print(ls)

# ls = [x**2 if x % 2 == 0 else x**3 for x in range(0, 101) if x % 2 == 0 or x % 3 == 0]

# print(ls)


# ----------------------------------------------------------------------------------

# newlist = [expression for item in iterable <if condition == True>]


# ls = [i ** 2 for i in range(0, 11)]
# print(ls)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# # result= [1,2,3,4,5,6,7,8,9]

# res =[]
# for x in ls:
#     for item in x:
#         res.append(item)

# for inner in ls:
#     res.extend(inner)
# print(res)


# ls = [[1,2,3], [4,5,6], [7,8,9]]

# res =[x for inner in ls for x in inner ]
# print(res)

# -----------------------------------------------

# from datetime import datetime
# start = datetime.now()

# ls = [x for x in range(0, 100_000_000)]
# # for x in range(0, 100_000_000):
# #     ls.append(x)
# finish = datetime.now()
# print(finish - start)

# ------------------------------------------------

# dict comprehension

# dict_ ={
#     'key1': 'value1',
#     'key2': 'value2'
# }

# dict_ = {x: x**2 for x in range(1,15)}

# print(dict_)

# names = ['jhon', 'tirion', 'sansa', 'eygan', 'sansa', 'ramsi']

# dict_ = {name: names.index(name) for name in names}

# print(dict_)


# dict1 = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4,
#     'e': 5, 'f': 6, 'g': 7, 'h': 8
# }
# print(dict1)
# print()
# res = {}
# for k,v in dict1.items():
#     if v % 2 == 0:
#         res[k] = 'четное'
#     else:
#         res[k] = 'нечетное'
# print(res)

# res = {k: 'четное' if v % 2 == 0 else 'нечетное' for k, v in dict1.items()}
# print(res)


