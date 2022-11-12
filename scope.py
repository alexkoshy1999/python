'''
LEGB
Local, Enclosing, Global, Built-in
'''
import builtins

# print(dir(builtins))

# def my_min(): #builtin scope #min([5,1,2,4,3]) checks for global min(def min()) then checks for builtins so changed min() as my_min
#     pass

# m = min([5,1,2,4,3])
# print(m)
x = 'global x' #global scope

# def test(z):
#     global x
#     y = 'local y' #local scope
#     x = 'local x'
#     print(y)
#     print(z)

# test('local z')
# print(y)
def outer():
    x = 'outer x' #enclosing scope

    def inner():
        nonlocal x
        x = 'inner x' 
        print(x)
    
    inner()
    print(x)
outer()
print(x)

# for a in range(2):
#     x = 'global {}'.format(a)


# def outer():
#     # x = 'outer x'
#     for b in range(3):
#         x = 'outer {}'.format(b)

#     def inner():
#         # x = 'inner x'
#         for c in range(4):
#             x = 'inner {}'.format(c)
#         print(x)
#         print(a, b, c)

#     inner()
#     print(x)
#     print(a, b)

# outer()
# print(x)
# print(a)