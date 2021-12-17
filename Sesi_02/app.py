# x = 0
# y = 5
# if x < y:
#     print('yes')
# if y < x:
#     print('yes')
# if x:
#     print('yes')
# if y:
#     print('yes')
# if 'aul' in 'grault':
#     print('yes')
# if 'quux' in ['foo', 'bar', 'baz']:
#     print('yes')

# if 'foo' in ['bar', 'baz', 'qux']:
#     print('Expression was true')
#     print('Executing statement in suite')
#     print('...')
#     print('Done.')
# print('After conditional')

# if 'foo' in ['foo', 'bar', 'baz']:
#     print('Outer condition is true')
#     if 10 > 20:
#         print('Inner condition 1')
#     print('Between inner conditions')
#     if 10 < 20:
#         print('Inner condition 2')
#     print('End of outer condition')
# print('After outer condition')

# x = 20
# if x < 50:
#     print('(first suite)')
#     print('x is small')
# else:
#     print('(second suite)')
#     print('x is large')

# x = 120
# if x < 50:
#     print('(first suite)')
#     print('x is small')
# else:
#     print('(second suite)')
#     print('x is large')

# hargaBuku = 20000
# hargaMajalah = 5000
# uang = 2000

# if uang > hargaBuku:
#     print("beli buku")
# else:
#     print("uang tidak cukup")

# hargaBuku = 20000
# hargaMajalah = 5000
# uang = 2000
# if uang > hargaBuku:
#     print("beli buku")
# elif uang > hargaMajalah:
#     print("beli majalah")
# else:
#     print("uang tidak cukup")

# name = 'Hacktiv8'
# if name == 'Fred':
#     print('Hello Fred')
# elif name == 'Xander':
#     print('Hello Xander')
# elif name == 'Hacktiv8':
#     print('Hello Hacktiv8')
# elif name == 'Arnold':
#     print('Hello Arnold')
# else:
#     print("I don't know who you are!")

# if 'a' in 'bar':
#     print('foo')
# elif 1/0:
#     print("This won't happen")
# elif var:
#     print("This won't either")

# if 'f' in 'foo': print('1'); print('2'); print('3')

# if 'z' in 'foo': print('1'); print('2'); print('3')

# x = 2
# if x == 1: print('foo'); print('bar'); print('baz')
# elif x == 2: print('qux'); print('quux')
# else: print('corge'); print('grault')

# x = 3
# if x == 1: print('foo'); print('bar'); print('baz')
# elif x == 2: print('qux'); print('quux')
# else: print('corge'); print('grault')

# x = 3
# if x == 1:
#     print('foo')
#     print('bar')
#     print('baz')
# elif x == 2:
#     print('qux')
#     print('quux')
# else:
#     print('corge')
#     print('grault')

# raining = False
# print("Let's go to the", 'beach' if not raining else 'library')

# raining = True
# print("Let's go to the", 'beach' if not raining else 'library')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break # Break Statement
#     print(n)
# print('Loop ended.')

# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n)
# print('Loop ended.')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Loop done.')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
#     if n == 2:
#         break
# else:
#     print('Loop done.')

# if age < 18:
#     if gender == 'M':
#         print('son')
#     else:
#         print('daughter')
# elif age >= 18 and age < 65:
#     if gender == 'M':
#         print('father')
#     else:
#         print('mother')
# else:
#     if gender == 'M':
#         print('grandfather')
#     else:
#         print('grandmother')

# n = 5
# while n > 0: n -= 1; print(n)

# a = ['foo', 'bar', 'baz']
# for i in a:
#     print(i)

# d = {'foo': 1, 'bar': 2, 'baz': 3}
# for k in d:
#     print(k)

# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         break
#     print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)