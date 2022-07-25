# #- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

# #Пример:
# #- при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

#Ряд Нилаканта:
# π = 3 + 4/(2*3*4) — 4/(4*5*6) + 4/(6*7*8) — 4/(8*9*10) + 4/(10*11*12) — (4/(12*13*14) …
# pi = 3.141
from fileinput import close


def null_counter(num:float):
    '''
    Переносит точку в числе и считает, сколько знаков после точки
    param: num - вещественное число
    return: counter - количество символов после точки, num = int
    '''
    counter = 0
    while num != int(num):
        num*=10
        counter+=1
    return counter, num

d = float(input('enter the d: '))
num_d = null_counter(d)
number_d = num_d[0]
print(number_d)
def find_pi(number_d):
    num = 2
    pi = 3

    
    for i in range(number_d):
        pi += (4 / (num * (num+1) * (num+2))*(1)) + (4 / ((num+2) * (num+3) * (num+4))*(-1))
        num = num+4
        print(pi)
    return pi
print(f'We find pi: {find_pi(number_d)}')

