imelda = "More Mayhem", "Imelda May", 2011, (( 1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
print(imelda)
print(title)
print(artist)
print(year)
print(tracks)
print("++"*30)
print(title, year,)
for song in tracks:
    track, songtitle = song
    print(song)
    # print("---" * 20)
    # print("\t", song)
    # print("---" * 20)
    # print("\n", song)
    # print("---" * 20)
    print("Track number {} assigned to the song named {}." .format(track, title))



