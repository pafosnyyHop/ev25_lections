# s1 = 'Amerika'
# s2 = 'Japan'
# # res = 'fs1-fs2-ms1-ms2-ls1-ls2'

# first_s1 = s1[0]
# first_s2 = s2[0]
# middle_s1 = s1[len(s1) //2]
# middle_s2 = s2[len(s2) //2]
# last_s1 = s1[-1]
# last_s2 = s2[-1]
# res = first_s1 +  first_s2 + middle_s1 + middle_s2 + last_s1 + last_s2
# print(res)

# 11. Объявите переменную string значением которой будет несколько хэштегов, разделённых символом '#'. Разделите их в отдельные строки.
# Например: #makers#bootcamp#программирование#it#курсы 
# Вывод: ['makers', 'bootcamp', 'программирование', 'it', 'курсы']

# str1 = '#makers#bootcamp#программирование#it#курсы'
# res = str1[1:].split('#')
# print(res)

# for number in range(1,100):
#     # print(number)
#     if number % 3 == 0 and number % 5 == 0:
#         print(f'{number} fuba')
#     elif number % 3 == 0:
#         print(f'{number} fu')
#     elif number % 5 == 0:
#         print(f'{number} ba')
