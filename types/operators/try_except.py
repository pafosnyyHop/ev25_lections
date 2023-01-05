# обработка исключений
# операторы try...except

# Ошибки Errors - связаны с кодом:
#     SyntaxError
#     IndentationError
#     TabError

# Исключения  Exceptions - связаны с неправильными данными которые передаются в код

# ZeroDivisionError
# ArithmeticError
# NameError
# IndentationError
# KeyError
# ValueError
# ImportError
# BaseException # прородитель всех исключений

# try:
#     num1 = int(input('Enter the number: '))
#     print(num1)
#     num2 = int(input('Enter the number2: '))
#     print(num2)
#     print(num1 / num2)
# except:
#     print('неправильные данные')

# print('очень важный код')



# try ... except 

# try:
#     <body try>
# except:
#     <body except> сработает только если ошибка в try
# <else:>
#     <body else> сработает если в операторе try нет ошибки
# <finally:>
#     <body finally> сработает в любом случае

# try:
#     num1 = int(input('Enter the number: '))

# except:
#     print('Invalid values!')
# else:
#     print(num1)
#     print(num1 + 5)
# finally:
#     print('Конец кода!')

# ------------------------------------------------------

#  отображение ошики 
# 1. import sys

# list_ = [1, 2, 3, 4, 5]
# index = int(input('Vvedite index: '))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'Oops, we catched {sys.exc_info()[0]} error!')

# 2. Exception as e / (error)

# ls = [1, 2, 3, 4, 5]
# while True:
#     try:
#         index = int(input('Vvedite index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'Oops we catched {e.__class__} error!')

# try:
#     num1 = int(input('Vvedite chislo1: '))
#     print(num1 / 0)
# except (ValueError, ZeroDivisionError ):
#     print('Vi vveli necorrectnie dannie!')

# try:
#     num1 = int(input('Vvedite chislo1: '))
#     print(num1 / 0)
# except ValueError:
#     print('Invalid Values')
# except ZeroDivisionError:
#     print('Divide by 0!')

# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     res = num1 / num2
# except ZeroDivisionError:
#     print('Nan nol delit nelzya!')
# except ValueError:
#     print('Invalid symbols!')
# else:
#     print(res)
# finally:
#     print('The end!')

# --------------------------------------------

# from string import digits

# flag = True
# symbols = digits + '-' + '.'

# while flag:
#     num1 = input('Vvedite pervoe chislo: ')
#     num2 = input('Vvedite vtoroe chislo: ')


   
#     try:
#         num1 = float(num1) if '.' in num1 else int(num1)
#         num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('Vi vveli nepravilnoe chislo!')
#         continue
    
#     operator = input('Vvedite operator(+, -, *, /): ' )
#     if operator == '+': 
#         print(f'Resultat: {num1 + num2}')
#     elif operator == '-':
#         print(f'Resultat: {num1 - num2}')
#     elif operator == '*':
#         print(f'Resultat: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('Na nol delit\' nelzya!')
#         else:
#             print(f'Resultat: {num1 / num2}')
#     else:
#         print('Vi vveli nepravilny operator!')

#     choise = input('Hotite ostanovit\' (yes): ')
#     if choise.lower() == 'yes':
#         flag = False
#         print('Good bue!')

# ----------------------------------------------------
# inp1 = input() 
# inp2 = input() 
# try:
#     if inp1.isdigit() and inp2.isdigit():
#         print(int(inp1)+int(inp2))
#     else:
#         print(inp1+inp2)
    

# except NameError:
#     print('a')


inp1 = input()
list_ = list(inp1)

