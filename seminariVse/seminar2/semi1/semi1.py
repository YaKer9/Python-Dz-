# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81



# N = int(input('Введите число: '))

# for i in range(0, N):
#     result = (-3)**i
#     print (result)
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input('Введите число: '))
# rest = {}
# for i in range (0, n +1):
#     result = {i:(i+1)* 3+ 1}
#     rest.update(result)
# print(rest)
# dicti = {}
# dicti[] = 
# n = int(input('Введите число n='))
# rez = {}
# for i in range(0,n):
#     result = {i+1:(i+1)*3+1}
#     rez.update(result)
# print(rez)

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# first_string = input('Заполните строку 1: ')
# second_string = input('Заполните строку 2: ')
# print (first_string, ',', second_string)


# slovar = dict()
# a = int(input('введите размер массива'))
# for i in range(1, n+1):
#  slovar [i] = i*3+1
#  print (slovar)

# range(start =1, ebd = 1, step = 2)                #-----начало, конец и шаг(оба варианта)
# range(1,5,2)

# s = s[1:]       #----------- это срез

# st1 = 'попугай попугал попугая'
# st2 = 'поп'
# i = len(st2)
# n=0
# while st1 != '':
#     if st2 == st1[0:i]:
#         n = n + 1
#         st1 = st1[1:]
#     else:
#         st1 = st1[1:]
# print(n)

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

# string1 = input('Напиши что нибудь: ')
# string2 = input('Напиши что нибудь ещё разок: ')
# if len(string1) < len(string2):
#     string1, string2 = string2, string1

# count = 0

# for i in range(0, len(string1)-len(string2)):
#     if string2.lower() == string1[i:i+len(string2)].lower():
#         count += 1
#     print(string1[i:i+len(string2)])
# print(count)
