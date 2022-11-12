# def outer_function():
#     message = 'Hi'

#     def inner_function():
#         print(message)

#     return inner_function()

# outer_function()



# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)

#     return inner_function

# hi_func = outer_function('Hi')
# hello_func = outer_function('Hello')

# hi_func()
# hello_func()



# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function

# def display():
#     print('display function ran')

# decorated_display = decorator_function(display)

# decorated_display()


# def decorator_function(original_function):
#     def wrapper_function(*args,**kwargs):
#         print('Wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function
# def display():
#     print('display function ran')

# @decorator_function
# def display_info(name,age):
#     print('display_info ran with arguments ({},{})'.format(name,age))

# display_info('Alex', 23)

# display()



# def decorator_function(original_function):
#     def wrapper_function(*args,**kwargs):
#         print('Wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args,**kwargs)
#     return wrapper_function

# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
    
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)


# @decorator_class
# def display():
#     print('display function ran')

# @decorator_class
# def display_info(name,age):
#     print('display_info ran with arguments ({},{})'.format(name,age))

# '''no need of @decorator_class'''
# # decorated_display = decorator_class(display_info)
# # decorated_display('Alex', 23)
# '''or'''
# # display_info('Alex', 23)

# display()

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig_func(*args,**kwargs)

    return wrapper
    
import time
def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        t1= time.time()
        result = orig_func(*args,**kwargs)
        print(result)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name,age))
    return 1

# display_info1 =  my_timer(my_logger(display_info)) #my_timer(display_info) = wrapper (as returned by my_timer)
# display_info1('Hank', 25)
display_info('Hank', 25)
print(display_info.__name__)





