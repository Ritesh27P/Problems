def isLeapYear(year):
    if(year % 400 == 0):
        if(year % 4 == 0):
            if (year % 100 == 0):
                return False
        else:
            return True
    
    return False

print(isLeapYear(2000))