# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print("Введите элементы последовательности: ")      
num_list = list(map(str, input()))        
print(num_list)
string_num=[]
for element in num_list:                 #тут мы переводим строку из ['2', '4'] В лист [2, 4]
    string_num.append(int(element))
print(string_num)                        #выводим лист какой нам нужен
# rev_string_num = string_num[::-1]      #тут я создавал перевернутую строку, но вроде она ненужна оказалась
# print(rev_string_num)
sum_different_sides= []  

for i in range(1, len(string_num)):      
    sum_different_sides.append(string_num[(i-1)]*string_num[(-1*i)])
print(sum_different_sides)               #тут перемножаю поиндексно с 1го по последний элементы с -1 по -последний
                                         #двигаюсь с краев к другим краям и друг на друга перемножаю(а надо как то к центру =(
                                         # а то они начинают дублироваться)

