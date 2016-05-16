import webbrowser
import csv

class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

Movies = []
with open('movie_data.tsv', 'r') as tsv_file:
    movie_reader = csv.DictReader(tsv_file, dialect=csv.excel_tab) 
    for row in movie_reader:
        movie = Movie(
                row['movie_title'],
                row['movie_storyline'],
                row['poster_image'],
                row['trailer_youtube']
                )
        Movies.append(movie)

        
