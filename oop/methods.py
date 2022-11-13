import datetime
class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise_amount(cls, amount): #cls - class variable
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:#0-Monday 6-Sunday
            return False
        return True

emp_1 = Employee("Alex", "Koshy", 40000)
emp_2 = Employee("Test", "User", 10000)

emp_1.set_raise_amount(1.04)
print(emp_1.pay)
emp_1.apply_raise()
print(Employee.raise_amount)
print(emp_1.pay)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)

my_date = datetime.date(2022,11,14)

print(Employee.is_workday(my_date))