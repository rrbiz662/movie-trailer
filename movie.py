class Movie:
    """A Class representing a movie data object."""
    def __init__(self, title, poster, trailer):
        """Movie class' __init__ method.

        Args:
            title(str): The title of the movie.
            poster(str): The poster image's URL.
            trailer(str): The movie trailer's YouTube URL.
        """
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
