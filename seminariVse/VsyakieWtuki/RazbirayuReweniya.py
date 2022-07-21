# from functions import input_numbers_text_float
# number = str(input_numbers_text_float('Enter number: '))     ### --- Решается только если интовое значение дать. иначе просит попробовать заново ввести число
# result = 0
# for i in number:
#     if i.isdigit():
#         result = result + int(i)
# print(f'sum of numbers in {number} = {result}')


# import time
# import random

# # 3 - Задайте список из n чисел последовательности (1+1/n)**n 
# # и выведите на экран их сумму.
# # - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

# def num_biger_then_zero(text):

#     int_num = True
#     while int_num:
#         n = input(f"{text}")
#         if n.isdigit():
#             n = int(n)
#             if n <= 0:
#                 print("Введите число > 0")
#             else:
#                 int_num = False
#         else :
#             print("Не число, попробуйте еще раз")
#     return n
# n = num_biger_then_zero("Введите n : ") 
# lst_num = {}
# for i in range(1, n +1): 
#     lst_num[i] = (1 + 1 / i) ** i
# print(f'Резултат: {lst_num}')


# # Используйте timeit.default_timer вместо timeit.timeit.
# # Первый обеспечивает наилучшие часы, доступные на вашей платформе и версии Python, автоматически:

# from timeit import default_timer as timer

# start = timer()
# # ...
# end = timer()
# print(end - start)      
# # timeit.default_timer присваивается time.time() или time.clock() в зависимости от ОС.
# # На Python 3.3+ default_timer time.perf_counter() на всех платформах. См. Python - time.clock() vs. time.time() - точность?


# #2ya zada4a 3dz
# len(list_of_numbers)/2 + len(list_of_numbers) % 2#0, 1
# math.ceil(len(my_list)/2)

###############

# #3ya
# {dif:.3f}#-obrezayet 3 posle .

#############

# 2. Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию. 
# (не использовать sort и sorted)
# from random import randint    #Создали и заполнили случайными целыми числами список 
# list_numbers = []
# for i in range(1,20):
#     list_numbers.append(randint(-10, 10))
# print(list_numbers)

# file = open('list_of_num.txt', 'w', encoding='utf-8') # создаем и записывем в файл наш рандомный список
# for i in list_numbers: # идем по циклу
#     file.write(f'{i}\n') # записываем каждый элемент списка с новой стоки в созданном файле
# file.close()    #закрываем

# file = open('list_of_num.txt', 'r', encoding='utf-8')
# data =file.read()
# list_of_rows = data.split()
# for i in range(0,len(list_of_rows)):
#     list_of_rows[i]=int(list_of_rows[i])

# def sort_list_from_min_to_max(list_num: int):
#     for i in range(0,len(list_num)):            # 1  2  3  4  5  6
#         for j in range(i +1, len(list_num)):    # 12 3  6  7  2
#             if list_num[j] < list_num[i]:       # 3  6  12 
#                 list_num[j], list_num[i] = list_num[i], list_num[j]

# print(list_numbers)  
# sort_list_from_min_to_max(list_of_rows)              
# print(list_of_rows)

###################
#puzirki ???
##################
            #2zada4a
# from random import randint
# n = 5

# def list_length_n(n:int = 0,lst: list = []): #Задаут список из N элементов, заполненных числами из промежутка [-N, N]
#     for i in range(-n,n):
#         lst.append(randint(n*-1,n+1))
#     return lst

# lst = list_length_n(n,)

# with open('text.txt', mode = 'w') as file:
#     for k in range(0,5):
#         file.write(f"\n{randint(0, len(lst)-1)}")
    
# with open('text.txt', mode = 'r') as file:
#     res = 1
#     lst_index = []
#     for i in file.read():
#         if i.isdigit():
#            res = res * lst[int(i)] #2*1*1*(-4)*1 = -8
#            lst_index.append(i)

# print(f"{lst_index=}")           
# print(f"{lst=}")
# print(res)

##########################

# 3.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# str_of_num = input("Enter numbers:") # вводим числа с клавиатуры через пробел
# list_of_nums = str_of_num.split() # разделяем строку пробелами 
# for i in range(0,len(list_of_nums)):
#     list_of_nums[i]= int(list_of_nums[i])
# max_num =list_of_nums[0]
# min_num = list_of_nums[0] 
# for i in list_of_nums:
#     if i < min_num:
#         min_num = i
#     if i > max_num:
#         max_num = i
# print(f'{list_of_nums} min->{min_num} and max->{max_num}')

#####

# 4.Задайте два числа. Напишите программу, которая найдёт НОК
#  (наименьшее общее кратное) этих двух чисел.
# Это наименьшее натуральное число, которое делится и на «num1», и на «num2».

# def find_nok(num1: int, num2: int) -> int:
#     nok = min(num1,num2)
#     while True:
#         if nok % num1 == 0 and nok % num2 == 0:
#             break
#         nok = nok + 1
#     return nok

# print(find_nok(4,6))

######################

# #- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

# #Пример:
# #- при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

# #Ряд Нилаканта:
# # π = 3 + 4/(2*3*4) — 4/(4*5*6) + 4/(6*7*8) — 4/(8*9*10) + 4/(10*11*12) — (4/(12*13*14) …
# pi = 3.141
# def null_counter(num:float):
#     '''
#     Переносит точку в числе и считает, сколько знаков после точки
#     param: num - вещественное число
#     return: counter - количество символов после точки, num = int
#     '''
#     counter = 0
#     while num != int(num):
#         num*=10
#         counter+=1
#     return counter, num
# d = float(input('enter the d: '))
# num_d = null_counter(d)
# number_d = num_d[0]
# print(number_d)
# def find_pi(number_d):
#     num = 2
    
#     for i in range(number_d+1):
#         pi = 4 / (num * (num+1) * (num+2))*(1)+pi
#         num+=2
#         pi = 4 / (num * (num+1) * (num+2))*(-1)+pi
#         num+=2
#     return pi
# print(f'We find pi: {find_pi(number_d)}')

#############

# #2- Задайте последовательность чисел. Напишите программу, 
# # которая выведет список неповторяющихся элементов исходной последовательности. 
# # Посмотрели, что такое множество? Вот здесь его не используйте.

# #Вариант без множества:

# numbers_lst = [20, 20, 30, 30, 40]
# print(f'Исходный заданный список:{numbers_lst}')
# def get_unique_numbers(numbers_lst):
#     unique_lst = []
#     for i in numbers_lst:
#         if i not in unique_lst: #если нет числа в уникальном списке, то его нужно добавлять в список
#             unique_lst.append(i)
#     return unique_lst
# print(f'Полученный уникальный список: {get_unique_numbers(numbers_lst)}')

# # ##########

# 3- Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]
# Простые множители положит числа  - это простые числа, которые делят это число нацело без остатка
# def num_biger_then_zero(text):
#     int_num = True
#     while int_num:
#         n = input(f"{text}")
#         if n.isdigit():
#             n = int(n)
#             if n <= 0:
#                 print("Введите число > 0")
#             else:
#                 int_num = False
#         else :
#             print("Не число, попробуйте еще раз")
#     return n
# n = num_biger_then_zero("Введите натуральное число n : ") 

# def get_prime_factors(n):
#     my_lst =[] # список делителей
#     i = 2 # чтобы число делилось на делитель нацело(если нет остатка - все ок, если есть остаток- увеличиваем делитель на единицу)
#     while(i <= n):
#         if(n % i) ==0:
#             my_lst.append(i) # добавляем в список, если делится без остатка
#             n = n / i #результат от деления записан в число(продолжаем делить новое число)
#         else:
#             i = i + 1    
#     return my_lst        
# print(set(get_prime_factors(n))) 
# 180 : 2 = 90 - записали в список  (2, 2, 3, 3, 5 )
# 90 : 2 = 45 - записали в список 
# 45 : 3 = 15 (увеличили делитель: i = i + 1)
# 15 : 3 = 5 (записали в список)
# 5 : 5 = 1 (увеличили делитель до следующего простого множителя)

# ##############

# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.



# from importlib.resources import path

# file = open('Text.txt' , "w",encoding='utf-8') #записыаем и создаем файл
# file.write("Мама сшила м0не штаны и7з бере9зовой кор45ы 893.")
# file.close()

# path = 'Text.txt'
# file = open('Text.txt' , "r",encoding='utf-8') #считываем из файла строку
# data = file.read()
# file.close()
# def delete_num(put:str): # Функия удаления слов с цифрой в строке
#     list_of_words = data.split() # разбиваем строку на отдельные символы через запятую
#     my_list =[] # создвем новый список для записи результата выполнения функкции
#     for i in list_of_words:
#         for num in i:
#             if num.isdigit(): #проверяем есть ли число
#                 break
#         else:
#             my_list.append(i)       #добавляем в список только слова     
#     return my_list       

# delete_num(path) # получаем резултат работы функции (наш новый список)
# result_string = "" # преобразуем в строку
# for i in delete_num(path):
#     result_string += str(i)+ ' ' # добавляем пробелы
# print(f'Результат: {result_string}')


