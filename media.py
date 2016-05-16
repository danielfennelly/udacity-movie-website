
"""
media.py - Provides a method for reading movie data and a container tuple
"""

from collections import namedtuple
import csv


Movie = namedtuple('Movie', ['title', 'storyline', 'poster_image_url',
                             'trailer_youtube_url'])


def read_movie_data(filename):
    """Reads movie data out of the tsv file specified by filename"""

    movies = []
    with open(filename, 'r') as tsv_file:
        movie_reader = csv.DictReader(tsv_file, dialect=csv.excel_tab)
        for row in movie_reader:
            movie = Movie(
                row['movie_title'],
                row['movie_storyline'],
                row['poster_image'],
                row['trailer_youtube'])
            movies.append(movie)
    return movies
