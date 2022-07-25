#2- Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

#Вариант без множества:

numbers_lst = [10, 20, 30, 40, 10, 40]
print(f'Исходный заданный список:{numbers_lst}')
def get_unique_numbers(numbers_lst):
    unique_lst = []
    for i in numbers_lst:
        if i not in unique_lst: #если нет числа в уникальном списке, то его нужно добавлять в список
            unique_lst.append(i)
    return unique_lst
print(f'Полученный уникальный список: {get_unique_numbers(numbers_lst)}')
