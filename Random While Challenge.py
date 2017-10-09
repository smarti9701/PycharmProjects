# import random
# highest = 15
# answer = random.randint(1,highest)
#
# print("Please guess a number between 1 and {}." .format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Great Job! You're good!")
#     else:
#         print("Sorry, but you suck!")
#
# else:
#     print("Dude, you must be psychic!")

import random
highest = 15
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}, or press 0 to exit." .format(highest))
guess = 0 #initialized because while loops need to be initialized. FOR loops don't.
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Thank you for playing. Goodbye!")
        break
    if guess < answer:
        print("Please guess higher.")
    elif guess > answer:
         print("Please guess lower.")

    else:
        print("Dude, you must be psychic!")