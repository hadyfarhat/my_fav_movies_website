import webbrowser


class Movie():

    def __init__(self, title, story_line, poster_image, youtube_url):
        """Movie class constructor"""
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url

    def show_trailer(self):
        """Displays the movie's trailer in the browser"""
        webbrowser.open(self.trailer_youtube_url)
