# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print("Введите элементы последовательности: ")      
list_ok = list(map(str, input()))           #Вводим числа без пробелов для заполнения строки
odd_list_ok = list_ok[1::2]                 #  заносим нечетные элементы в отдельную строку(list_ok[1::2] - list_ok[START:STOP:STEP]
                                            #  - берёт срез от номера START, до STOP (не включая его),с шагом STEP.
                                            #  По умолчанию START = 0, STOP = длине объекта, STEP = 1)
print (f'all odd elements in enter numbers {odd_list_ok}')  #выводим на экран нечетные числа
ints=[]
for element in odd_list_ok:                 #тут мы переводим строку из ['2', '4'] В лист [2, 4]
    ints.append(int(element))
print(f'convert elements to list: {ints}')  #выводим лист с нечетными элементами
print("sum of odd elements: ", sum(ints))   #выводим сумму элементов нашего листа(тутже и складываем в принте)

#правда без всяких проверок))