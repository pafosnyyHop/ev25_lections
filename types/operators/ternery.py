# a = input('Vvedite predlojenie: ')

# if a [-1] == '?':
#     print('predlojenie voprositelnoe')
# else:
#     print('obichnoe predlojenie')

# a = input('Vvedite predlojenie: ')
# print('Predlojenie voprositelnoe' if a[-1] == '?' else 'Obichnoe predlojenie')

# Тернарный оператор - это конструкция, которая аналогичная по своим свойствам 
# и дествию констпукции if/else, но при этом записывается в одну строчку кода.

# <выражение если в условии True> if <условие> else <выражение если False>

# number = 15
# res = 'even' if number % 2 == 0 else 'odd number'
# print(res)

# from string import digits 

# symbols = digits + '-'
# print(symbols)
# number = input('Vvedite chislo: ')
# is_correct = True
# for i in number:
#     if i not in symbols:
#         is_correct = False
    
# if is_correct:
#     print('Yes number!')
#     number = int(number)
#     print('your number:', number)
#     res = number if number >= 0 else -number
#     print(res)
# else:
#     print('invalid values!')

# if number.isdigit():
#     number = int(number)
#     print('Da chislo!')
# else:
#     print('Vi vveli ne chislo!')

# ---------------------------------------------

from string import digits

flag = True
symbols = digits + '-' + '.'

while flag:
    is_correct_number = True
    num1 = input('Vvedite pervoe chislo: ')
    if len(num1) <= 1 and num1 == '.' or num1 == '-' or not num1:
            print('Vi vveli nepravilnoe chislo!')
            is_correct_number =False
    for x in num1:
        if x not in symbols:
            print('Vi vveli nepravilnoe chislo!')
            is_correct_number = False
            break
    if not is_correct_number:
        continue

    num2 = input('Vvedite vtoroe chislo: ')
    if len(num2) <= 1 and num2 == '.' or num1 == '-' or not num2:
            print('Vi vveli nepravilnoe chislo!')
            is_correct_number =False
    for x in num2:
        if x not in symbols:
            print('Vi vveli nepravilnoe chislo!')
            is_correct_number = False
            break
    if not is_correct_number:
        continue

    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    
    operator = input('Vvedite operator(+, -, *, /): ' )
    if operator == '+': 
        print(f'Resultat: {num1 + num2}')
    elif operator == '-':
        print(f'Resultat: {num1 - num2}')
    elif operator == '*':
        print(f'Resultat: {num1 * num2}')
    elif operator == '/':
        if num2 == 0:
            print('Na nol delit\' nelzya!')
        else:
            print(f'Resultat: {num1 / num2}')
    else:
        print('Vi vveli nepravilny operator!')

    choise = input('Hotite ostanovit\' (yes): ')
    if choise.lower() == 'yes':
        flag = False
        print('Good bue!')


