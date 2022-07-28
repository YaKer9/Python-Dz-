#4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах
#RLE) или кодирование повторов — алгоритм сжатия данных, заменяющий повторяющиеся 
#символы (серии) на один символ и число его повторов. Серией называется последовательность, состоящая из нескольких одинаковых символов.
#RLE означает “run-length encoding” — это способ сокращённой записи последовательности чего угодно (в случае этой задачи — цифр), 
# при котором для подряд идущих группы одинаковых цифр (run) записываются длина этой группы (run length) и сама эта цифра. 
# Таким образом, “99999” превратится в “5 9” («пять девяток»), и так далее. 

from importlib.resources import path

file = open('RLE.txt' , "w",encoding='utf-8') #записыаем и создаем файл
file.write("FFFFFAAAAABBBB")
file.close()

path = 'RLE.txt'
file = open('RLE.txt' , "r",encoding='utf-8') #считываем из файла строку
data = file.read()
file.close()
string = data
def encode(string):
 
    encoding = "" # сохраняет выходную строку
 
    i = 0
    while i < len(string):
        # подсчитывает количество вхождений символа в индексе i
        count = 1
 
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + string[i]
        i = i + 1
 
    return encoding
print(encode(string))

file = open('result.txt' , "w",encoding='utf-8') #записыаем и создаем файл
file.write(encode(string))
file.close()