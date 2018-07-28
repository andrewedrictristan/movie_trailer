import webbrowser


class Movie():
    """Class movie is consist of constructor and method"""
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        """Inits is the constructor where its parameter will get the value
        from module entertainment_center"""
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ show_trailer_function can be called to open
        the function that open trailer in browser """
        webbrowser.open(self.trailer_youtube_url)
