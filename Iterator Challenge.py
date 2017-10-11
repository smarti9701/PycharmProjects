# string = input('Please enter you name:')
#
# for thing in iter(string):
#     if len(string) > :
#         print(thing)
#     else:
#         break

list = ['Sushi', 'Salmon', 'Cuttlefish', 'Tuna', 'Burger' ]

menuChoice = iter(list)

for food in range(0, len(list)):
    if food < len(list):
        print(next(menuChoice))
else:
    #food == len(list) or food > len(list):
     print("That's all we have!")

