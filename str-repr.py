'''what is the diff btw str() and repr()?'''
''' The goal of __repr__ is to be unambiguous
    the goal of __str__ is to be readable'''
a = [1,2,3,4]
b = 'sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))