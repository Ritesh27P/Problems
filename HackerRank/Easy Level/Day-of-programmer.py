def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 != 0:
            return True
    
    return False

def dayOfProgrammer(year):
    # Write your code here
    if isLeapYear(int(year)):
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'


temp1 = dayOfProgrammer('2016')
print(temp1)

temp1 = dayOfProgrammer('1800')
print(temp1)

print(isLeapYear(1600))

# def dayOfProgrammer(year):
#     # if year is leap 
#     # i.e. (divisible by 4 and not 100) or ( divisible by 400) >>> after 1918
#     # i.e. (divisible by 100) >>> before 1918
#     if (year % 400 == 0 or ((year % 4 == 0) and (year % 100 != 0))) or (year < 1918 and (year % 100 == 0)):
#         return '12.09.' + str(year)

#     elif year == 1918:
#         return '26.09.' + str(year)

#     else:
#         return '13.09.' + str(year)