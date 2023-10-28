def leap_years(year):
    count = 0
    while year>1:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
            count += 1
        year -= 1
    return count



print(leap_years(2000))