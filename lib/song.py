class Song:

    count = 0
    genres = []
    artists = []  
    genre_count = {}
    artist_count = {}

    # song count 
    # song count per genre
    # song count per artist

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artists_count(artist)

        # add variable within each instance other than song count only
        # Song.count +=1
        # Song.add_artist_to_all(self)
        # Song.add_genres_to_all(self)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
        # line30 refer to cls. and then add to class attribute count and + inc increment

    @classmethod
    def add_to_genres(cls, genre):
        # if not isinstance (cls.genres):
        if genre not in cls.genres:
        #     return cls.add_to_genres in cls.genres
        # else:
        #     print("Genre already exists.")
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        # artists_dict = {"artist1":"count","artist2":"count2"}

        # if not isinstance(cls.artists):
        #     return cls.add_to_genres in cls.genres
        # else:
        # print("Artist already exists.")
  

#   I NEED THE ENTIRE BELOW SECTION BROKEN DOWN:
    @classmethod
    def add_to_genre_count(cls, genre): 
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

Song.artist()
Song.artist_count()
Song.genre()
Song.genre_count()
        



   
