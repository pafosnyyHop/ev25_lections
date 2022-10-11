# множества в пайтоне - контейнер, который 
# содержит в себе уникальный элементы в упорядоченном виде

# {} !!!
# a = {1: 'a'} - словари
# a = {1, 2, 3} - множества

# set_ = {8, 1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7}
# print(set_)
# print(type(set_))

# ls = [1, 2, 'a', 0, False, True, 'n']
# str1 = 'My name is Jhob Snow'
# ls.extend(str1)
# # print(ls)
# # res = list(set(ls))
# # print(res)

# print(ls)
# set1 = {*ls}
# res = [*set1]
# print(set1)
# print(type(set1))
# print(res)
# print(type(res))

# FIFO / LIFO
# a = {1, 2, 3, 4, 5}
# print(a)
# a.pop()
# print(a)

# remove/diskard

# remove - error 
# discard - None
# set_ = {1, 2, 3, 4, 5, 6, 7}

# print(set_.discard(5))
# set_.remove(8)
# print(set_)

# ------------------------------------------------------------

# frozenset

# a = {1, 2, 3, 4, 5}
# f_set = frozenset([1,2,3,4,5])
# print(type(f_set))
# print(f_set)
# print(dir(f_set))


# a = set('qwerty')
# b = frozenset('qwerty')
# a.add(1)
# print(a)
# b.add(1)
# print(b)


