#####################

#Задана натуральная степень n. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени n.
# *Пример:
#
# from random import randint
# # n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# #n =4  => x**4 + 8*x**3 + 2*x² + 4*x + 5 = 0
# #Все коэффициенты кроме нулевого могут быть нулем - такого элемента в полиноме не будет
# #если коэффициент равен 1, то 1 указывается только при свободном элементе.При x² + 5 = 0  - это 5.
# N = int(input('Enter the num: '))                   #Вводим число(колличество коэфициентов)
# lst_first = [randint(1, 100)]                       #эта задает первый элемент
# lst_second = [randint(0, 5) for x in range(N-1)]    #эта задает все остальные элементы многочлена
# lst_mnogo4 = lst_first+lst_second                   #обьеденяет оба предыдущих листа


# lst_new = []
# for i in range(N, 0, -1):                           #приводим лист к нужнуму нам виду, добавляем (х и степени)
#     chislo = len(lst_mnogo4)-i
#     lst_new.append(f'{lst_mnogo4[chislo]}*x**{i}')

# for i in range(len(lst_new)-1, 0, -1):              #тут мы убираем некорректные символы
#     if lst_new[i][:lst_new[i].find('*')] == '0':    #ищем срезом есть ли где i равно нулю и удаляем целиком эту часть
#         lst_new.remove(lst_new[i])
#     if lst_new[i][lst_new[i].rfind('*'):] == '*1':  #ищем есть ли 1степень и заменяем ее на пустоту( **1 было "ничего"стало)
#         lst_new[i]=lst_new[i].replace('**1','')     
#     if lst_new[i].startswith('1*'):                 #ищем есть ли впервом элементе коэфицент 1 и заменяем на пустоту(было 1* стало "ничего")
#         lst_new[i]=lst_new[i].replace('1*', '')
    
# result = f'{" + ".join(lst_new)} + {randint(1, 100)} = 0'  #тут мы добавляем "+"" между элементами, добавляем последний элемент 
# with open("resul.txt",'w') as file:                        # без "х" просто чило с рандома и добавляем "=0"
#     file.write(result)

#############################



# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5
# 10/2 * 5




expression = '12+2'
expression1 = []
for i in expression.split('+'):
    expression1.append(i)
operator = []
digits = []
for i, char in enumerate(expression1):
    if char in '-+*/' :
        operator.append(char)
    elif char.isdigit():
        digits.append(char)
print(operator, digits)