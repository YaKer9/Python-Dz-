                                                # 3 
# - Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.561, 10.01] => 0.56 или 56
import random 
random_float_lst = []
for i in range(1,6):
    random_float_lst.append(round(random.uniform(1,2), 2))
print(random_float_lst)

# split_r_f_l = random_float_lst1.split(".")
# only_float_list = split_r_f_l
def min_max(random_float_lst):
    m_min = random_float_lst[0]
    m_max = random_float_lst[0]

    for i in random_float_lst:
        if i < m_min:
            m_min = i
        else:
            if i > m_max:
                m_max = i    
    return round((m_max - m_min), 2)
    
dif_max_min = min_max(random_float_lst)

print(f'Разница между min и max значением дробной части: {min_max(random_float_lst)}') 

# если изначально задать, что первое число будет до точки 1 
# (например, 1.67987807) и т д по списку, то тогда в принцепи прога считает
# разницу того, что останется как раз после запятой между (макс условно 1.567689) -  (и минимальным 1.1367890) = 0.465786.
# Но как написать, что до точки будут разные числа типо (3.458978(мах) и 2.123654(мин)),  
# и посчитать 0.458978 - 0.123654 =..., я не могу придумать