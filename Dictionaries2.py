locations = {0: "You are sitting at home with your dick in your hands...",
             1: "You are in the mountains of Shenandoah enjoying nature.",
             2: "Uh-oh, you went too far West and now are in Hick country! Get your purty lips out of here!",
             3: "Ah shit....You've entered crying-vagina territory. Freakin' Liberals EVERYWHERE! Get out!",
             4: "You've headed South to Miami for some good Latin cusine. Yep, going to get FAT!",
             5: "You've finally headed North to watch the Auroras! This is great!"                }

exits = [{'Q': 0},
         {'W': 2, 'E':3, 'N':5, 'S':4, 'Q':0},
         {'N':5,'Q':0},
         {'W': 1,'Q':0,},
         {'W': 2, 'N':1, 'Q':0,},
         {'W': 2, 'S':1, 'Q':0}]

loc = 1

while True:
    availableExits = ' '
    for direction in exits[loc].keys(): #the keys in exits are the cardinal directions
        availableExits += direction + ','
    #an alternative to lines 19 & 20
    #availableExits = ",".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input('Available exits are: '+ availableExits).upper()  #.upper here takes any of the input and converts it to uppercase
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Sorry, but you can't go in that direction!")