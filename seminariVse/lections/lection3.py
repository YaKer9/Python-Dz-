
# def f(x):
#     return x**2

# g = f

# # print(f(4))
# # print(g(4))

# def calc1(x):
#     return x+10

# def calc2(x):
#     return x*10
# # print(calc2(10))

# def math(op, x):
#     print (op(x))

# math(calc2,10)
# math(calc1,10)

#################

# def sum(x,y):
#     return x+y

# sum = lambda x, y: x + y + 1

# def mylt(x,y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return (a, b)

# calc(lambda x, y: x + y, 4, 5)

###########

# List Comprehension
# [exp for item in iterable]

# [exp for item in iterable (if conditional)]

# [exp <if conditional> for item in iterable (if conditional)] - 4toto strawnoe

# list = []
# for i in range(1, 100):
#     # if(i%2==0):
#     list.append(i)

# print(list)


# def f(x):
#     return x**3

#         #vskobkah nije kortej
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

#################

##############
# path = 'text.txt'               #peremennaya text.txt
# f = open(path, 'r')             #otkrivaem text i vitaskivaem ottuda vse
# data = f.read() + ' '           #stroka data - vse 4to est' v file + iskusstvenni probel
# f.close()

# numbers = []

# while data != '':               #prohodim po stroke (poka ne pustaya)
#     space_pos = data.index(' ') #naiti 1 posiciyu probela
#     numbers.append(int(data[:space_pos])) #vzyat' vse 4to ot 1 simvola do posicii 1 probela,
#                                           #prevratit v 4islo i dobavit v spisok nomerov
#     data = data[space_pos+1:]   #obnovlyaem stroku s u4etom togo 4to dobavili i 4to bolwe ne nujno ispolzovat

# out = []
# for e in numbers:               #idem po numbers
#     if not e % 2 :              
#         out.append((e, e**2))   #esli 4etnoe zapisivem v novi spisok kortej koordinati - 4etnoe 4islo i ego kvadrat
# print (out)                     #vivodim na ekran

##############

# def select(f, col):                     #funk prinimaet funkciyu i nabor dannih
#     return [f(x) for x in col]          #formiruem novi spisok i srazu ego vozvrawat(funkciyu i 4islo)

# def where(f, col):                      #funk prinimaet funkciyu i nabor dannih
#     return[x for x in col if f(x)]      #vozvrawaet spisok x, idem po col esli rabotaet f(x)
#                                         #est' vstroennaya funk - map() vmesto nawei where


# data = '1 2 3 5 8 15 23 38'.split()     #sozdaem nabor strok iz stroki

# res = select(int, data)                 #int - funkciya prevrowaet v 4islo nabor dannih - data
# res = where(lambda x: not x%2, res )    #labda proveryaet dlya kajdogo x vozvrawaet resultat dlya 4etnih 4isel
#                                         #i resultat s pred etapa
# res = select(lambda x: (x, x**2), res)  #1 - labda prinimayuwaya x i vozvrawayuwaya kortej(x, x**2), 2 prediduwi res
# print (res)

# #########################             #MAP

# f(x) => x+10              1 
# map(f, [1, 2, 3, 4, 5])   #tak rabotaet map

#        [11 12 13 14 15]


# li = [x for x in range (1, 20)]       #zadali spisok v odnu stroku
# li = list(map(lambda x: x+10, li))    #primenili funkciyu k spisku 4ereaz map
# print(li)

##############

# data  = list(map(int, '1 2 3 4 43 22'.split()))  #kak rabotaet map
# print(data)
# for e in data:
#     print(e*10)

# print('--')

# for e in data:
#     print(e*10)

################

# def where(f, col):                      #funk prinimaet funkciyu i nabor dannih
#     return[x for x in col if f(x)]      #vozvrawaet spisok x, idem po col esli rabotaet f(x)
#                                         #est' vstroennaya funk - map() vmesto nawei where


# data = '1 2 3 5 8 15 23 38'.split()     #sozdaem nabor strok iz stroki

# res = list(map(int, data))               #int - funkciya prevrowaet v 4islo nabor dannih - data
# res = where(lambda x: not x%2, res )    #labda proveryaet dlya kajdogo x vozvrawaet resultat dlya 4etnih 4isel
#                                         #i resultat s pred etapa
# res = list(map(lambda x: (x, x**2), res))  #1 - labda prinimayuwaya x i vozvrawayuwaya kortej(x, x**2), 2 prediduwi res
# print (res)

############                            #FILTER

## Функция filter() применяет указанную функцию к
## каждому элементу итерируемого объекта и
##возвращает итератор с теми объектами, для
## которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])  #sna4ala funkciya obrabotki dannih  a potom sami dannie
#  ↓
#  [ 2, 4 ]
## Нельзя пройтись дважды

####

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)

# ######                                #rewili 4erez map i filter
# data = '1 2 3 5 8 15 23 38'.split()     #sozdaem nabor strok iz stroki

# res = map(int, data)               #int - funkciya prevrowaet v 4islo nabor dannih - data
# res = filter(lambda x: not x%2, res)   #labda proveryaet dlya kajdogo x vozvrawaet resultat dlya 4etnih 4isel
#                                         #i resultat s pred etapa
                                        
# res = list(map(lambda x: (x, x**2), res))  #1 - labda prinimayuwaya x i vozvrawayuwaya kortej(x, x**2), 2 prediduwi res
# print (res)

# #############                             #ZIP
# 
# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓                                        
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды'

################

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [3, 2, 12, 4, 9]
# salary = [ 111, 222, 333]
# common = list(zip(users, ids, salary))      # ob'edenyaet v kortej po naimenwemu 4islu elementov v ob'edenyaemih strokah
# print(common)

###################                     #ENUMERATE

# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# common = list(enumerate(users))      # ob'edenyaet v kortej po naimenwemu 4islu elementov v ob'edenyaemih strokah
# print(common)

#######################