# 1. Name:
#      Steven Sellers
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program has a function which computes prime numbers.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part for me was figuring out how to "take out" the non prime numbers.
# 5. How long did it take for you to complete the assignment?
#      In total, the assignment took me about three hours to complete.

import math

n = int(input('What is the top number? '))

# This function computes all prime numbers at and below the number.
def Compute_Primes(top_number):
    prime_list = []
    inclusive_list =[]
    # Creates a list with all number sbelow number and above 0.
    for x in range(top_number +1):
        inclusive_list.append(x)

    # Remove 0.
    inclusive_list[0] = False

    # Remove 1.
    inclusive_list[1] = False

    # Remove multiples of 2, 3, 4, and so forth. Stop at the square root.
    for x in range(2,round(math.sqrt(top_number)+ 1)):
        if inclusive_list[x]:
            for y in range (x + x, top_number + 1, x):
                inclusive_list[y] = False

    # Remove items set to False.
    for z in range(len(inclusive_list)-1,-1,-1):
        if inclusive_list[z] == False:
            inclusive_list.pop(z)

    # Assign the left over numbers to the prime list.
    prime_list = inclusive_list

    return(prime_list)


print(Compute_Primes(n))