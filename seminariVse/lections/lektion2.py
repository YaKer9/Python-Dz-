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

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)            #rekursiya v 4islah fibona4i
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print (list)                #1 1 2 3 5 8 13 21 34

# a, b = 3, 4         #prisvoenie zna4eni peremennih
# (a) = (3, 2, 41, 4)     #kortedj(sostoit iz bolwogo kolli4estva "koordinat")
# print (a)
# print(a[-2])            # kortedj - neizmenyaemi spisok

# a[0] = 12
# a = (3)                   # ne kortedj
# a = (3,)                  #kortedj
# print (a)
# print(a[0])

# a = (3, 5, 4, 2)
# for item in a:
#     print(item)           #for dlya perebora kortedja
# print(item)

# from re import T
# t = tuple(['red', 'green', 'blue'])                     #sozdaem spisok->konvertiruem v kortedj
# red, green, blue = t                                    #kortedj raspakovivaem i prevrawaem egov 3 nezavisimih peremennih
# print('r:{} g:{} b:{}'.format(red, green, blue))        #r:red, g:green, b:blue

########  Словари - неупорядоенные коллекции произвольных объектов с доступом по ключу
# dictionary = {}         # \ - nujen 4tobi ne pisat vse v odnu stro4ku
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)                 # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])         #  ←
# типы ключей могут отличаться
# for k in dictionary.keys():       #klu4i .keys
#     print(k)

# for k in dictionary.values():     #konkretnie zna4eniya .values
#     print(k)

# for v in dictionary:                #klyu4i, kak .keys
#     print(v)
#     print(dictionary[v])            #zna4eniya

# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

#################
# Mnojestva

# colors = {'red', 'green', 'blue'}
# print(colors)                       #tip dannih dlya mnojestv - set
# colors.add('red')                   #ne dobavlyaet odinakovie zna4eniya
# print(colors)
# colors.add('grey')                  #zato dobavlyaet novoe
# print(colors)
# colors.remove('red')                #funkciya udaleniya .remove
# print(colors)               
# # colors.remove('red')              #KeyError...   tak kak red - net
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                         # c = {1, 2, 3, 5, 8} kopirovat
# u = a.union(b)                       # u = {1, 2, 3, 5, 8, 13, 21} ob'edenit
# i = a.intersection(b)                # i = {8, 2, 5} tolko 4tosovpadaet
# dl = a.difference(b)                 # dl = {1, 3}  4to iz a ne vhodit v b
# dr = b.difference(a)                 # dr = {13, 21} 4to iz b ne vhodit v a
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
#                                      # {1, 21, 3, 13}

# list[1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
    
