# def square(x):
#     return x*x

# # f=square

# # print(square)
# # print(f(5))


# def cube(x):
#     return x*x*x


# def my_map(func, arg_list):
#     result=[]
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares= my_map(square, [1,2,3,4,5])

# print(squares)


# cubes = my_map(cube, [1,2,3,4,5])

# print(cubes)
    
def logger(msg):

    def log_message():          #closure
        print('Log:',msg,'\n')

    return log_message
    

log_hi = logger('Hi!')
log_hi()

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>\n'.format(tag,msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline')

print_p = html_tag('p')
print_p('Test PAragraph')

