import webbrowser


class Movie():

    # Get all the values from entertainer.py
    def __init__(self, movie_name, movie_story, movie_image, movie_trailer):
        self.title = movie_name                   # Assigns movie_name to the title
        self.storyline = movie_story              # Assigns movie_story to the storyline
        self.poster_image_url = movie_image       # Assigns movie_image to the variable
        self.trailer_youtube_url = movie_trailer  # Assigns movie_trailer to the trailer variable
