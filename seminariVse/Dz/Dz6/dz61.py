# #1- Определить, присутствует ли в заданном списке строк, некоторое число

number_lst = list(input('Введите список чисел:'))
print(' '.join(number_lst))
number = input('Введите число:')
def find_number(number_lst : str,number : str):
    return len(list(filter(lambda x : x in number_lst, number_lst))) > 0
print(f"{number} в списке : '{number_lst}' - > {find_number(number_lst,number)}")

# def reult_bool(text, number):
#     return len(list(filter((lambda x: x == search_number, numbers_str))))>0

# numbers_list = list(input('Enter list of numbers: '))
# search_number = str(input('Enter serch number: '))
# numbers_str = list(map(int, numbers_list))
# result_re = list(filter(lambda x: x == search_number, numbers_str))
# print(result_re)