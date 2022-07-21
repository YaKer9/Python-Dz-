# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# Пояснения к первой задаче: нужны три функции.
# Первая - на ваш N дает список

# Вторая - из вашего списка записывает в файл любое количество индексов (иначе индексы в списке не соотносятся с списком) 

# Третья - считывает индексы с файла, находит их в списке, умножает их.


# print(Numbers_N)

# with open('file.txt', 'w') as data:           #peremennaya data(avtmati4eski zakroetsa)
#     data.write(Numbers_N)
   
# with open('text.txt', mode = 'r') as file:
#     # data.write(Numbers_N)
#     print(file.read())
# import random

# # # N = random.randint(1, 10)
# N=5
# Numbers_N = []

# def lst1(numbers:int, lst:list):
#     lst = []
#     for i in range((-1)*N, N+1):
#         lst.append(i)
#         return lst

# with open("copy.txt", "w") as file:
#     for i in range(0, 5):
#         file.write(str(random.randint(0, 5))+'\n')

# def res(Numbers_N, res_list):
#     mult = 1
#     for i in res_list:
#         mult = mult * i
#     return mult
    

# def return_list(path):
#     copy_txt = open(path, 'r')
#     lst = [int(line.rstrip()) for line in copy_txt]
#     copy_txt.close
#     return lst

# path = 'copy.txt'
# result_list = return_list(path)
# print(result_list)
# result = res(N, result_list)
# print(result)
# # f = open('copy.txt')
#  for line in f:
#      line

# with open('copy.txt', mode = 'r') as file:
#     file.write()
# f = open('text.txt')
# f.read(1)
# 'H'
# f.read()
# 'ello world!\nThe end.\n\n'







# Numbers_neg  = []
# for j in range((-1)*N, 0):
#     Numbers_neg.append(j)
# print(Numbers_neg)
# res = 



# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
# (не использовать sort и sorted)

# 3.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# 4.Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


# with open('text', mode = 'r') as file:
#    print(file.read())


##########################

# from random import randint


# def input_number_test_float(text):
#     int_test = True
#     is_minus = False
#     while int_test:
# def list_length_n(n:int = 0,lst: list = []):
#     for i in range(-n,n):
#         lst.append(randint(n*-1,n+1))
#     print(lst)
#     return lst
# lst = list_length_n(n,)

# with open('text.txt', mode = 'w') as file:
#     for k in range(0,5):
#         file.write(f"\n{randint(0, len(lst)-1)}")
    
# with open('text.txt', mode = 'r') as file:
#     res = 1
#     lst_index = []
#     for line in file.read():
#         if line.isdigit():
#            res *= lst[int(line)] 
#            lst_index.append(line)
# print(f"{lst_index=}")           
# print(f"{lst=}")
# print(res)
# #############