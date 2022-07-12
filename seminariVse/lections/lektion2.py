# colors = ['red', 'green', 'blue']           #-про а - добавляет еще раз всю запись. w - записывает заново
# data = open('file.txt', 'w')
# # data.writelines(colors) #разделителей не будет
# data.write('LINE121\n')
# data.write('LINE131\n')
# data.close()

# with open('file.txt', 'w') as data:           #peremennaya data(avtmati4eski zakroetsa)
#     data.write('LINE111\n')
#     data.write('LINE2222\n')
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()

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
 
# import lection1 as l                #----function zaimstvovana iz "lection1" i pereimenovano zaimstvovanie na "l"

# print(l.f(1))

# def new_string (symbol, count):
#     return symbol* count
# print (new_string('!', 5))      #!!!!
# print (new_string('!'))         #TypeError missing 1required ...

# def new_string (symbol, count=3):
#     return symbol* count
# print (new_string('!', 5))      #!!!!
# print (new_string('!'))         #!!!
# print (new_string(4))           #12

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res+= item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))     #asdw
# print(concatenatio('a', '1', 'd', '2'))     #a1d2
# print(concatenatio(1, 2, 3, 4))             #TypeError: ...

# def concatenatio(*params):
#     res: int = 0                              #int ne obyazatelen
#     for item in params:
#         res+= item
#     return res
# print(concatenatio(1, 2, 3, 4))               #vivodim tolko numbers

