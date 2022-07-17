                                    # 2
# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def num_biger_then_zero(text):

#     int_num = True
#     while int_num:
#         n = input(f"{text}")
#         if n.isdigit():
#             n = int(n)
#             if n <= 0:
#                 print("Введите число > 0")
#             else:
#                 int_num = False
#         else :
#             print("Не число, попробуйте еще раз")
#     return n
# n = num_biger_then_zero("Введите n : ") 
# list = [1]
# for i in range(1, n):
#     list.append(list[i-1] * (i+1))          # [0] - 1 , 2 * (2 + 1) = 6, 6 * 4 = 24
# print(f'Результат: {list}')
neg_liston =[]
my_liston = [0, 1, 1, 2, 3, 5]
for i in range(1, len(my_liston)):
    neg_liston.append(my_liston[i]*((-1)**(i+1)))
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)
neg_liston.reverse()
print(neg_liston)
print(neg_liston + my_liston)
# F−n = (−1)^(n+1)*F(n).

# def fib(n):
#     cur = 1
#     old = 1
#     i = 1
#     while (i < n):
#         cur, old, i = cur+old, cur, i+1
#     return cur

# for i in range(10):
#     print(fib(i))

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите число членов последовательности:"))
print("Последовательность Фибоначчи:")
a=[]
for i in range(n):
    print(fibonacci(i))
    a.append(fibonacci(i))
print(a)
neg_liston =[]
my_liston = a
for i in range(1, len(my_liston)):
    neg_liston.append(my_liston[i]*((-1)**(i+1)))

neg_liston.reverse()
print(neg_liston)
print(neg_liston + my_liston)
# F−n = (−1)^(n+1)*F(n).
