def make_album(artist, album_title, number_of_songs = None):
    album = {"artist": artist, "title": album_title}

    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    
    return album

first_album = make_album("Muse", "Absolution")
print(first_album)
second_album = make_album("The weeknd", "Starboy")
print(second_album)
third_album = make_album(album_title="Hard To Imagine The Neighbourhood Ever Changing", artist="The Neighborhood", number_of_songs=21)
print(third_album)

while True:
    print("Let's add a new album to our collection")
    print("If you want to stop recording please press x")
    
    artist = input("What's the name of the artist: ").title()
    if artist == "X":
        break
    album = input("What's the name of the album: ").title()
    if album == "X":
        break
    
    new_album = make_album(artist, album)
    print(new_album)

    
