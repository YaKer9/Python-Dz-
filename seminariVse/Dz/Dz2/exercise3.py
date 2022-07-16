# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

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
n = num_biger_then_zero("Введите n : ") 
lst_num = {}
for i in range(1, n +1): 
    lst_num[i] = (1 + 1 / i) ** i
print(f'Резултат: {lst_num}')
