# def outer_func():
#     message = 'Hi'

#     def inner_func():
#         print(message)

#     return inner_func()

# outer_func()

# def outer_func(msg):
#     message = msg

#     def inner_func(a):
#         print(message,a)

#     return inner_func

# my_func = outer_func('Hi!')
# my_func('Alex')
# my_func('Reji')
# my_func('Pappa')

import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)