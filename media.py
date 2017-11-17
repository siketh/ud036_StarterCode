import webbrowser


class Movie(object):
    """ This class provides a way to store movie related information """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        """ Constructs a new instance of Movie """

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ Opens a new browser window and plays the youtube trailer for this
        movie instance """

        webbrowser.open(self.trailer_youtube_url)
