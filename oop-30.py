# oop 
# data structures

song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

# driver code 
artists = set()
for song, artist in song_library:
    artists.add(artist)

print(artists)
print('Opeth' in artists)
alpabetical = list(artists)
alpabetical.sort()
print(alpabetical)