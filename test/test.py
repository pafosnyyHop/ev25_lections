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

# res = [word for word in list_ if a in word.lower()[0]]
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

#    print("ERROR")

# else:

#    print("YES")

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

months = {
    1:'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

while True:
    number = input('Vvedite nomer mesyaca: ')
    if number == 'john':
        break

    if not number.isdigit():
        print('Trebuetsya vvesni realniy nomer mesyaca!')
        continue
    number = int(number)
    if number not in range(1,13):
        print('Trebuetsya vvesni realniy nomer mesyaca!')
        continue

    if number in range(3,6):
        print(f'Vi rodilis v {months[number]}. Birds pely prekrasnie pesny.')
    elif number in range(6,9):
        print(f'Vi rodilis v {months[number]}. Solnce svetilo yarche chem kogda libo')
    elif number in range(9,12):
        print(f'Vi rodilis v {months[number]}. Urojay bil neveroyatny.')
    else: 
        print(f'Vi rodelis v {months[number]}. Za oknom padal bely sneg. ')


    




