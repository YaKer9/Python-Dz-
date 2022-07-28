str = "абвгдейка серьезный проек в абвороны, дождь неабвразные абвреатуры"
print(str)
list_of_words = str.split() # разбиваем строку на отдельные символы через запятую
res_list =[]
# def delet_words(list_of_words):
#     res_list =[]
#     for word in list_of_words:
#         if not ('абв' in word) == True:
#             res_list.append (word)
#         else:
#             print('')
#         return res_list
for word in list_of_words:
    if not ('абв' in word) == True:
        res_list.append(word)
    # else:
    #     res_list.append(word)
print(res_list)
result = ' '.join(res_list)
print(f'Введеный текст: {str} \n↓ \nПолученный: {result}')
# print(delet_words(list_of_words))