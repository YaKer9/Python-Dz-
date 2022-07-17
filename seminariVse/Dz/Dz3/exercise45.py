# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

def num_biger_then_zero(text):

    int_num = True
    while int_num:
        n = input(f"{text}")
        if n.isdigit():
            n = int(n)
            if n <= 0:
                print("Введите число > 0")
            else:
                int_num = False
        else :
            print("Не число, попробуйте еще раз")
    return n
def fib():
    n = num_biger_then_zero("Введите n : ") 
    my_lst = [0,1]
    i = 2
    while i <= n:
        my_lst.append(my_lst[i -1] + my_lst[i -2])
        i = i +1
    print(f'{my_lst}')    
fib()
# перевернуть список: 
my_list = [1, 2, 3, 4, 5]
my_list. reverse()
print(my_list)
## соединить два списка: 
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print(list_1 + list_2)