# type hint
# from ast import Param
# from typing import List

# def sum_list(nums.List): 
#     :param
#     :return
#     nums.
#     return sum(nums)
# sum_list('gaga')

# with open('text.txt') as file:                #что это вообще хз
#     data = file.read()
#     for line in data:
#         print(line)

# N = int(input('Введите число : '))
# count = 1
# for i in range(1,N):
#     count = count*i
    
#     print(count, f'{[i]}')



# from time import time
# print(f'Случайное число от 0 до 99 = {int(time() % 1 * 100)}')

# def sporadic_number():
#     oper_moment = timer()
#     textp = str(oper_moment).split(".")
#     randomnum = (int(textp[0])^int(textp[1]))%10
#     print(randomnum)


#######################################################
# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# [',hfh5', '5', 'dfgh'] - da
import re
list_ok = 'seven 4 odin 0'
# number_f = '4'

# str = 'We live at 9-162 Malibeu. My phone numb'
# x = re.findall('[0-9]+', str)
numbers = re.findall('[0-9]+', list_ok)
print(numbers)

# print(type(list_ok))
# print(list_ok)

# numbers = re.findall('[0-9]+', str)

# for i in list_ok:
#     if list_ok[i] == True:
#         print('da')
#     else:
#         i+=1









# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# ##['a', 'a','b'] -> 'a' по индексу 1

# def findSecondIndex(list, word):
#     n = 0
#     for idx,item in enumerate(list):
#         if (word == item):
#             n += 1
#             if (n == 2):
#                 return f'result = {idx}'
#     return 'result - not found'

# list_of_words = ['green', 'red', 'blue', 'yellow', 'green']
# t = input('введите слово для поиска: ')
# print(findSecondIndex(list_of_words, t))

###lu4weee!!!!!!

# lst = ['21','1', 'er', '21']
# find_number = 1
# #count = 2#количество вхождений
# def find_nuber_in_list(lst_to_seek:list,number:int,count:int = 2):
#     for i in range(0,len(lst_to_seek)):   
#         if lst_to_seek[i] == str(number):
#             count = count-1
#         if count == 0:
#             return i
#     return -1
# pos_number = find_nuber_in_list(lst,find_number)
# if pos_number != -1:
#     print(pos_number)
# else:
#     print('в списке нет 2 вхождение')
