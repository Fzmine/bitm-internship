album= 'aashiqui 2', 2013, 'arijit shing',((1,"tum hi ho"),(2,"chahum mai ya na "),(3,"meri aashiqui"))

title,year,singer,songs=album
print("title:", title)
print("year:", year)
print("singer:", singer)

for song in songs:
    num = song[0]
    song_name=song[1]
    print("\t song number: ",num,"song name: ",song_name)