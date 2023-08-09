# coding: utf-8

# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    letter = letter.lower()
    alphabet_list = [chr(ord('a') + i) for i in range(26)]

    current_position = alphabet_list.index(letter)
    new_steps = n % 26
    if (n < 0):
        new_steps -= 26

    new_position = (current_position + new_steps) % 26
    return alphabet_list[new_position]

def rotate(string, number):
    new_string = ''
    for letter in string:
        if (not letter.isspace()):
            new_string += shift_n_letters(letter, number)
        else: 
            new_string += ' '
    return new_string

print(rotate('sarah', 13))
# >>> 'fnenu'
print(rotate('fnenu', 13))
# >>> 'sarah'
print(rotate('dave', 5))
# >>>'ifaj'
print(rotate('ifaj', -5))
# >>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))
# >>> ???
