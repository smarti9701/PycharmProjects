largest_so_far = -1
print("Before", largest_so_far)
for the_num in [2, 14, 25, 38, 125, 1000]:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(largest_so_far, the_num)
print("After", largest_so_far)


next = -1
print("Before", next)
for num in [2, 14, 25, 38, 125, 1000]:
    next = next + num
    print(next, num)
print("After", next)