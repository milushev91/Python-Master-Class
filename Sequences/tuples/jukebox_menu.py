from nested_data import albums

SONG_LIST_INDEX = 3
loop_stop = False

while not loop_stop:
    print("=" * 40)
    print("Please choose your album (invalid choice exits):")

    #printing albums
    #unpacking the second value (tuple) using parenthesis
    for number, (title, artist, year, songs) in enumerate(albums):
        print(f"{number + 1}: {title}, {artist}, {year}")
    
    #chossing album
    choice = int(input("Album number: "))

    #Invalid choice exits the program
    if choice <= 0 or choice > len(albums):
        print("Exiting jukebox...")
        print("Goodbye")
        loop_stop = True 
        continue
    
    #geting album data
    choisen_album = albums[choice - 1]

    print("Please choose your song number: ")
    
    #geting songs list
    songs = choisen_album[SONG_LIST_INDEX]

    #printing songs
    for number, song in songs:
        print(f"{number}: {song}")
    
    #getting choisen song
    choicen_song_number = int(input("Song: "))

    if choicen_song_number < 1 or choicen_song_number > len(songs):
        continue

    choicen_song = songs[choicen_song_number - 1][1]

    print(f"Playing {choicen_song}")
    
