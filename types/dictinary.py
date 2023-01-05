# dict() - словарь - упорядоченная коллекция элементов. (py 3.7 - ordered).
#  каждый элемент в словаре хранится в виде пары: {ключ: значение},
#  ассоциативный массив, hash tables, object(js), structire == dictionary(py)

# ключами могут выступать только неизменяемые типы данных 
# и в словаре хранятся уникальные ключи. Тогда как значениями могут выступать любые типы да

# thisdict = {
#     'brand': 'Ford',
#     'model': 'mustang',
#     'year': 1967
# }

# print(thisdict)
# print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])

# a = dict()
# b = {}

# print(type(a))
# print(type(b))

# dict_ = [('key1', 'value1'), ('key2', 'value2')]
# print(dict(dict_))

# -----------------------------------------------------

# print(dir(dict))

# keys, items, values

user_info = {
    'first_name': 'John',
    'last_name': 'snow',
    'age': 24,
    'email': 'jhonsnow@gmail.com',
    'role': 'admin'
}
# print(user_info.items())
# print()
# print(user_info.keys())
# print()
# print(user_info.values())

# for value in user_info.values():
#     print(value)

# print(user_info)
# for key, value in user_info.items():
#     print(f'key: {key}, value: {value}')

# a = list(user_info.items())
# print(a[0][0])

#  изменения элементов в словаре 

# dict_ = {'name': 'Jake', 'age': 24}

# print(dict_['name'])
# dict_['name'] = 'John'
# dict_['addres'] = 'WinterFell'
# print(dict_)
# dict_.update({'name': 'John', 'addres': 'WinterFell'})
# print(dict_)

# ------------------------------------------------------

# создание - fromkeys

# dict_ = {}
# ls = list(range(1, 101))
# new_dict = dict_.fromkeys(ls, 'value')
# print(new_dict)

# ________________________________________________________
# get

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.get(2))
# print(dict_[2])

# setdefault - работает так же как и get,
#  но если нет такого ключа, то он создает ноую пару из этого ключа

# dict_ = {'name': 'Eddard', 'last_name': 'Stark'}
# print(dict_.setdefault('age', 38))
# print(dict_)

# __________________________________________________________
# удаление элементов
#  pop, popitem

# pop(<key>) - удаляет пару по клюу



# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.pop('addres', 'такого ключа нет')
# print(dict_)
# print(removed)

# _________________________________

# popitem() - удаляет последнюю пару

# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.popitem()
# print(removed)
# print(dict_)


















































































