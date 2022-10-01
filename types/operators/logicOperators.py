# операторы сравнения 
# условные операторы 
# логические операторы

# операторы сравнения 
# <, >, ==, <=, >=, !=

# email = input('Enter email:\n')
# passworld1 = input('enter the password:\n')

# if len(passworld1) < 8:
#     raise ValueError('passworld too short!')

# passworld2 = input('enter the password confirmation:\n')

# if passworld2 != passworld1:
#     raise ValueError('Passwords didn\'t math!')
# else:
#     print('successfully signed up!')

# age = input('Enter your age:\n')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid values!')

# if age < 18:
#     print(f'Acces denied!!! come again {18 - age} age!')
# else:
#     print('You can buy!!')

# Логические операторы
# and - логическое и
# or - логическое или
# not - лог отрицание

# user = 'John'
# is_google_user = True
# is_github_user = True
# is_age_greater_21 = False
# user_coins = 4000

# # либо юзер гкгла или гитхаба и лтбо возраст выше 21
# # либо бабки(8000)

# if is_google_user or is_github_user and is_age_greater_21 or user_coins > 8000:
#     print(f'Yu can enter the sistem Mr/Mrs {user}!')
# else:
#     print('sorry, you couldnt enter!')

# Операторы идентификации
# in - проверяет наличие элементов внутри какого-либо интерируемого обьекта(строки, списки и т.д)
# is - сравнивает ячейки памяти двух обьектов
# is not - отричательное сравнение ячеек памяти

str1 = 'Hello world!'
print(str1)
choise = input('Enter the symbol:\n')

if choise in str1:
    print(f'the symbol: {choise} exist!')
else:
    print(f'The symbol: {choise} does not exit!')




