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

dusty_artists = {
    'Sarah Brightman',
    'Guns N" Roses',
    'Oppeth',
    'Vixy and Tony',
}

steve_artists = {'Yes', 'Guns N', 'Genesis'}

artists = {'Gun N Roses', 'Vixy and Tony', 'Sarah Brightman', 'Opeth'}
bands = {'Opeth', 'Guns N Roses'}


# driver code 
# artists = set()
# for song, artist in song_library:
#     artists.add(artist)

# print(artists)
# print('Opeth' in artists)
# alpabetical = list(artists)
# alpabetical.sort()
# print(alpabetical)

# print(f'All: {dusty_artists | steve_artists}')
# print(f'Both: {dusty_artists.intersection(steve_artists)}')
# print(f'Either but not both: {dusty_artists ^ steve_artists}')

print(artists.issuperset(bands))
print(artists.issubset(bands))
print(artists - bands) 
print(bands.issuperset(artists))
print(bands.issubset(artists))
print(bands.difference(artists))