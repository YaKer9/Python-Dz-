# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


# def Squar(x,y):
#     if x*x == y:
#         print ('Yes')
#     elif y*y == x:
#         print ('Yes')
#     else:
#         print ('No')

# x = int(input('Введите X '))
# y = int(input('Введите Y '))
# Squar(x,y)


# lst = [1, 4, 8, 7, 5]
# max = lst[0]
# for i in range(5):
#     if max < lst[i]:
#         max=lst[i]
# print (max)

# import random
# lst = []
# for i in range (5):
#     lst.append(random.randint(1,100))
#     print(lst)

# a = [4, 7, 9, -2, 7]


# def fun(b):
#     max = b[0]
#     for i in b:
#         if i > max:
#             max = i
#     return max
# print(f'{fun(b)}')

# a = [4, 7, 9, -2, 7]


# list_num = [10, 4, 8, 7, 5]
# max_num = list_num[0]
# for i in list_num: - Тоже работает
#     if max_num < i:
#         max_num=i
# print (max_num)


# input_numbers = input('Enter numbers using space: ').split(' ')       -   Ввод числе и нетолько через пробел
# print(input_numbers)
