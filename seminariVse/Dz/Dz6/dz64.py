#4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# list_rand = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# # print(list_rand)
# need_str = ["qwe"]
# new_str = []
# for i in range (1, len(list_rand)):
#     if list_rand[i] == need_str:
#         new_str.append(i)
# print(new_str)

# def look_up_second_pos(list_wrer,str_what):
#     count = 0
#     for i,item in enumerate(list_wrer):#(0, 'qwe') 
#         if item == str_what:
#             count +=1
#             if count ==2:
#                 break
#     if count>1:
#         return i
#     else:
#         return -1

# text = ["qwe", "asd", "gfe", "zxc", "weq"]
# to_find = "qwe"

# print(f"список: {text}, ищем: '{to_find}', ответ: {look_up_second_pos(text,to_find)}")
####################

lst = ["qwe", "asd", "zxc", "222", "ertqwe", "123"]
find_char = "qwe"

def find_number_in_list(lst, find_char):
    count = 2
    for ind, char in enumerate(lst):
        if char == find_char:
            count = count - 1
            if  count == 0:
                break
    if count < 1:
        return ind
    elif count == 1:
        return 1
    else:
        return -1  
print(f"список: {lst}, ищем: '{find_char}', ответ: {find_number_in_list(lst, find_char)}")

