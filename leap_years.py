def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) :
        return True
    
def leap_years(century):
    start_year = (century - 1) * 100
    end_year = (century * 100) - 1
    tab = []
    for i in range(start_year, end_year + 1):
        if is_leap(i) == True :
            tab.append(i)
    return tab

year = int(input("Enter a year: "))
if is_leap(year) == True :
    print(f"The year {year} is leap")
else:
    print(f"The year {year} is not leap")

century = int(input("Enter a century (in numbers): "))
print("The leap years in this century are:\n",leap_years(century))
