# coding: utf-8

# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If the first number in the string is greater than or equal 
# to the proceeding number, the proceeding number should be inserted 
# into a sublist. Continue adding to the sublist until the proceeding number 
# is greater than the first number before the sublist. 
# Then add this bigger number to the normal list.

# Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    list_of_numbers = []
    first = int(string[0])
    list_of_numbers.append(first)
    sub_list = []
    for x in range(1, len(string)):
        current_number = int(string[x])
        if current_number > first:
            first = current_number
            if len(sub_list):
                copy_of_sub_list = sub_list.copy()
                list_of_numbers.append(copy_of_sub_list)
                sub_list.clear()
            list_of_numbers.append(current_number)
        else:
            sub_list.append(current_number)
    if len(sub_list):
        list_of_numbers.append(sub_list)
    return list_of_numbers


# testcases
string = '543987'
result = [5, [4, 3], 9, [8, 7]]
print(repr(string), numbers_in_lists(string) == result)
string = '987654321'
result = [9, [8, 7, 6, 5, 4, 3, 2, 1]]
print(repr(string), numbers_in_lists(string) == result)
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print(repr(string), numbers_in_lists(string) == result)
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(repr(string), numbers_in_lists(string) == result)
