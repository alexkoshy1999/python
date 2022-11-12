# def hello_func():
#     pass
# print(hello_func())



# print('Hello Function!') #any changes should be done to all as function only once
# print('Hello Function!')
# print('Hello Function!')
# print('Hello Function!')

# def hello_func():
#     print('Hello Function!')

# hello_func()
# hello_func()
# hello_func()
# hello_func()

# def hello_func(greeting, name = 'You'):
#     return '{} {}'.format(greeting, name) 

# print(hello_func().upper())

# print(hello_func('Hi', name = 'Alex'))

# def student_info(*args, **kwargs):
#     print(args) #positional arguments
#     print(kwargs) #keyword arguments
# courses = ['math', 'art']
# info={'name': 'Alex', 'age': 23}

# student_info('math','art',name='Alex',age=23)
# student_info(courses,info)
# student_info(*courses,**info) 


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years.""" # doc string

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))
print(days_in_month(2020,2))








# Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""

#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# def days_in_month(year, month):
#     """Return number of days in that month in that year."""

#     if not 1 <= month <= 12:
#         return 'Invalid Month'

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]