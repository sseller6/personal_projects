# 1. Name:
#      Steven Sellers
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program takes a number from the user to be converted into a francois number.
# 4. What was the hardest part? Be as specific as possible.
#      The most silly part of the assignment was when I realized I was supposed to put += not just + when I tried incrementing the index.
# 5. How long did it take for you to complete the assignment?
#      I spent just under an hour on this assignment.

max_number = int(input('What is the number to be converted? '))

def Get_list(num):
    # Define Variables to use.
    max_number = num
    number_list = []
    # Starting the list.
    if max_number == 2:
        number_list.append(2)
        number_list.append(1)
        return number_list
    elif max_number == 1:
        number_list.append(1)
        return number_list
    elif max_number == 0:
        assert max_number != 0, 'The size of the list you selected was 0. Therefore, no list will be displayed. \n'
        return
    elif max_number < 0:
        assert max_number != -1, 'The size of the list you selected was less than 0. Therefore, no list will be displayed. \n'
        return
    # Populate the rest of the list up to the max number.
    elif max_number > 2:
        number_list.append(2)
        number_list.append(1)
        first_number_index = 0
        second_number_index = 1

        while len(number_list) != max_number:
            first_number_to_add = number_list[first_number_index]
            second_number_to_add = number_list[second_number_index]
            number_list.append(first_number_to_add + second_number_to_add)
            first_number_index += 1
            second_number_index += 1
        return number_list
    
number_list = Get_list(max_number)

last_number_index = (len(number_list)-1)

francois_number = number_list[last_number_index]
# Uncomment line 36 if you want to see the list.
# print(number_list)
print(f'The number you chose to convert is {max_number}. \n The converted number is {francois_number}. ')