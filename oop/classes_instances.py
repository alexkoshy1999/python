class Employee:
    def __init__(self , first , last , pay = None):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last) 

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last) 

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Alex' , 'Koshy' , 15000)
emp_2 = Employee('Test' , 'User' , 10000)

# print(emp_1)
# print(emp_2)

# print(emp_1.pay)
# print(emp_2.email)

# print(emp_2.fullname)
# print(Employee.fullname(emp_1))