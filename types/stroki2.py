# print(dir(str)) 
"""
replace(old, new, [count]) - меняем в строке old на new 
значение, если вы укажите count, то он заменит его ровно count раз.
"""
# text = 'ha ha ha ha'
# res = text.replace('a', 'i', 2)
# print(text)
# print(f'res afternreplace: {res}')

# str1 = 'hi world! my name is John Snow'
# res = str1.replace('John', 'Jamie')
# print(res)

# print(id('H'))
# print(id('h'))

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip 


# text = input('Enter the text:\n')
# print(text)
# print(len(text))
# res = text.strip()
# print(res)
# print(len(res))

# text = '   Hello world   '
# print(len(text))
# res = text.rstrip()
# print(res)
# print(len(res))

# print(dir(str))

# isdigit -                       проверяет
# isnumerical -           состоит ли наша строка
# isdecimal -               полностью из чисел

# text = '57'
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
#     print('oops')

# text = '\u0031'
# print(text)
# print(text.isnumeric())

# isalnum() - состоит ли наша строка из
# символов и чисел латинского алфавита и керpилицы

# str1 = '56_a'
# print(str1.isalnum())

# isalpha() - состоит ли наша строка из символов латиского,
# киррильского алфавита

# text = 'Hello world'
# print(text[:5].isalpha())

# islower()
# isapper()
# istitle()

# str1 = 'Is My Name'
# print(str1.istitle())

# index(value, [start], [end]) - выводит индекс значения value которое мы передаем в нашей строке.

# count(value,[start]) - считает количество вхождений value в нашу строку

# text = 'hello o o hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))

# text ='Hello World! My name is John Snow'
# print(text.index('John'))
# res = text.index('o')
# print(res)
# res = text.index('o', res+1)
# print(res)
# res = text.index('o', res+1)
# print(res)
# res = text.index('o', res+1)
# print(res)

'Hello World! My name is John Snow'
# text = 'oooHello World! My name is John Snowooo'
# text = input ('Enter the name: ')
# i = 0
# res = -1
# while i <   text.count('o'): #4
#     res = text.index('o', res+1)
#     print(res)
#     i += 1 # инкремент

# find(value , [start], [end]) - делает то же самое что и index ,
#  но есть одно отличие, в том что если value нет в строке то возращается индекс -1

# text = 'hello'
# print(text.find('l'))
# print(text.find('hi'))

# swapcase() - переводит все символы в противоположный регистр
# upper() - все символы в верхний регистр
# lower() - все символы в нижний регистр

# text = 'HellO World, joHN SNow'
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# capitalize() - переводит первую букву в верхний регистр

# name = input('Enter your name:\n').capitalize()
# print(f'Hello! {name}!')

# title() - переводит первые символы всех слов в верхний регистр

# text = 'jonh jamie sansa marsel risya '
# print(text.title())
# print(text.capitalize())

# split(разделитель) - дробит строку на несколько частей по разделитнлю 
# который находится в строке, все части строки сохраняются в тип данных list

# text = 'let my speak by my hearth in English! Cause'
# ls = text.split(' ')
# print(ls)
# print(len(ls))

# 'разделитель'.join(iterable(list)) - соединяет строки по разделителю строки,
#  которые находятся в list 

# res =' '.join(ls)
# print(res)















