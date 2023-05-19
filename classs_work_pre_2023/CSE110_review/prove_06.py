"""
This was practice 
"""
# gpa = float(input('What was your Grade Point Average? '))
# lowest_grade = float(input('What was your lowest grade? '))

# if gpa >= .85 and lowest_grade >= .70:
#     honour_roll = True
# else:
#     honour_roll = False

# if honour_roll:
#     print('You made honour roll')

# elif honour_roll == False:
#     print('Better luck next year')

# else: 
#     print('You messed up somehow.')
"""
This is where the prove assignment starts. Loan Assignment.
"""

#Gathering data 
print('Please answer the following questions with a rating from 1-10. ')
print()
loan_size = input('How large is the loan? ')
credit_history = input('How good is your credit history? ')
income = input('How high is your income? ')
down_payment_size = input('How large is your down payment? ')

loan_size = int(loan_size)
credit_history = int(credit_history)
income = int(income)
down_payment_size = int(down_payment_size)

if loan_size >= 5:
    if credit_history >= 7 and income >=7:
        status_approve = True
    elif credit_history >=7 or income >=7:
        if down_payment_size >=5:
            status_approve = True
        else:
            status_approve = False
    else:
        status_approve = False

if loan_size < 5:
    if credit_history < 4:
        status_approve = False
    elif income >= 7 or down_payment_size >=7:
        status_approve = True
    elif income >= 4 and down_payment_size >= 4:
        status_approve = True
    else:
        status_approve = False

if status_approve:
    print()
    print('Looks like you\'re approved!')
else:
    print()
    print('Sorry, you\'re not approved :(')
