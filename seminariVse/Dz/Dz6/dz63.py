#3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
# import math       
# Ax = int (input('Введите X для первой точки: '))
# Ay = int (input('Введите y для первой точки: '))
# Bx = int (input('Введите X для второй точки: '))
# By = int (input('Введите y для второй точки: '))
# first_coordinate = (Ax, Ay)
# second_coordinate = (Bx, By)
# # # print (first_coordinate)
# # # print (second_coordinate)
# # AB = √(xb - xa)^2 + (yb - ya)^2
# # distance = math.sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)
# distance =((Bx - Ax) ** 2 + (By - Ay) ** 2)**0.5
# print ('для: ', 'A', first_coordinate, 'B', second_coordinate, 'Расстояние между точками --> ', distance)

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
import math
number_lst = list(map(int,input('Введите координаты точек (x1, x2, y1, y2) через пробел:').split()))
print(number_lst)

def distance_of_two_points(number_lst):
    x1,x2,y1,y2 = number_lst
    return ((x2 - x1) **2 + (y2-y1) **2 )**0.5
print(f'Расстояние между точками: {round(distance_of_two_points(number_lst))}')