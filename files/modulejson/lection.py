# JSON - JavaScript Pbject Notation
# единый формат, хранения и передачи данных между компьютерамиб сервисамиб приложениями и языками програмирования через сеть интернет
# <filename>.json # файл в формате json

# {
#     "id": 1,
#     "author": "Ed Sherran",
#     "title": "Perfect",
#     "year": 2015
    #   "hit": true
# } -- это json

# наша заача научиться переводить данные JSON в Pthon Dcitionary

# !!!!
# JS object == {key: value}
# PY dict == {key: value}
# JSON == {key: value}

# процессы сериализации и десериализации данных
# Сереализация (запись данных в JSON) - это перевод из Python в JSON  формат

# dump -> метод записывает Python данные в формате JSON, параллельно сделав сериализацию 
# dumps -> метод записывает Python данные в текст в формате JSON, параллельно сделав сериализацию 

# Десериализация (чтение данных из JSON) - это рпоцесс перевода из JSONa в PY 

# load - метод который считывает файл в формате JSON и переводит его в PY dict
# loads - метод который считывает текст в формате JSON и переводит его в PY dict

# --------------------------------
# процесс сериализации 

# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_)
# print(type(dict_))

# json_text = json.dumps(dict_)
# print()
# print(json_text)
# print(type(json_text))

# -------------------------------------

# import json

# dict_ = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True,
#     'wife': False,
#     'children': None
# }
# print(dict_)
# print(type(dict_))

# with open('new.json', 'w') as file:
#     json.dump(dict_,file)

# with open('new.json', 'r') as file:
#     data = file.read()
#     print()
#     print(data)

# ------------------------------------
# Процесс десериализации
# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data)
# dict_ = json.loads(json_data)
# print(dict_)
# print(type(dict_))

# import json

# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_))

# ---------------------------
#  import urlopen
# import json

# url = 'https://randomuser.me/api/'
# json_data = urlopen(url)

# # print(json_data)
# # print(type(json_data))

# dict_ = json.load(json_data)
# print(dict_)
# print(type(dict_))
# from urllib.request import urlopen
# import json

# url = 'https://randomuser.me/api/'
# json_data = urlopen(url)

# # print(json_data)
# # print(type(json_data))

# dict_ = json.load(json_data)
# print(dict_)
# print(type(dict_))