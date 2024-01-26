#  2. Write an if statement to determine whether a variable holding a year
#  is a leap year.

# 366 days in year
leap_year= int(input("Enter the year"))
if (leap_year %4==0 and (leap_year%100!=0 or leap_year%400==0)):  
    print("Variable holding a year is a leap year ! ")
else:
    print("Variable doesnot hold leap year !")