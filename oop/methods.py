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

    @classmethod
    def set_raise_amt(cls, amount):
        pass


emp_1 = Employee("Alex", "Koshy", 40000)
emp_2 = Employee("Test", "User", 10000)

print(Employee.num_of_emps)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# Employee.raise_amount = 1.04
# emp_1.raise_amount = 1.04

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.fullname())
print(emp_2.raise_amount)

# emp_1.raise_amount
# Employee.raise_amount
