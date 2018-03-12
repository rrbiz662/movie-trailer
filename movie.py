# Class represents a movie data object. 
class Movie:
    # Constructor.
    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
