# Функция высшего порядка - это функция которая в качестве аргумента принемает другую функцию


# Декораторы- это функция, которая позволяет без изменения кода "обернуть"
#  другую функцию для того чтобы расширить функционал обернутой функции


# def decorator(func):
#     print(func) #-высвечивает что за функция и где она находится
#     print(f'Name of function: {func.__name__}')
#     return func()

# def hello():
#     print('Hi stranger!')
#     print('My name is Tony Stark!')

# decorator(hello)




# Pythonic way - это красота и простота кода
# Синтаксический сахар - красота кода  
# @ -синтаксический сахар декоратора
#_-----------------------------------------------


# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Vremya vipolneniya functii:  {func.__name__} , zanyalo :{finish-start}')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     while i <= 10000:
#         print(i)
#         i +=1

# @benchmark
# def add():
#     ls =[]
#     for i in range(0,10001):
#         ls.append(i)

# loop()

# add()

#-------------------------------------------------

# def bold(func):
#     def wrapper(*args,**kwargs):
#         return '<bold>' + func() +'</bold>'
#     return wrapper


# def div(func):
#     def wrapper(*args,**kwargs):
#         return '<div>' + func()+'/div'
#     return wrapper


# @div
# @bold
# def str_():
#     return 'John Snow'

# print(str_())


#---------------------------------
# def capitalize(func):
#     def wrapper(name):
#         modified_name = name.capitalize()
#         return func(modified_name)
#     return wrapper


# @capitalize      
# def say_hello(name):
#     return f'Hello, {name}!'
# @capitalize
# def say_whatsapp(name):
#     return f'What\s  up-broo ,{name} nigga'

# print(say_hello('tony'))
# print('Lock Dog')


#-------------------------------------------------\\\

# def trace(func):
#     def wrapper (*args,**kwargs):
#         print(f'Trace: vizvano {func.__name__}(), \n {args},{kwargs}')
#         original_res = func(*args,**kwargs)
#         print(f'Trace: vizvano {func.__name__}(), \n:function became{original_res}'  )
#         return original_res
#     return wrapper


# @trace
# def say(name,line):
#     return f'{name}:{line}'



# @trace
# def hello(name, last_name ,country):
#     return f'Hello {name} {last_name} from {country}'
# say('Tony','333line') 
# hello('Tirion','Lanister','Csterly Rock')

# ------------------------------------------------------------

# globals()-возвращает словарь в котором описанны все имена которые содержит глобальная область видимости
# locals()-возвращает словарь в котором описанны все имена которые содержит локальная область видимости

# num =1
# while num>=0:
#     try:
#         num = int(input('vvedite chislo: '))
#     except ValueError:
#         pass
# else:
#     print('Vstretilos otricatelnoye chislo!')
#-------------------     
# from random import randint
# ls=[]
# for x in range(0,100):
#     ls.append(randint(1,50))
    
# ls = list(set(ls))
# res = sorted(ls)
# print(res)
#----------------------
# def introduce(name, last_name, wife ='holost',**kwargs):
#     print(F'Hello! This is {name} {last_name}')
#     print(f'Hes {wife}')
#     if kwargs:
#         print(f'His wife\'s name is {" ".join(kwargs.values())}')
# introduce('Tony','Stark','Pepper Pots')
# introduce('John','Snow',wife_name='Mark',wife_last_name ='Stark')
#-----------------------------------------------
# roles ={
#     0:'Admin',
#     1:'Customer',
#     2:'Vendor',
# }
# users=[
#     {
#         'id':1,
#         'username': 'Tony',
#         'role': roles[0],
#     },
#     {   'id':3,
#         'username': 'Tirion',
#         'role': roles[2],
#     },
#     {
#         'id':2,
#         'username': 'Raychel',
#         'role':roles[1]
#     }
# ]
# product={
#     'id': 1,
#     'title':'Iphone 14',
#     'description':'Lorem Ipsum',
#     'prise':1200
# }
# print(f'Before: {product}')
# id_user =int(input('Vvedite svoi id:'))
# try:
#     user = list(filter(lambda x: x['id'] ==id_user,users))[0]
#     print(f'Welcome {user}')
# except IndexError:
#     raise ValueError('invalid id for user! User with this id does not exist!')
# if user['role']==roles[0]:
#     choise =input('Vvedite izmeneniya: ')
#     product[choise]=input('Vvedite novoye znacheniye: ')
# else:
#     raise Exception('Permission denied')
# print(f'After: {product}')
#_----------------------------------------------
# cash=int(input('Vvedite depozit ne menshe 30 000: '))
# years =int(input('Vvedite period vlogeniya ne menshe 3 let: '))
# def depozit(cash,years):
#     if cash<30000:
#         raise Exception('Nedostatochno sredstv')
#     if years<3:
#         raise Exception('Bolshe vremeni')
#     i =0
#     while i<years:
#         cash +=cash/100*10
#         i+=1
#         return cash
# print(depozit(cash,years))
#-----------------------------
# list_ =[[100,2,3],[300,3,5],[5,5,5,5],[45,45,6]]
# def findmax(ls):
#     return max(sum(x)for x in ls)
# print(findmax(list_))
#_----------------------------------------
# str_ = 'formula john snow 1'
# def getReverse(str):
#     res = str_.split(' ')
#     res2 = res[::-1]
#     return ' '.join(res2)
# print(getReverse(str_))
