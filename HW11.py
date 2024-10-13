import random

# a
print('a:')
list_a: list[bool] = [random.choice([True, False]) for _ in range(3)]
print('the list:', list_a)
# b
print('b:')

if not all(list_a):
    print("not all the list is True")
else:
    print('all the list is True')
# c
print('c:')

if any(list_a):
    print('There is at least one True')
else:
    print('all the list is false')
# d
print('d:')

if not any(list_a):
    print('all the list is false')
else:
    print('not all the list is false')
# e
print('e:')

if all(list_a):
    print('there is not 1 false in tje list')
else:
    print('there is at least one false')
# f
print('f:')

list_f: list[int] = [random.randint((-2), 2) for i in range(5)]
print('list_f:', list_f)
# g
print('g:')

if all([number != 0 for number in list_f]):
    print('All numbers are different from 0')
else:
    print('not all numbers are different from 0')
# h
print('h:')

if any(num != 0 for num in list_f):
    print('There is a number that is different from 0 ')
else:
    print('There is no single number that is different from 0')
# i
print('i:')

if all(number == 0 for number in list_f):
    print('The entire list contains 0')
else:
    print('The list does not consist only of 0')
# j
print('j:')

if any(num == 0 for num in list_f):
    print('there is 0 in the list')
else:
    print('there is no 0 in the list')
