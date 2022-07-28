#2- Найти сумму чисел списка стоящих на нечетной позиции
# list_nums = [1, 2, 3, 12, 5, 6]
# list_nums_ind = [x for x in range(1, len(list_nums))]
# print(list_nums_ind)
# odd_nums = list(filter(lambda x: not list_nums[x] % 2==0, list_nums_ind))
# print(odd_nums)

# def sum_nums(odd_nums, list_nums):
#     sum = 0
#     for i in range(0, len(list_nums)):
#         if i == odd_nums[0]:
#             sum += list_nums[i]
#             odd_nums[]
#             print(sum)

# print(sum_nums(odd_nums, list_nums))



#############
# 2- Найти сумму чисел списка стоящих на нечетной позиции

def sum_on_not_odd_pos(list_of_num : list):
    sum_of_num = 0
    for i in list(filter(lambda a : list_of_num.index(a)%2 != 0  , list_of_num)):
        sum_of_num += i
    return sum_of_num

list_of_num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"sum of nums on not odd places in {list_of_num} => {sum_on_not_odd_pos(list_of_num)} ")
