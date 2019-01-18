import lyricsgenius
genius = lyricsgenius.Genius("j5c5R-jadsQRoMOBnx8OiJJtju5um3qa3so4nE7hqRadA1FjI91J3j_wSiktYduk")
artist = genius.search_artist("Sabotage", max_songs=15)
print(artist.songs)
print(artist.songs[0])
artist.save_lyrics(format='json')
