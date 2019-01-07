def is_leap_year(year):
    try:
        return year%400 == 0 or ( year%4 == 0 and year%100 != 0)
    except TypeError:
        print("Enter year number as integer.")
