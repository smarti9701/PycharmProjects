IP = (input("Please provide your IP address here: => "))
segment = 1
segmentlength = 0
char = ""

for char in IP:
    if char == '.':
        print("Your IP adress consists of Segment number {} containing {} Characters. ".format(segment, segmentlength,))
        segment += 1
        segmentlength = 0  #this resets the segment length back to 0 for the next segment
    else:
        # this says that if you don't run into a '.' char, then it will increment the count of segmentlength
        segmentlength += 1

#this was the original way to count the last segment without a '.'
#if char != '.':
#print("Your IP adress consists of Segment number {} containing {} Characters. ".format(segment, segmentlength, ))

#This was my first attempt to account for the lack of input.
#if char != '.' and char != '0123456789':

#yes! I figured out how to just make the lack of input come out by itself.
if char != '.' and char != '0123456789' and char == "":
    print("Hey dummy, you forgot to enter your IP address!")
elif char != '.':
    print("Your IP adress consists of Segment number {} containing {} Characters. ".format(segment, segmentlength, ))