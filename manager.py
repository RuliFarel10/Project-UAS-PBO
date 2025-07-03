#MY FAV MOVIES_RULIFARELRIFA'I TI23H

import json
from .movie import Movie, WatchedMovie

class MovieListManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, title):
        self.movies = [m for m in self.movies if m.title.lower() != title.lower()]

    def list_movies(self):
        if not self.movies:
            print("No movies in the list.")
        else:
            for idx, movie in enumerate(self.movies, 1):
                print(f"{idx}. {movie.display_info()}\n")

    def save_to_file(self, filename="data/movies.json"):
        data = []
        for movie in self.movies:
            entry = movie.__dict__.copy()
            entry['type'] = movie.__class__.__name__
            data.append(entry)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename="data/movies.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.movies = []
                for item in data:
                    if item['type'] == 'WatchedMovie':
                        movie = WatchedMovie(**{k: item[k] for k in item if k != 'type'})
                    else:
                        movie = Movie(**{k: item[k] for k in item if k != 'type'})
                    self.movies.append(movie)
        except FileNotFoundError:
            self.movies = []
