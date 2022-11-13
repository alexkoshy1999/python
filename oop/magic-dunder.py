
class Employee:

    raise_amt = 1.04

    #__ are called Dunders
    def __init__(self, first, last, pay):#dunder init
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
        
    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    # def __name__(self):
    #     return self.first

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(len('test'))
print('Test'.__len__())
print(emp_1.fullname().__len__())

# print(emp_1)
# print(emp_2)
# print('a'+'b')

# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1+2)
# print(int.__add__(1,2))
# print('a'+'b')
# print(str.__add__('a','b'))
# 
# print(emp_1+emp_2)