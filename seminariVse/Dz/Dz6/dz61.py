#1- Определить, присутствует ли в заданном списке строк, некоторое число


numbers_list = list(input('Enter list of numbers: '))
search_number = int(input('Enter serch number: '))
numbers_str = list(map(int, numbers_list))
print(numbers_list)
print(numbers_str)

how_many_numbers = list(filter((lambda x, y: x if x == search_number y+=1 )  , numbers_str))
print(how_many_numbers)