from classes_instances import Employee

def email(self):
    return '{}.{}@email.com'.format(self.first,self.last) 

emp_1 = Employee('John','Smith')

emp_1.fullname = 'Alex Koshy'
# emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)