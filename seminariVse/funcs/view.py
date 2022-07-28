
import random

def view_data(data, title):
    print(f'{title}= {data}')

def get_value():
    return int(input('value= '))

def get_sensor():
    return int(random.randint(1, 10))