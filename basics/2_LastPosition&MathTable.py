# coding: utf-8

# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

def print_multiplication_table(n):
    if not isinstance(n, int) or n <= 0:
        return print('Value must be an integer greater than zero')
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            print(x, '*', y, '=', x * y)


print_multiplication_table(2)
# >>> 1 * 1 = 1
# >>> 1 * 2 = 2
# >>> 2 * 1 = 2
# >>> 2 * 2 = 4

print_multiplication_table(3)
# >>> 1 * 1 = 1
# >>> 1 * 2 = 2
# >>> 1 * 3 = 3
# >>> 2 * 1 = 2
# >>> 2 * 2 = 4
# >>> 2 * 3 = 6
# >>> 3 * 1 = 3
# >>> 3 * 2 = 6
# >>> 3 * 3 = 9
