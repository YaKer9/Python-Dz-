                                    # 4
# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from time import time 
num = int(input('Введите число от 1 до 1000000:'))
x = time()                       #  число из библ time 
strNum = str(num)    
print(x)             
strNum = strNum.replace('.','')    
number = int(strNum)
rnd_num = x//number
print(f'Результат:{rnd_num}')
