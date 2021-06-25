#A leap year is exactly divisible by 4. A century year is a leap year when it is exactly divisible by 400.


def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True    
    else:        
        leap = False
    return leap
    


year = int(input("Enter a year: "))
if is_leap(year):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))