                                                        # 4 
# - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

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
bin_num = ''  # Здесь скорее всего надо через функцию делать 
while n > 0: # выше уже есть проверка, вот не знаю нужно ли здесь условие 
    bin_num = str(n % 2) + bin_num # прибавляем к остатку результат деления 
    n = n // 2 # новое частное делим на два 

print(f'Двоичное число: {bin_num}')