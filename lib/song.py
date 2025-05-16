class Song:

    count= 0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}

    def __init__(self,name ,artist, genre):
        Song.add_song_to_count()
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls,increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls,genre):
        if not genre in Song.genres:
            Song.genres.append(genre)
            

    @classmethod
    def add_to_artists(cls,artist):
        if not artist in Song.artists:
            Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        if Song.genre_count.get(genre):
            Song.genre_count[genre]+=1
        else:
            cls.genre_count[genre]=1
    
    @classmethod
    def add_to_artist_count(cls,artist):
        if Song.artist_count.get(artist):
            Song.artist_count[artist]+=1
        else:
            cls.artist_count[artist]=1

        





    
                                        
        
