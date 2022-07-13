                                    # 1
# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11
# from asyncio.windows_events import NULL


# number_float = input('Enter the number: ')
# result = NULL
# for i in number_float[1, ]:
#     if i.isdigit == True:
#         result += 


# from asyncio.windows_events import NULL

# result = NULL
# a= int(input('Enter the number: '))
# for i in (a):
#         result = result+i
# print(f"sum of numbers in {a} = {result}")
# print(result)


# def concatenatio(a):
#     res: str = "" # int = 0 print(1,2,3,4)
#     for item in a:
#         res += item
#     return res    
# # print(concatenatio('а', 'b', 's'))
# a= int(input('Enter the number: '))
# # concatenatio(a)
# print(type(a))
# print(concatenatio(a))

# n= NULL
# for i in range (a):
#     a.isdigit() == True
#     n+=1
#     print(n)
# else:
#     print('Eror')
# print (n)

# num_of_quater = ' '                                #второй вариант проверки для себя
# while num_of_quater.isdigit() == False:
#    num_of_quater = input ('Введите номер четверти: ')
# print('Номер четверти: {}'.format(num_of_quater))

#num_of_quater = ' '                                #второй вариант проверки для себя
# while num_of_quater.isdigit() == False:
#    num_of_quater = input ('Введите номер четверти: ')
#print('Номер четверти: {}'.format(num_of_quater))

# from functions import input_number_test_float#как и советовали - тяну из файла проверку на число

# number = str(input_number_test_float("Enter number : "))

# result = 0

# # схема - при вводе - проверяет на число, но сам number - строчка. По этому я прохожу по каждому эллементу строки, если число , тогда прибавляю к результату
# for i in number:
#     if i.isdigit():
#         result = result+int(i)

# print(f"sum of numbers in {number} = {result}")

# # print (a)
# if a.isdigit() == True:
#     print('all numbers is int')
# else:
#     print('uncorrect items in string, use int numbers')

                                    # 2
# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

                                    # 3
# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

                                    # 4
# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности