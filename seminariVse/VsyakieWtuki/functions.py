

def input_numbers_text_float(text): #Проверка на число
    int_test = True
    is_minus = False
    while int_test:
        coord = input(f'{text}')
        if coord[0] == '-':
            is_minus = True
            coord = coord.replace('-', '')
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        elif coord.isdecimal():
            coord = float(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else:
            print('Not a number, try again')
    return coord

#################################

def input_nuber_bigger_than_zero(numb):
    
    while True:
        number = input(f'{numb}')
        if float(number) > 0:
            True
        else:
            False
            print('try again')
            
        return number

####################
from ctypes import string_at
import time

def factorial(number):
    if number == 0:
        return 1
    return number*factorial(number - 1)

def main():
    n = int(input('Введите натуральное число: '))
    lst = []
    for i in range (1, n+1):
        lst.append(factorial(i))
    print(lst)

if __name__ == "__main__":
    main()

########

def my_random(min=0, max=10):
    result = min -1
    digit_num = len(str(max))
    while result < min or result > max:
        string_time - str(time.time_ns()//100)
        ##print(string_time)
        result = int(string_time[-digit])
        