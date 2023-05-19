# 1. Name:
#      Steven Sellers
# 2. Assignment Name:
#      Lab 03: Calendar
# 3. Assignment Description:
#      The purpose of this program is to receive user input and display an output of a desired calendar month.
# 4. What was the hardest part? Be as specific as possible.
#      The assignment went well. It took me about 6 hours to finish. The hardest part for me was figuring out the compute offset part. 
#      Despite having been provided pseudocode for that portion, it was still very difficult for me to figure it out.
# 5. How long did it take for you to complete the assignment?
#      The total time it took me to complete the assignment was about 6 hours. That includes reading the instructions.

# This portion of the code is where we define functions.
def compute_offset(year,month):
    num_days = 0
    year_count_list = []
    # Line 19 prepares our list of years.
    for x in range(1753, year, 1):
        year_count_list.append(x)
    # Line 22 calculates the number of days.
    for years in year_count_list:
        num_days += get_year_days(years)
    for y in range(1, month, 1):
        num_days += get_month_days(month, year)
    offset = (num_days + 1) % 7.
    offset = int(offset)
    return offset

# The purpose of this function is to display the calendar table. end='' is used to make sure the end of each print statment doesn't start a new line on the console.
def display_table(offset, days):
    print("  Su  Mo  Tu  We  Th  Fr  Sa")
    for i in range(offset):
        print("    ", end='')
    for x in range(1, days + 1):
        # Converts int into a string.
        print(repr(x).rjust(4), end='')
        offset += 1
        if offset % 7 == 0:
            print("")

    if offset % 7 != 0:
        print("")

# The purpose of this function is to return the number of days in a month. The year parameter is required to determine if the month of February is a leap year or not.
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

#This function's purpose is to return how many days are in a year.
def get_year_days(year):
    leap_year = is_leap_year(year)
    if leap_year:
        return 366
    else:
        return 365

#This function's purpose is to get a valid month input.
def get_month():
    month = input('Enter a month number: ')
    invalid = True
    is_number = month.isnumeric()
    while invalid:
        if is_number == True:
            month = int(month)
            if 0 < month < 13:
                invalid = False
            elif 0 >= month or month >= 13:
                invalid = True
                month = input('Month must be between 1 and 12. ')
        elif is_number == False:
            invalid = True
            month = input('Month must be an integer. ')
            is_number = month.isnumeric()
    return month

#This function's purpose is to get a valid year input.
def get_year():
    year = input('Enter Year: ')
    invalid = True
    while invalid:
        is_number = year.isnumeric()
        if year == '-1':
            is_number = True
        if is_number:
            year = int(year)
            if year >= 1753:
                invalid = False
            elif year < 1753:
                invalid = True
                year = input('Year must be 1753 or later. ')
        elif is_number == False:
            invalid = True
            year = input('Year must be an integer. ')

    return year

# The purpose of this function is to determine if the year is a leap year or not.
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def main():
    month = get_month()
    year = get_year()
    offset = compute_offset(year,month)
    days = get_month_days(month,year)
    display_table(offset,days)
    
main()