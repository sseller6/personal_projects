import json

# step 1 Completed - Read the data from the file into a single string.
with open ('Lab02.json', 'r') as file_handle:
    json_usernames = file_handle.read()

# step 2 Completed - Convert the string into a JSON object.

json_dictionary = json.loads(json_usernames)

# step 3 Completed - Convert the username and password components of the JSON object into two lists.

json_username_list = json_dictionary['username']

json_password_list = json_dictionary['password']

#print(json_username_list)
print()
print()
#print(json_password_list)
authorized = False
print()

while authorized == False:
    # Promt User for Username and Password

    username_input = input('Username: ')
    password_input = input('Password: ')

    if username_input in json_username_list and password_input in json_password_list:

        # Get username and password input indexes
        username_input_index = json_username_list.index(username_input)
        password_input_index = json_password_list.index(password_input)

        # Check if username and password index match

        if username_input_index == password_input_index:
            print('You are authenticated!')
            authorized = True

        elif username_input_index != password_input_index:
            print('You are not authorized to use the system.')
            authorized = False

        else:
            print('Username and or Password invalid.')

    else:
        print('Invalid Username and or Password.')