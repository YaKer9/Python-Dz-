                                            # 2 
# - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print("Введите элементы последовательности: ")      
num_list = list(map(str, input()))        
print(num_list)
string_num=[]
for element in num_list:                 #тут мы переводим строку из ['2', '4'] В лист [2, 4]
    string_num.append(int(element))
print(string_num)
rev_string_num = string_num[::-1]
print(rev_string_num)
sum_different_sides= []  
# for i in range(0,len(string_num)):
#     sum_different_sides.append(string_num[i]*rev_string_num[i])
# for i in range(0, len(string_num)):
#     sum_different_sides.append(string_num[i]*string_num[-1*i])

# print(sum_different_sides)
