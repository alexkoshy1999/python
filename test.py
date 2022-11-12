month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def leap_yr(yr):
    return yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)
# y=leap_yr(yr=int(input('enter yr: ')))
# if y == True:
#     print("true")
# else:
#     print('False')

def month(y,m):
    if not 1<=m<=12:
        return 'invalid month'
    if m==2 and leap_yr(y):
        return 29
    return month_days[m]
print(month(int(input('Enter yr: ')),int(input('enter month: '))))

