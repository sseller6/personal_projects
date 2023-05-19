def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline

def get_year_days(year):
    leap_year = is_leap_year(year)
    if leap_year:
        return 366
    else:
        return 365

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
def compute_offset(year,month):
    num_days = 0
    year_count_list = []
    #Line 19 prepares our list of years.
    for x in range(1753, year, 1):
        year_count_list.append(x)
    #Line 22 calculates the number of days.
    for years in year_count_list:
        num_days += get_year_days(years)
    for y in range(1, month, 1):
        num_days += get_month_days(month, year)
    return (num_days + 1) % 7.

def get_month_days(month, year):
    leap_year = is_leap_year(year)
    if month == 2:
        if leap_year:
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31


number_of_days = compute_offset(1753,1)

print(number_of_days)