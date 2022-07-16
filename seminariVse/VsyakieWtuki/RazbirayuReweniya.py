from functions import input_numbers_text_float
number = str(input_numbers_text_float('Enter number: '))
result = 0
for i in number:
    if i.isdigit():
        result = result + int(i)
print(f'sum of numbers in {number} = {result}')
