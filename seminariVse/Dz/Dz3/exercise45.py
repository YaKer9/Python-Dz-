# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите число членов последовательности:"))
print("Последовательность Фибоначчи:")
new_lst=[]
for i in range(n):
    # print(fibonacci(i))
    new_lst.append(fibonacci(i))
print(new_lst)
neg_liston =[]
my_liston = new_lst
for i in range(1, len(my_liston)):
    neg_liston.append(my_liston[i]*((-1)**(i+1)))

neg_liston.reverse()
# print(neg_liston)
print(f'в том числе отрицательное фибоначи: \n{neg_liston + my_liston}')
# F−n = (−1)^(n+1)*F(n).