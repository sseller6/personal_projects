"""
I will need to break the program down into different sections. I want the program to do the following things:
1. Use a dictionary that is found in a CSV file to either append, edit, or delete information
2. 

Plan:
 - Function that searches if an address book is in the system already; (scans a CSV file if it's compatible)
 - Function that asks the user if they would like to view, edit (append/delete) the dictionary. (and close the program)
 - Function that opens the dictionary (in the other file)
 - Function that asks what they would like to edit (name, PTN, email, address, DELETE)
 - Function that closes the dictionary
"""

from tkinter import LAST
from unittest import skip

#Indexes

FIRST_NAME_INDEX = 0
MIDDLE_NAME_INDEX = 1
LAST_NAME_INDEX = 2
TITLE_INDEX = 3
SUFFIX_INDEX = 4
INITIALS_INDEX = 5
WEB_PAGE_INDEX = 6
GENDER_INDEX = 7
BIRTHDAY_INDEX = 8
ANNIVERSARY_INDEX = 9
LOCATION_INDEX = 10
LANGUAGE_INDEX = 11
INTERNET_FREE_BUSY_INDEX = 12
NOTES_INDEX = 13
EMAIL_ADDRESS_INDEX = 14
EMAIL_2_ADDRESS_INDEX = 15
EMAIL_3_ADDRESS_INDEX = 16
PRIMARY_PHONE_INDEX = 17
HOME_PHONE_INDEX = 18
HOME_PHONE_2_INDEX = 19
MOBILE_PHONE_INDEX = 20
PAGER_INDEX = 21
HOME_FAX_INDEX = 22
HOME_ADDRESS_INDEX = 23
HOME_STREET_INDEX = 24
HOME_STREET_2_INDEX = 25
HOME_STREET_3_INDEX = 26
HOME_ADDRESS_PO_BOX_INDEX = 27
HOME_CITY_INDEX = 28
HOME_STATE_INDEX = 29
HOME_POSTAL_CODE_INDEX = 30
HOME_COUNTRY_INDEX = 31
SPOUSE_INDEX = 32
CHILDREN_INDEX = 33
MANAGERS_NAME_INDEX = 34
ASSISTANTS_NAME_INDEX = 35
REFERRED_BY_INDEX = 36
COMPANY_MAIN_PHONE_INDEX = 37
BUSINESS_PHONE_INDEX = 38
BUSINESS_PHONE_2_INDEX = 39
BUSINESS_FAX_INDEX = 40
ASSISTANTS_PHONE_INDEX = 41
COMPANY_INDEX = 42
JOB_TITLE_INDEX = 43
DEPARTMENT_INDEX = 44
OFFICE_LOCATION_INDEX = 45
ORGANIZATIONAL_ID_NUMBER_INDEX = 46
PROFFESTION_INDEX = 47
ACCOUNT_INDEX = 48
BUSINESS_ADDRESS_INDEX = 49
BUSINESS_STREET_INDEX = 50
BUSINESS_STREET_2_INDEX = 51
BUSINESS_STREET_3_INDEX = 52
BUSINESS_ADDRESS_PO_BOX_INDEX = 53
BUSINESS_CITY_INDEX = 54
BUSINESS_STATE_INDEX = 55
BUSINESS_POSTAL_CODE_INDEX = 56
BUSINESS_COUNTRY_INDEX = 57
OTHER_PHONE_INDEX = 58
OTHER_FAX_INDEX = 59
OTHER_ADDRESS_INDEX = 60
OTHER_STREET_INDEX = 61
OTHER_STREET_2_INDEX = 62
OTHER_STREET_3_INDEX = 63
OTHER_ADDRESS_PO_BOX_INDEX = 64
OTHER_CITY_INDEX = 65
OTHER_STATE_INDEX = 66
OTHER_POSTAL_CODE_INDEX = 67
OTHER_COUNTRY_INDEX = 68
CALLBACK_INDEX = 69
CAR_PHONE_INDEX = 70
ISDN_INDEX = 71
RADIO_PHONE_INDEX = 72
TTY_TDD_INDEX = 73
TELEX_INDEX = 74
USER_1_INDEX = 75
USER_2_INDEX = 76
USER_3_INDEX = 77
USER_4_INDEX = 78
KEYWORDS_INDEX = 79
MILEAGE_INDEX = 80
HOBBY_INDEX = 81
BILLING_INFORMATION_INDEX = 82
DIRECTORY_SERVER_INDEX = 83
SENSITIVITY_INDEX = 84
PRIORITY_INDEX = 85
PRIVATE_INDEX = 86
CATEGORIES_INDEX = 87

def find_address_book():
    try:
        filename = input('What is the name of the CSV file? ')
    except FileExistsError or FileNotFoundError as file_err:
        print(f'Error: {file_err}')
        print('Restart the program and input a compatible file name')
    return filename

def open_address_book(filename):
    address_book = []
    #Will finish names later.
    names = []
    errors = []
    with open(filename) as address_book_file:
        next
        #Will finish count later.
        count = 0
        for line in address_book_file:
            # if '\n' in new_line:
            #     pass
            text = str()
            if len(line) < 50:
                text = "{}\n{}".format(text, line.strip())
            else:
                text = "{} {}".format(text, line.strip())
            new_line = line.split(',')
            address_book_file.seek(0)
            address_book_file.write(text[1:])
            count += 1
    return address_book, errors

def edit_address_book():
    pass

def close_address_book():
    pass

def main_menu():
    pass

def main():
    filename = find_address_book()
    address_book, errors = open_address_book(filename)
    for contact in address_book:
        # print(f'{contact[FIRST_NAME_INDEX]} {contact[LAST_NAME_INDEX]} {contact[PRIMARY_PHONE_INDEX]} {contact[MOBILE_PHONE_INDEX]}')
        # print(contact)
        pass
    print(errors)
main()