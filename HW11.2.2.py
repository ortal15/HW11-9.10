# a
print('a:')
str2: str = '   fun-day   '
print(str2)
print('after strip:', str2.strip())
# b
print('b:')
print('is_alphe:', str.isalpha('hello'))
# c
print('c:')
print('is_digit:', str.isdigit('777'))
# d
print('d:')
print('is_space:', str.isspace("   "))
# e
print('e:')
str_e: str = ['N', 'I', 'N', 'J', 'A']
print(str_e)
print('join:', ''.join(str_e))
# f
print('f:')
print('join *:', '*'.join(str_e))
# g
print('g:')
str_g: str = 'hELLo'
print('in,lower:', 'e' in str_g.lower())
# h
print('h:')
sentence: str = input('enter a sentence:')
print("'".join(sentence).upper())
