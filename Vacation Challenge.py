name = input("Hi! Please state your name: ")
print("Hi {}" .format(name))
age = int(input("{}, Could you tell me your age? " .format(name)))

if (age< 18)or(age>30):
    print("I'm sorry {}, but you aren't able to join our vacation. ".format(name))
else:
    print("{}, get ready to PARTY!".format(name))

