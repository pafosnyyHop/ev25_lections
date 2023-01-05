# Наример:
# Name: Maya Angelou
# Name: Chimamanda Ngozi Adichie
# Name: Tobias Wolff
# Name: Sherman Alexie
# Name: Jane Austen
# Результат:
# ['Adichie', 'Alexie', 'Angelou', 'Austen', 'Wolff']


# a = input('Введите имя и фамилию: ').split()[-1]
# b = input('Введите имя и фамилию: ')
# c = input('Введите имя и фамилию: ')
# d = input('Введите имя и фамилию: ')
# i = input('Введите имя и фамилию: ')

# a = list(map(lambda x: input('Введите имя и фамилию: ').split()[-1], range(5)))

# print(sorted(a))


# lists = [10, 'abcd', 3, 2.5, 4, 'xyz', 2, 'pqr', 8, -6, -17.35]
# sum = 0
# for x in lists:
#     if type(x) == int or type(x) == float:
#         sum += x
# print(sum)

# str_list = ['abc', 'xyz', 'aba', '1221']
# for x in str_list:
#     if x[0] == x[-1]:
#         indexs = str_list.index(x) 
#         print(list([indexs]))

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# a = max(lists)
# b = min(lists)
# print(f' Max_list {a} \n Min_list {b}')

# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# a = input('Хочу найти слово начинающееся на букву: ')

# res = list(filter(lambda x: x.startswith(a), list_))
# print(res)
    # res = [idx for idx in test_list if idx[ 0 ].lower() = = check.lower()]

# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]

# c = []

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]

# a = []
# for x in list1:
#     if a == 1:
#         continue
#     for i in list2:
#         if x != i:
#             a.append(False)
#             break
# print(a)
            
        # else:
        #     print(False)
        #     break


# str_list = ['abc', 'xyz', 'aba', '1221']
# a = []
# for x in str_list:
#     if x[0] == x[-1]:
#         indexs =str_list.index(x)
#         a.append(indexs)

# print(a)

# -----------------------------------------

# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# b = []

# for x in list_:
#     if x in b:
#         continue
#     if list_.count(x) > 1:
#         b.append(x)
# print(b)

                
            


# for x in list1:
#     for i in list2:
#         if x != i:
#             print(False)
#             break

        

# a = []
# b = a.append(list(range(1, 4)))

# flag = True
# while flag:
#     a.append(list(range(1, 4)))
#     if len(a) >= 3:
#        flag = False
# print(a)

# list_ = ['world', 'hello'] 
# a = list_.reverse()
# new_list = list_

# print(new_list)

# a = input()

# list_ = a.split(',')
# tuple_ = tuple(a.split(','))
# print(list_)
# print(tuple_)

# list_ =  [1, 2, 3, 4, 5]
# new_list = []
# for x in list_:
#     if x % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
        
# print(new_list)

# list_ = []
# for x in range(0, 20):
#     list_.append(x)
# print(list_)

# list_ = []
# for x in range(0,101):
#     if x % 2 == 0:
#         list_.append(x)
# print(list_)

# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# res = list1 + list2
# print(sum(res))

# a = input().split(',')
# res = a.sort(key = str)

# print(a)

# a =[1,2,3]
# if len(set(a)) == len(a):
#     print("ERROR")
# else:
#     print("YES")

# list_ = []
# for x in range(54, 9184):
#     if x % 5 == 0:
#         list_.append(x)
# print(list_)

# 


# for i in range(1, 10):
#     i -= 5
# print(i)
       
    
# a = input().split()[-1]
# b = input().split()[-1]
# c = input().split()[-1]
# d = input().split()[-1]
# i = input().split()[-1]

# result =[]
# result.append(a)
# result.append(b)
# result.append(c)
# result.append(d)
# result.append(i)
# result.sort()
# print(result)

# for k in names:
#     k = k.split(' ')
#     result.append(k[-1])
# result.sort()
# print(result)

# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# res =[]
# for x in colors:
#     res.append(x[::-1])
#     res.sort(key=len)

# print(res)

# --------------------------------------------------------------------------------------

# lists = [[433, 746, 243, 432], [645, 45, 343, 76], [123, 463], [432, 54, 65, 76, 98]]

# res = []
# for x in lists:
#     res.append(sum(x))
    
# print(max(res))

# ------------------------------------------

# a = {'x': 1, 'y': 2, 'z': 1}
# res = a.keys()
# print(list(res))


# ------------------------------

# a = {'a': 1, 'b': 2, 'c': 1}
# for x,z in a.items():
#     print(z)

# -----------------------------------------------

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 

# b = a.copy()
# for k,v in list(a.items()):
#     if v % 2 == 0:
#         b[k] = 2
# print(b)
    
# ----------------------------------------------------

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# for k, v in list(a.items()):     
#     if type(v) != int and type(v) != str:         
#         del a[k]  
# print(a) 
    
# ----------------------------------------------------------

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 

# for k, v in list(a.items()):
#     a[k] = v / 5    
# print(a)

#------------------------------------------------------ 

# a = {'apple': 2, 'orange': 5, 'banana': 10} 

# for k, v in list(a.items()):     
#     if v % 2 == 0:         
#         del a[k]  
# print(a) 

# ________________________________

# a = {'a': 1, 'b': 2, 'c': 3} 

# a = {v: k for k, v in a.items()}

# print(a)

# -----------------------------------------

# a = {'a': 3, 'b': 2}

# res =[]
# for k, v in list(a.items()):
#     res.append(v)
# print(sum(res))

# --------------------------------------------

# a1 = {
#   "move": "water",
#   "eat": "insects",
#   "say": None
# }
# print(a1)

# a2 = dict(
#     eat= 'leaves', 
#     move= 'ground', 
#     say= None
# )
# print(a2)

# a3 =dict([
#     ('move', 'ground'),
#     ('eat', 'grass'),
#     ('say', 'moo')
# ])
# print(a3)

# ---------------------------------

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# res =[]
# for k, v in list(dict_.items()):
#     res.append(v)
# print(min(res))

# ----------------------------------

# dict1 = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 

# dict2 = dict1.copy()
# for k,v in list(dict1.items()):
#     if v % 2 != 0:
#         dict2[k] = 1
# print(dict2)

# ----------------------------------------------------

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# for k, v in list(a.items()):     
#     if type(v) == int or type(v) == str:         
#         del a[k]  
# print(a) 

# -----------------------------------------------------

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}

# dict2 = {v: k for k, v in dict1.items()}

# for k, v in list(dict2.items()):
#     dict2[k] = v ** 2   

# dict2 = {v: k for k, v in dict2.items()}

# print(dict2)

# -----------------------------------------------------

# months = {
#     1:'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May',
#     6: 'June',
#     7: 'July',
#     8: 'August',
#     9: 'September',
#     10: 'October',
#     11: 'November',
#     12: 'December'
# }

# while True:
#     number = input('Vvedite nomer mesyaca: ')
#     if number == 'john':
#         break

#     if not number.isdigit():
#         print('Trebuetsya vvesni realniy nomer mesyaca!')
#         continue
#     number = int(number)
#     if number not in range(1,13):
#         print('Trebuetsya vvesni realniy nomer mesyaca!')
#         continue

    # if number in range(3,6):
    #     print(f'Vi rodilis v {months[number]}. Birds pely prekrasnie pesny.')
    # elif number in range(6,9):
    #     print(f'Vi rodilis v {months[number]}. Solnce svetilo yarche chem kogda libo')
    # elif number in range(9,12):
    #     print(f'Vi rodilis v {months[number]}. Urojay bil neveroyatny.')
    # else: 
    #     print(f'Vi rodelis v {months[number]}. Za oknom padal bely sneg. ')


# ------------------------------------------------------------------------------

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for x in tuples:
#     if len(x) != 0:
#         cleared_tuples.append(x)
# print(cleared_tuples)

# ____________________________________________________________________________________

# lists = [10, 'abcd', 3, 2.5, 4, 'xyz', 2, 'pqr', 8, -6, -17.35]
# sum = 0
# for x in lists:
#     if type(x) == int or type(x) == float:
#         sum += x
# print(sum)

# -------------------------------------------------------------------------------

# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for x in list_:
#     dict_.setdefault(x, len(x))
# print(dict_)

# --------------------------------------------------------

# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}

# for k, v in list(dict1.items()):
#     dict2.setdefault(k, v ** 3)

# print(dict2)

# ---------------------------------------------------------

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}

# for k, v in list(dict_.items()):
#     for x, i in list(v.items()):
#         dict_[k] = v.pop(x)
# print(dict_)

# ------------------------------------------------------

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = int(input())

# if key in list(dict_.keys()):
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")

# --------------------------------------------------

# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {}

# for k, v in dict1.items():
#     dict4[k] = v
# for k, v in dict2.items():
#     dict4[k] = v
# for k, v in dict3.items():
#     dict4[k] = v

# print(dict4)

# ---------------------------------------------------------

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = dict(zip(list1, list2))
# print(dict_)

# -------------------------------------------------------------------

# dict_ = {'math': {'sum': sum},'vars': {'a': 5,'b': 20,'c': 50}}
# res = 0
# a =[]
# for v in dict_.values():
    

    # for x, i in v.items():
    #     print(i)
    #     if type(i) == int:
    #         a.append(i)

# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }
# print(dict_['math']['sum'](dict_['vars'].values()))
# a =[]

# for v in dict_.values():
#     for x, i in v.items():
#         if type(i) == int:
#             a.append(i)

# print(dict_['math']['sum'](a))

        

        

        
            
        
        

# ----------------------------------------------------------------------

# a = {'a': 10, 'b': 9, 'c': 3}
# res = 1
# for k, v in a.items():
#     res *= v

# print(res)

# ------------------------------------------------------------------

# string = "pythonist"
# dict_ = {}

# for x in string:
#     dict_.setdefault(x, string.count(x))
# print(dict_)

# _____________________________________________________________________________________________

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {x: j for x in list_ if type(x) == str for j in list_ if type(j) == int }

# print(dict_)

# for x in list_:
#     if type(x) == str:
#         dict_.setdefault(x,)
# for k, v in dict_.items():
#     for x in list_:
#         if type(x) == int:
#           dict_[k] = x

          
# print(dict_)

# a = {0, 1, 2, 3, 34, 5, 8, 13}
# b = {1, 2, 34}

# if a > b:
#     print('Надмножество')

# ----------------------------------------------------------

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}


# if robert.intersection(kail) and robert.intersection(merri):
#     print('kail merry')
# elif robert.intersection(kail) and not robert.intersection(merri):
#     print('kail')
# elif robert.intersection(merri) and not robert.intersection(kail):
#     print('merri')
# else:
#     print('no one')

# --------------------------------------------------------------------

# tilek ={'Dodo', "ImperiaPizza", "FreshBox"}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"FreshBox", 'KFC'}
# elina = {'Dodo', "ImperiaPizza", "FreshBox", "OchakKebab", 'KFC'}

# print(elina.intersection(tilek,timur,alexander))

# ---------------------------------------------------------------------


# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}

# for k,v in dict_.items():
#     if dict_[k] > dict_[k]:
#         print(k)




# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# res =1

# for key, in_dict in dict1.items():
#     for val in in_dict.values():
#         res*=val
#     print(res)
#     res = 1


# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {k: dict_[k] for k in sorted(dict_, key=dict_.get, reverse=True)}
# sorted_values = sorted(dict_.values())
# for i in sorted_values:

#     for k in dict_.keys():

#         if dict_[k] == i:

#             sorted_dict[k] = dict_[k]

#             break

 

# print(sorted_dict)

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add('помидор')
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.discard("cыр чеддар")
# ingredients.add('сыр моцарелла')
# print(ingredients)
    
# ----------------------------------------------------

# set1 ={x for x in range(0,10) if x % 2 == 0}
# set2 = {x for x in range(0,10) if x % 2 != 0}

# if set1.intersection(set2):
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')


# --------------------------------------------------

# list_ = [True if x % 2 == 0 else False for x in range (1,11)]

# print(list_)

# -------------------------------------------------------------

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(x) <= 4 else 'longer' for x in list_name]

# print(new_list)

# ----------------------------------------------------------------

# n = int(input())
# dict_ = {x: x**2 for x in range(1, 501) if n == x or x % n == 0}

# print(dict_)

# -----------------------------------------------------------------

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: list(range(1,v+1)) for k, v in a.items()}
# print(dict_)

# -----------------------------------------------------------

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [s for s in str.split(string_) if s.isdigit()]
# print(list_)

# ---------------------------------------------------------

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k: i for k, v in my_dict.items() for j, i in v.items()}

# print(dict_)

# ----------------------------------------------------------

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# a ={k: max(v, key= v.get) for k, v in dict_.items()}

# print(a)

# ---------------------------------------------------------

# dict_ = {2: 'apple', 5: 'orang', 6: 'banana'} 

# new_dict = {k: len(v) if k % 2 ==0  else len(v)**3 for k, v in dict_.items()}

# print(new_dict)

# --------------------------------------------------------




# set1 ={x for x in range(1,11)}
# set2 ={x for x in range(8,18)}

# # set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# # set2 = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     res = len(set1.intersection(set2))
#     print(f"В этом сете было {res} повторения, его длина составляет {len(full_set)}")
# else:
#     print("Ваш объединенный сет полностью уникальный!")



# --------------------------------------------------------------------


# try:
#     age = int(input())
#     if age < 18:
#         raise Exception('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# -------------------------------------------------

# inp1 = input().split()
# list_ = []

# try:
#     for x in inp1:
#         list_.append(int(x))
# except:
#     raise ValueError('Данный элемент не является числом!')

# __________________________________________________________

# try:
#     age = int(input())
#     if age < 18:
#         raise Exception('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
#     raise

# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')
        
# ---------------------------------------------

# num = 3
# def check(num):
#     if num % 2 != 0:
#         return "It is even number"
#     else:
#         return "It is odd number"

# print(check(num))

# -------------------------------------------------

# def is_palindrome(words):
#     if words.lower().split() == words[::-1].lower().split():
#         return True
#     else:
#         return False

# print(is_palindrome('Mom'))

# -------------------------------

# def sum_digits(a):
#     res = 0
#     for x in list(a):
#         res += int(a)
#     return res
# print(sum_digits(105))

# ---------------------------

# def sum_digits(a):
#     list_=[]
#     list_.extend(str(a))
#     res = 0
#     for x in list_:
#         res += int(x)
#     return res
# print(sum_digits(105))


# def func(a = 5, b = 6, **args):
#     print(args)
# func(a = 1, b = 2, c = 3)

# --------------------------------------------

# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     x = 'Я могу изменяться'


# print(x)
# my_func()
# print(x)
# print(globals())

# ----------------------------------------

# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
#     def bar():
#         global var
#         var = 'переменная bar'
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# ---------------------------------------

# num = 3
# def mul():
#     global num
#     num *= num

# mul()
# mul()
# mul()
# print(num)

# -----------------------------------------

# balance = 0

# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f"Вы заплатили {amount} сом за {log_name}")

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# ---------------------------------------------------------

# result = 0

# def pow_first(x,y):
#     global result
#     result = x ** y

# def pow_second(z):
#     global result
#     result = result % z

# pow_first(2, 3)
# pow_second(3)
# print(result)

# ---------------------------------

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control():
#     global a
#     for k, v in a.items():
#         if v >= 17:
#             print(f"{k}, Вы можете войти в клуб")
#         else:
#             print(f'{k}, извините, Вы не проходите по age-control')

# age_control()

# ---------------------------------------------------------------------

# a = ['pipi', 'papa', 'mama']
# b = []
# def title_list():
#     global b
#     for x in a:
#         b.append(x.title())

# title_list()
# print(b)

# ---------------------------------


# a = [
#     'й', 'у', 'е', 'ы', 
#     'а', 'о', 'э', 'я', 
#     'и', 'ю', 'ё'
#     ]
# b = [
#     'ц', 'к', 'н', 'г', 'ш', 'С', 'Ж',
#     'щ', 'з', 'х', 'ф', 'в', 'Т',
#     'п', 'р', 'л', 'д', 'ж', 'П',
#     'ч', 'с', 'м', 'т', 'б', 'М'
# ]
# def count_symbols(str_):
#     c = []
#     d = []
#     i = []
#     for x in str_:
#         if x in a:
#             c.append(x)
#         elif x in b:
#             d.append(x)
#         else:
#             i.append(x)
#     return f'Количество гласных: {len(c)}, согласных: {len(d)}, остальных символов: {len(i)}'

# print(count_symbols('Мурат супер!'))

# ---------------------------------------------------------------------

# a = []

# def rangage():
#     global a
#     for x in range(0, 11):
#         a.append(x)

# rangage()
# print(

# ------------------------------

# list_ = [1, 5, -9, 6, -4] 

# result = all(int > 3 for int in list_)

# print(result)

# --------------------------------

# list_ = [5, 8, 4, 6, 7]
# result = any(int < 0 for int in list_ )
# print(result)

# ---------------------------------------

# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x**2, list_))
# print(result)

# ------------------------------------------

# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x % 2 == 0, list_))
# print(result)

# --------------------------------------------------

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)

# ------------------------------------------------------------------

# list_ = [5, 6, 7, 8] 
# import functools 
# result = functools.reduce(lambda x, y: x * y, list_) 
# print(result)

# -----------------------------------------------------

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = len(list(filter(lambda x: x % 2 == 0, list_)))
# list3 = len(list(filter(lambda x: x % 2 != 0, list_)))
# result = f'even {list2}, odd: {list3}'
# print(result)

# ------------------------------------------------------

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: False if x <= 0 else True , list_))
# print(result)

# ---------------------------------------------------------------

# import functools 
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = functools.reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)

# --------------------------------------------------------------------------

# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# for x in range(len(list_)):
#   if list_[x] < 0:
#     list_[x] = False
#   else:
#     list_[x] = True

# print(list_)

# -------------------------

# list_ = [x for x in range(1,25) if x % 2 == 0]
# print(list_)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = list(map(lambda x: 1 if x < 0 else x, list_))
# print(int_list)

# ----------------------------------------------------------

# list_ = [False, True, False, True, False, True, False, True, False, True] 
# list1 = [1 if x == True else 0 for x in list_ ]
# print(list1)

# --------------------------------------------------------
# from string import ascii_letters
# string = "happy birthday!"
# list_ = [x for x in string if x in ascii_letters]
# print(list_)

# --------------------------------------------------

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list_ = [v for x in dict_.values() for v in x.values()]
# print(list_)

# ---------------------------------------------------

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# res = {k: len(k)**2 for k in list_name if len(k) > 4 }
# print(res)

# -----------------------------------------------------

# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# res = [x.upper() for x,v in dict_.items() if v in range(200, 5000)]
# print(res)

# ----------------------------------------------------------

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i', ''):k.count('i') for k,v in dict1.items() }

# print(dict2)

# ----------------------------------------------------------------

# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [x for x in list1 if x ]
# print(list2)

# ------------------------------------------------------------

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [x[0] for x in SPL_Patrons if x[1] > 100]
# print(readers)

# ---------------------------------------------------

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# res = [x['likes'] for x in dict_.values() if x['rating'] > 3 ]
    
# print(sum(res))

# -------------------------------------------------------------

# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# id_ = [v['id'] for x in dict_.values() if len(x['comments']) > 3 for v in x['comments']]

# print(id_)

# for x in dict_.values():
#     for v in x['comments']:
        # print(v['id'])

# -----------------------------------------------------

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# res = {k:len(v) if k % 2 == 0 else len(v)**3 for k,v in dict_.items()}

# # for k,v in dict_.items():
# #     if k % 2 == 0:
# #         dict_[k] = len(v)
# #     else:
# #         dict_[k] = len(v)**3
# # print(dict_)

# print(res)

# ---------------------------------------------------------

# def call_function(func):
#     def obertka():
#         print(f' Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#     return obertka

# @call_function
# def first():
#     print("hello world")
#     return "hello world"
# first()

# -----------------------------------------------

# def func_start_time(func):
#     def datatime():
#         import datetime
#         print(f'Функция запущена {datetime.datetime.now()}')
#         func()
#     return datatime

# @func_start_time
# def func():
#     print('Hello world')
# func()

# ----------------------------------------------------

# def make_bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper

# def make_italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         return '<u>' + func() + '</u>'
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())

# -------------------------------------------

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения: {finish - start} секунд.')
#     return wrapper

# @benchmark 
# def fetch_webpage(): 
#     import requests 
#     webpage = requests.get('https://google.com') 
# fetch_webpage()

# ------------------------------------------------

# users = {'jaanger': '123312', 'vlad': '46456', 'nazar': '456132', 'tima': '456123'}

# def validate_password(func):
#     def wripper(username, password):
#         try:
#             if users[username] != password:
#                 print('Password is invalid')
#             else:
#                 func(username, password)
#         except:
#             print('Username is not defined')
#     return wripper

# @validate_password
# def login(username, password):
#         print(f'Welcome, {username}')

# login('vlad', '789465')

# ----------------------------------------------

# def is_admin(func):
#     def wrapper(a):
#         if a['is_admin']:
#             print(f'Доступ разрешен {a["username"]}')
#         else:
#             print(f'Доступ запрещен {a["username"]}')
#     return wrapper
    

# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})

# -------------------------------------------------------

# def route(func):
#     def wrapper(a):
#         return 'https://www.mywebsite.com/' + func(a)
#     return wrapper

# @route
# def get_page(path):
#     return path
 
# print(get_page('about/'))
# print(get_page('products/'))

# --------------------------------------------------------

# name_of_list = ['Helloworld!']
# for x in name_of_list:
#     a = x[:len(x)//2 + 1]
#     b = x[len(x)//2 + 1:]
# print(a,b)

# -------------------------------------------

# def sort_names(func):
#     def wrapper(names):
#         global sorted_
#         sorted_ = sorted(names, key=func)
#     return wrapper

 
# @sort_names
# def sort_key(e):
#     return e[2]

# def prefix_name(person):
#     sort_key(person)
#     res = []
#     for x in sorted_: 
#         for i in x[3]:
#             if i == 'M':
#                 res.append(f'Mr. {x[0]} {x[1]}')
#             else:
#                 res.append(f'Ms. {x[0]} {x[1]}')
#     return res

# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]))


# a = [('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]

# def sort_name(e):
#     return e[2]
# print(sorted(a, key= sort_name))



# boy = [x for x in a for i in x[3] if i == 'M']
# woman = [x for x in a for i in x[3] if i == 'F']
# print(f'Mr.{boy[0][0]} {boy[0][1]}')
# print(boy)

# ------------------------------------------------

# def get_full_number(func):
#     def wrapper(int_):
#         global res
#         res = []
#         for x in int_:
#             res.append(f'+996 {x[1:4]} {x[4:]}')
#         return func(res)
#     return wrapper


# @get_full_number
# def sort_phone_nums(list_):
#     global res
#     res = sorted(res)
#     res = [str(x) for x in res]
#     res = '#'.join(res)
#     print(res)


# sort_phone_nums(['0777987456', '0555123456', '0770369852'])


# -------------------------------------------

# def type_check(dec_arg):
#     def wrapper(func):
#         def wrapper2(func_arg):
#             if type(func_arg) == dec_arg:
#                 func(func_arg)

#             else:
#                 print('Неверный тип данных :(')
#         return wrapper2
#     return wrapper


# @type_check(int)
# def func1(num):
#     print(num*2)


# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})

# ------------------------------------------------

# with open('task3.txt', 'w+') as f:
#     sumbol = list(range(0,10))
#     res = [str(res) + '*' for res in sumbol]
#     for x in res:
#         f.write(x)
#     f.seek(0)
#     print(f.read())

# --------------------------------------------

# with open('makers.txt', 'r') as f:
#     print(len(f.readlines()))

# ---------------------------------------
# a =[45,21,67,291,13,45,166]

# with open('files.txt', 'r+') as f:
#     a = f.readlines()
#     new_f = [x.replace('\n', '') for x in a]
#     res = [int(x) for x in new_f]
#     f = open('task6.txt', 'w')
#     f.write(f'{min(res)}-{max(res)}')
#     f.close()

# _________________________________________________

# def read_last(lines: int, filename: str):
#     with open(filename, 'r') as f:
#         reverse = f.readlines()[::-1]
#         res = reverse[0:lines]
#         res = [lines.replace('\n', '') for lines in res]
#         for x in res:
#             print(x)


# read_last(1,'makers.txt')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def longest_words(filename: str):
#     with open(filename, 'r') as f:
#         res = [x.split() for x in f.readlines()]
#         result = []
#         for x in res:
#             result.extend(x)
#         result.sort(key=len, reverse=True)
#         max_len = len(result[0])
#         res = []
#         for i in result:
#             if len(i) == max_len:
#                 res.append(i)
#             else:
#                 break
#         return res if len(res) > 1 else res.pop()


# print(longest_words('makers.txt'))

# def countSymbols(s):
#     t=0
#     for i in s:
#         t+=1
#     print(t)
#     return t
    


# items = ["111","1111111","22222"]

# maxStr=[]

# for elem in items:
#     if countSymbols(elem)>countSymbols(maxStr):
#         maxStr=elem

# print(maxStr)


# --------------------------------------------------

# 1.Вам дан список accounts, элементами которого являются другие списки
# Каждый список представляет собой количество денег на счету клиента.
# Напишите функцию которая выводит максимальное количество денег на счету самого богатого клиента.

# Пример:
# accounts = [[1,5],[7,3],[3,5]]
# # Ожидаемый вывод: 10

# res = [sum(x) for x in accounts]
# print(max(res))

# --------------------------------------------------------

# 2.Вам даны две строки:
# Word - слово, ch - буква.
#  Напишите функцию которая будет переварачивать сегмент слова (word),который начинается с индекса 0 и заканчивается индексом первого вхождения ch(включительно). Если ch не существует в слове, возвратите переменную word.

# Пример:
# Ввод: word = "abcdefd", ch= "d"
#  Ожидаемый вывод: "dcbaefd"
# Объяснение:
# Первое вхождение "d" находится в индексе 3.
# Переверните часть слова от 0 до 3 (включительно), в результате получится строка «dcbaefd».

# word = "abcdefd"
# ch= "d"
# def func(word, ch):
#     mid = word.index(ch)
#     s1 = word[0:mid+1]
#     s2 = word[mid+1:]
#     return s1[::-1]+s2
# print(func(word,ch))

    


# a = 'abcdefd'

# print(a.index('d'))

# ---------------------------

# def func(list_):
#     res = []
#     for x in list_:
#         if x.isdigit():
#             res.append(int(x))
#     return res
        
# print(func(['123', '12sd', '54', 'das', '142']))

# -------------------------------

# for i in range(1,51):
#     if i % 3 == 0:
#         i = 'Fizz'
#     else:
#         i = 'Buzz'

#     print(i,end='\n\n')

# result = list(filter(lambda x: x % 3 == 0, range(1,51)))
# print(result)
# result = ['Buzz' if x % 3 == 0 else 'Fizz' for x in range(1,51) ]
# for x in result:
#     print(x)

# result = list(map(lambda x: 'Fizz' if x % 3 == 0 else 'Buzz', range(1,50)))
# print(result)
# ----------------------------------------------------------------------------

# list_ = [1,2,3,4,5,6,8]
# print(max(list_))

# --------------------------------

# from functools import reduce
# list_ = [1,2,3,4,5,6,7,8]
# res = reduce(lambda x, y: x if x < y else y, list_)
# print(res)

# -------------------------------

# string = 'hello'
# res = tuple(enumerate(string, 1))
# print(res)

# -------------------------------

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# res = list(map(abs, list_))
# print(res)

# ----------------------------

# list_ = ['hello', 123]
# print(list(map(type,list_)))

# ----------------------------

# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# res = list(map(lambda x,: x + ' Python' if len(x) > 5 else x + ' JavaScript', names))
# print(res)

# -------------------------------

# list_ = ['123hello@gmail.com', '123', 'hello']
# res = list(map(lambda x: x if '@gmail.com' in x else 'Not valid email', list_))
# print(res)

# ----------------------------------

# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]

# res = list(zip(list1,list2))
# print(res)

# ____________________________________________________________________

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]

# res1 = tuple(map(lambda x: x, filter(lambda x: x if x < 0 else None, list_)))
# res2 = tuple(map(lambda x: x,filter(lambda x: x if x > 0 else None, list_)))
# res = [res1, res2]
# print(res)

# ----------------------------------------------------

# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# res = list(map(lambda x: x ** 2, list_))
# res = [round(x, 3) for x in res]

# print(res)

# -----------------------------------------------------

# list_ = ['a', 'n', 'n', 'a']

# res = [''.join(list_)]
# res2 = list(map(lambda x: 'YES' if x == x[::-1] else 'NO', res))
# for x in res2:
#     print(x)

# ----------------------------------------

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# lists = []
# for x in list_:
#     if type(x) == int or x.isdigit():
#         lists.append(int(x))
# print(sum(lists))        

# -------------------------------------

# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()
# res = []
# a = chars.index(merge_from)
# d = chars.index(merge_to)
# res.append(''.join(chars[a:d+1]))
# for x in chars[d+1:]:
#     res.append(x)
# index_ = 0
# for x in chars[:a]:
#     res.insert(index_, x)
#     index_ += 1

# print(res)

# --------------------------

# import time

# with open('rows_300.csv', 'w') as file:
#     num = 1
#     name = 0
#     while name < 300:
#         ssek = time.localtime()
#         sek = time.time()
#         msek = str(round(sek * 1000000))
#         time.sleep(0.01)
#         file.write(f'{num},{ssek.tm_sec},{msek[-6:]}\n')
#         name += 1
#         num += 1
#         time.sleep(0.01)

# ------------------------------

# def calc_price(filename: str) -> int:
#     res = []
#     result2 = []
#     with open(filename, 'r') as file:
#         a = file.readlines()
#         result = [x.replace('\n', '') for x in a]
#         for x in result:
#             res.append(x.split())
#         for x in res:
#             result2.append(float(x[2]) * float(x[1]))
#         return sum(result2)

# print(calc_price('files.txt'))

# ------------------------------------

# def read_csv(filename: str):
#     with open(filename, 'r') as file:
#         a = file.readlines()
#         list_ = [x.replace('\n', '') for x in a]
#         list_ = [x.split(',') for x in list_]
#         dict_ = {}
#         values = []
#         index_ = 0
#         for x in list_: 
#             a = list_[index_].pop(0)
#             dict_.setdefault(a, x)
#             index_ += 1    
        
#         return dict_

# print(read_csv('data.csv'))

# ----------------------------------------

# import re
# def filter_text(text_filename: str) -> str:
#     with open('forbidden_words.txt', 'r') as bed, open(text_filename, 'r') as text:
#         list_ = bed.read().split()
#         out = text.read()
#         for w in list_:
#             out = re.sub(w,"*"*len(w),out,flags=re.I|re.M)
#         return out


# print(filter_text('files.txt'))

# -------------------------------------

# def bad_students(filename: str):
#     with open(filename, 'r') as file:
#         list_ = file.readlines()
#         list_ = [x.replace('\n', '') for x in list_]
#         list_ = [x.split() for x in list_]
#         res = [x[1] for x in list_ if int(x[2]) < 4]
#         return res

# print(bad_students('students.txt'))

# -------------------------------------

# def reverse_file_print(filename: str) -> None:
#     with open(filename, 'r') as file:
#         list_ = file.readlines()
#         res = [x[::-1] for x in list_]
#         res2 = []
#         for x in res:
#             res2.append(x)
#         for x in res2:
#             print(x)


# print(reverse_file_print('zen_of_python.txt'))


# ---------------------------------------------

# import json
# with open('task1.json', 'r') as file:
#     a = file.read()
#     python_obj = json.loads(a)
# with open('task1.py', 'w') as file:
#     file.write(str(python_obj))

# -------------------------------------------

# import json
# with open('task2.json', 'r') as file:
#     json_obj = file.read()
#     python_obj = json.loads(json_obj)

# ----------------------------------------

# import json
# python_obj = None
# json_obj = json.dumps(python_obj)
# print(json_obj)

# -----------------------------------

# import json
# json_obj = "null"
# python_obj = json.loads(json_obj)
# print(python_obj)

# ---------------------------------
# size = 3
# read = [[x for x in range(1,size+1)] for x in range(1,size+1)]

# print(read)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = int(input())
# b = int(input())
# c = int(input())
# if (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
#     print("rectangular")
# elif (c**2 < a**2 + b**2) or (a**2 < b**2 + c**2) or (b**2 < a**2 + c**2):
#     print("acute")
# elif (c**2 > a**2 + b**2) or (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2):
#     print("obtuse")
# else:
#     print("impossible")

# ------------------------------

# string = '123456'
# if (int(string[0]) + int(string[1]) + int(string[3]) == (int(string[4])) + int(string[5]) + int(string[5])):
#     print('да')
# else:
#     print('нет')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = 3
# b = 2
# c = 1
# if a > b and a > c and b > c:
#     print(c,b,a)
# elif b > a and b > c and a > c:
#     print(c,a,b)
# elif a > b and a > c and c > b:
#     print(b,c,a)
# elif b > a and b > c and c > a:
#     print(a,c,b)
# elif c > a and c > b and a > b:
#     print(b,a,c)
# else:
#     print(a,b,c)

# -------------------------------------







        
    

