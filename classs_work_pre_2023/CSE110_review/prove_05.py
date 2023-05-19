from random import choice


print('Welcome to the fastest game ever.')
print()
choice_road = str(input('Would you like to go down the road of rainbows, or the road of spikey thorns?'))
choice_road = choice_road.lower()

if choice_road == 'rainbows':
    print('Well, you\'re gonna win!')

elif choice_road == 'spikey thorns': 
    print('Sorry, you\'re outta luck')

    choice_road = 'finished'
    print('You\'re done with the game.')

else:
    print('Somehow, you messed it all up...')