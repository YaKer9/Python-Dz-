from curses.ascii import isdigit
from operator import is_


def input_numbers_text_float(text):
    int_test = True
    is_minus = False
    while int_test:
        coord = input(f'{test}')
        if coord[0] == '-':
            is_minus = True
            coord = coord.replace('-', '')
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
    elif coord.isdecimal