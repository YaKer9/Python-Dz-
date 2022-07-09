                                                            #1.
 #  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    #     *Пример:*
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

                                                            #----Complite

# a = int(input('Enter Day: '))
# if a == 6 or a == 7:
#     print ('Day off')
# elif a == 1 or a == 2 or a == 3 or a == 4 or a == 5:      
#     print ('Weekday')
# else:
#     print ('none')
############################

                                                            # 2.
#  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

                                                            #----Complite

# f = False
# t = True
# x = (t, f, f)
# y = (t, f, t)
# z = (f, f, t)
# i = 0
# for i in range (3):
#     a = not(x[i] or y[i] or z[i])
#     b = not x[i] and not y[i] and not z[i]                
#     if a==b:
#         print (True)
#     i += 1
##############################

                                                            # 3.
#  Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#     *Пример:*
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3

                                                            #----Complite

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# if x == 0 or y == 0:
#     print ('Координаты не могутбыть 0')                      
# elif x > 0 and y > 0:
#     print ('1')
# elif x > 0 and y <0:
#     print ('4')
# elif x < 0 and y > 0:
#     print ('2')
# else:
#     print ('3')
#######################

                                                                # 4.
#  Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

                                                                #------Complete

# quarter = int(input('Введите число четверти: '))
# if quarter > 4 or quarter < 1:
#     print ('Change number')
# elif quarter == 1:
#     print ('x > 0 and y > 0')
# elif quarter == 2:
#     print ('x < 0 and y > 0')                                 
# elif quarter == 3:
#     print ('x < 0 and y < 0')
# else:
#     print ('x > 0 and y < 0')
# #########################
                                                                # 5.
#  Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     *Пример:*
    
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21
                                                                #-------Comlite
# import math       
Ax = int (input('Введите X для первой точки: '))
Ay = int (input('Введите y для первой точки: '))
Bx = int (input('Введите X для второй точки: '))
By = int (input('Введите y для второй точки: '))
first_coordinate = (Ax, Ay)
second_coordinate = (Bx, By)
# # print (first_coordinate)
# # print (second_coordinate)
# AB = √(xb - xa)^2 + (yb - ya)^2
# distance = math.sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)
distance =((Bx - Ax) ** 2 + (By - Ay) ** 2)**0.5
print ('для: ', 'A', first_coordinate, 'B', second_coordinate, 'Расстояние между точками --> ', distance)

#пока самые очевидные решения применил)