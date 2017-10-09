import random
highest = 15
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}." .format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher.")
    else:
        print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Great Job! You're good!")
    else:
        print("Sorry, but you suck!")

else:
    print("Dude, you must be psychic!")

