                                            # 2 
# - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



print('Число поленились с ввода задать, написал сразу внутри: ')
string_num = [2, 1, 7, 3, 4, 8]
new_str = []
for el in string_num:
    el = int(el)
    new_str.append(el)
print(new_str)
sum_different_sides= []
for i in range(0, int(len(new_str)/2)):      
    sum_different_sides.append(new_str[i]*new_str[-(1+i)])
print(f'Выводим произведение крайних элементов списка: \n{sum_different_sides}')
                                         #тут перемножаю поиндексно с 1го по последний элементы с -1 по -последний
                                         #двигаюсь с краев к другим краям и друг на друга перемножаю(а надо как то к центру =(
                                         # а то они начинают дублироваться)

# print("Введите элементы последовательности: ")      
# num_list = list(map(str, input()))        
# print(num_list)
# string_num=[]
# for element in num_list:                 #тут мы переводим строку из ['2', '4'] В лист [2, 4]
#     string_num.append(int(element))
# print(string_num)                        #выводим лист какой нам нужен
# rev_string_num = string_num[::-1]      #тут я создавал перевернутую строку, но вроде она ненужна оказалась
# print(rev_string_num)
# a = int(len(string_num))
# print(a)
