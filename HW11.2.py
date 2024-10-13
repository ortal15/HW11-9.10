str1: str = 'ortal istacharov netanya'
print(str1)
# a
print('a:')
print('len:', len(str1))
# b
print('b:')
print('upper:', str1.upper())
# c
print('c:')
print('lower:', str1.lower())
# d
print('d:')
print('start with:', str1.startswith('ortal'))
# e
print('e:')
print('end with:', str1.endswith('netanya'))
# f
print('f:')
print('split:', str1.split())
# g
print('g:')
print('replace:', str1.replace(' ', '*'))
print('split back:', str1.split())
# h
print('h:')
print('center', str1.center(50, '='))
# i
print('i:')
print('index 4:', str1[4:])
# j
print('j:')
print('index 1-4:', str1[:5])
# k
print('k:')
print('even characters:', str1[::2])
# l
print('l:')
print('title:', str1.title())
