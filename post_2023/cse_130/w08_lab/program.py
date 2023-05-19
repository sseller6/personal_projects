# 1. Name:
#      Steven Sellers
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      It sorts a list alphabetically.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out how to use the indexes correctly.
# 5. How long did it take for you to complete the assignment?
#      It took me about two hours.

# Creating the list of words.
import json
print()
file_name = input('What is the name of the file? ').strip()
file = open(f'files/{file_name}')
words_text = file.read()
words_json = json.loads(words_text)
words_list = words_json['array']

def Sort_list(list):
    i_pivot = len(list) - 1
    while i_pivot != 0:
        i_largest = 0
        i_largest = list.index(list[i_pivot])
        i_check = list.index(list[i_pivot -1])
        if list[i_largest] > list[i_check]:
            i_pivot -= 1
        elif list[i_largest] < list[i_check]:
            # Assign new copies of i_largest and i_check.
            new_i_check_copy = list[i_largest]
            new_i_largest_copy = list[i_check]
            # Assign new values for i_largest and i_check.
            list[i_largest] = new_i_largest_copy
            list[i_check] = new_i_check_copy
            # Starting over
            i_pivot = len(list) -1

    return list

new_list = Sort_list(words_list)

print(new_list)