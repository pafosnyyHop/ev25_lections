
# Наример:
# Name: Maya Angelou
# Name: Chimamanda Ngozi Adichie
# Name: Tobias Wolff
# Name: Sherman Alexie
# Name: Jane Austen
# Результат:
# ['Adichie', 'Alexie', 'Angelou', 'Austen', 'Wolff']


# names = []
# for x in range(0, 5):
#     name = input('Vvedite FIO: ')
#     names.append(name)

# result = []
# for x in names:
#     x = x.split(' ')
#     result.append(x[-1])

# result.sort()
# print(result)

# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = 3

# list1 = []
# list2 = []
# list3 = []
# for x in range(0, len(list_), n):
#     list1.append(list_[x])
#     list2.append(list_[x+1])
#     if x + 2 >= len(list_):
#         continue
#     list3.append(list_[x+2])

# res = [list1, list2, list3]
# print(res)

# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# step = 3

# res = []
# for i in range(step):
#     list_q = []
#     for x in range(i, len(list_), step):
#         list_q.append(list_[x])
#     res.append(list_q)
#     list_q = []
# print(res)


#  Создайте список с 3 вложенными списками списками, где внутри должно быть три 0
# Результат:
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# res = []

# for x in range(0, 3):
#     ls = []
#     for x in range(0, 3):
#         ls.append(0)
#     res.append(ls)

# print(res)

# Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
# Например:
# list_ = [1, 2, 3]
# Результат:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# from itertools import permutations

# res = list(permutations([1, 2, 3], 3))
# for x in res:
#     print(x) 






