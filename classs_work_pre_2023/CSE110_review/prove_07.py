"""
Practice while loops
"""
# number = int(input('Please type a positive number: '))

# while number <= 0:
#     number = int(input('Sorry, that is a negative number. Please try again. '))

# print(f'The number is {number}')

# answer = input('May I have a piece of candy? ')

# while answer != 'yes':
#     answer = input('May I have a piece of candy? ')

# print('Thank you.')
"""
Practice for loops
"""
# colors = ["red", "blue", "green", "yellow"]
# for color in colors:
#     print(color)

# number_list = range(1,9)
# for number in number_list:
#     print(number)

# even_number_list = range(2,20,2)
# for even_number in even_number_list:
#     print(even_number)

"""
Assignment V
"""
# Start of Game
import random
print()
print('Welcome to the word guessing game!')

list_of_secret_words = ['table','mouse','money']

secret_word = random .choice(list_of_secret_words)
print('Your hint is:_ _ _ _ _')
user_guess =input('What is your guess? ')

guess_count = 1

# Game Logic
while user_guess != secret_word:
    for secret_letters in secret_word:
        for guess_letters in user_guess:
            if secret_letters == guess_letters:
                guess_letters = guess_letters.upper()
            elif secret_letters != guess_letters:
                guess_letters ='_'

    print('Sorry, that was incorrect.')
    user_guess = input('What is your guess? ')
    guess_count += 1
        

# End of Game
if user_guess == secret_word:
    print('Congratulations! You guessed it!')

    if guess_count == 1:
        print(f'It took you {guess_count} guess.')
    elif guess_count > 1:
        print(f'It took you {guess_count} guesses.')
