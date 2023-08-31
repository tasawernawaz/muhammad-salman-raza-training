import random

print('Hello world!')

a = int(5)
b = 2
if b > a:
  print(b, 'is greater than', a)
else:
  print(a, 'is greater than', b)

# Single line comments
"""
Multiline
comments!
"""
a = str('changed type')
# print(a, type(a))

x, y, z = 'hi', 'there', 'snake'
# print(x, y, z)
x = y = z = 'Alright'
# print(x, y, z)

def myFunc():
  print('Python is', x)

# myFunc()

# Change a variable inside a function,
# that was originally declared outside a function
change_inside = 2
# print('before', change_inside)
def changeVariable():
  global change_inside
  change_inside = 33

changeVariable()
# print('after', change_inside)

using_e = 12.3e12
using_E = -12.3E12
# print(using_e, using_E)

a = 2
b = 6.8
c = 2j

# convert int to complex
# print('before conversion', a)
a = complex(a)
# print('after conversion', a)

for x in range(5):
  print(random.randrange(1, 10), end=', ' if x < 4 else '')
print()

s = 'Hello, there!'
# print(s[1:5], '---', s[-3:-1], '---', s.upper(), '---', s.lower(), '---', '   Huh    '.strip())

quantity = 2
item_number = 9
placed_order = 'I\u2019ll have {} number {}s' 
placed_order2 = 'I\u2019ll have {1} number {0}s'
# print(placed_order.format(quantity, item_number), '--', placed_order2.format(item_number, quantity))

x = 200
print(isinstance(x, int), isinstance(x, str))

a_list = ['apple', 'banana', 'orange', 'mango']
if 'mangos' in a_list:
  print('we got mangos')

a_list[1:3] = ['borange', 'lanana']
# print(a_list)

a_list.insert(2,'peach')

# Does this work for them? Currently it doesn't
b_list = ['grapes', 'watermelon']
a_list.extend(b_list)
# print(a_list)

del b_list

# [print(x, end= ' ') for x in a_list]
# print()


'''
newlist = [expression for item in iterable if condition == True]
'''

new_list = [x for x in a_list if 'n' in x]
# print(new_list)
new_list.sort()
# print('sorted asc', new_list)
new_list.sort(reverse=True)
# print('sorted desc', new_list)

another_list = ["banana", "Orange", "Kiwi", "cherry"]
another_list.sort(key = str.lower)
print(another_list)

das_set = { 4, 2, 9, 6, 5, 'c', 'a', 'x', 'X', 'x'}
print(das_set)

this_dict = {
  'brand': 'Plymouth',
  'model': 'Roadrunner',
  'year': '1970',
  # 'color': 'blue',
}

# print(this_dict)

# The update() method will update the dictionary with the items from a given argument.
this_dict.update({ 'color': 'golden' })
print(this_dict)
# last added item is removed
this_dict.popitem()
# print(this_dict)
this_dict.update({ 'color': 'golden' })

# Removes specific
del this_dict['color']
print(this_dict)

# These 2 methods prints out keys
# 1
# for x in this_dict:
#   print(x)
# 2
# for x in this_dict.keys():
#   print(x)

# This prints out values
# for x in this_dict.values():
#   print(x)

# This prints out both
for x, y in this_dict.items():
  print('(', x, y, ')', end=' ')
print()

this_dict_copy = dict(this_dict)
this_dict_copy2 = this_dict.copy()

def myFunc():
  test_int = 1
  test_str = 'hi'
  print(test_int + test_str)

# myFunc()

# Sending values by name
def argFunc(arg1, arg2):
  print(arg1, arg2)

arg1 = 3
arg2 = 'hello'
argFunc(arg2 = arg2, arg1 = arg1)
# The following does not work like i thought it would
argFunc(arg2, arg1)

# arbitrary arguemnts as a tuple
def arbitrary_arg(*key):
  print(key[1])
arbitrary_arg('hello', 'there', 'crepe')

# arbitrary arguemnts as keywords
def arbitrary_arg(**key):
  print(key['name'])
arbitrary_arg(greeting = 'hello', direction = 'there', name = 'crepe')
