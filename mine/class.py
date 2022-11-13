# import datetime

class Employee():
    def __init__(self,fname,lname,email,dob):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.dob = dob

n = int(input('No of enteries: '))
empl = {}
for i in range(n):
    fname = input('Enter your First name: ')
    lname = input('Enter your Last name: ')
    email = input('Enter your Email Address: ')
    dob = input('Enter date of birth in the format \'DD/MM/YYYY\': ')
    # dob1 = datetime.datetime.strptime(dob,'%d/%m/%Y')
    empl[i]  = Employee(fname,lname,email,dob)
    print(empl[i].__dict__)


