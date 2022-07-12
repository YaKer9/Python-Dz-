# # print ('hello world')
# #  print ('solder')
# value = None  -   вводим переменную, чтобы заполнять потом(пустую)
# a = 123
# b = 1.23
# # print (type(a)) -   выводим тип данных переменной
# # print(type(b))
# value = 12343
# # print(type(value))
# s='hello'
# print (s)

# print(a, '-', b, '-', s)   -  вывод с разделением/знаком
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')



# f = False - присваеваем верно-неверно
# print (f)

# list = ['1', '2', '3', 'hello'] - строки пишутся так
# print (list)

# print ('введите а')
# a = int (input())
# print ('введите b')
# b = int(input())
# print (a, '+', b, '=', a+b)
# # print ('{} {}'.format(a, b))
# # print (f'{a} {b}')

# a= 1.31232122
# b= 3
# c=round (a*b, 5)  -   знаки после запятой
# print (c)

# a = 3
# a = a + 5 -   так или 
# a+=5      -   так
# print (a)


# a = 1>3
# print (a)

# a = [1, 2]
# b = [1, 2]
# print (a==b)

# a = 1 < 3 < 5
# print (a)

# f= 1>2 or 4<5
# print (f)

# f=[1, 2, 3, 4]
# # print (f)
# # print (not 2 in f)

# is_odd = not f[0] % 2 
# print (is_odd)

# a = int(input('a =')) - как работает иф - элс
# b = int(input('b='))
# if a > b :
#     print (a)
# else:
#     print (b)

# username = input('введите имя: ')
# if username == 'Маша':
#     print ('Ура, это же МАША!')
# elif username == 'Марина':
#     print ('Я так ждал вас, Марина!') -   как работает if, elif, else
# elif username == 'Ильнар':
#     print ('Ильнар - топ')
# else:
#     print ('Привет, ', username)
    
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print (inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)    -   if, else 
#     original //= 10
#     print (original)
# else:
#     print ('Пожалуй')
#     print ('хватит )')
# print (inverted)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# list = range(10)  -   0-10 range  -   cicle for
# for i in range (1, 10, 2):
#     print(i)
# for i in 'qwe - rty':
#     print(i) 

# help (text.istitle)   -   встроеная справка пайтона


# text = 'съешь еще этих французских булок'
# print (text[0])             #c
# print (text[len(text)-1])   #к
# print (text[-5])            #б
# print (text[:])             #принт (текст)
# print (text[2 : 5])         #ешь
# print (text[2 : -18])       #ешь еще этих

# numbers = [1, 2, 3, 4, 5]
# print (numbers)
# ran = range(1, 6)
# print (type(ran))
# numbers = list(ran)    # -   приведение к типу - list
# print (type(numbers))

# print (numbers)
# numbers [0] = 10
# print (f'{len(numbers)} len')
# print (numbers)
# for i in numbers:               #поэлементно умножаем строку на 2
#     i*=2                        #в текущую переменную(i) вкладываем значение НЕ В САМ СПИСОК(numbers)
#     print (i)
# print(numbers)

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print (e*2)

# colors.append('grey')              #добавили в конец новый цвет
# print (colors == ['red', 'green', 'blue', 'grey']) #True
# colors.remove('red')               #del colors[0] #удалить элемент
# print (colors)

# def f(x):
#     if(x)  == 1:
#         return 'целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 1
# print(f(arg))
# print(type(f(arg)))
 