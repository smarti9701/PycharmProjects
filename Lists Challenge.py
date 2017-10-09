# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "spam", "bacon", "sausage"])
menu.append(["egg", "spam", "bacon", "spam", "spam"])
menu.append(["egg", "spam",])
menu.append(["spam", "spam", "spam"])
menu.append(["spam", "bacon", "spam"])
menu.append(["egg", "spam", "bacon", "spam", "spam"])
menu.append(["egg", "spam", "saudage", "spam"])
menu.append(["egg", "grits", "bacon", "sausage", "ham"])


for meal in menu:
    if not "spam" in meal:
        print("If you don't like spam, then you will like our {} meal." .format([meal]))
        for item in meal:
            print(item)