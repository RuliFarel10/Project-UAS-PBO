#MY FAV MOVIES_RULIFARELRIFA'I TI23H

class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def display_info(self):
        return f"{self.title} ({self.year}) - Genre: {self.genre}, Rating: {self.rating}"

class WatchedMovie(Movie):
    def __init__(self, title, genre, year, rating, date_watched, review):
        super().__init__(title, genre, year, rating)
        self.date_watched = date_watched
        self.review = review

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\n  Watched on: {self.date_watched}\n  Review: {self.review}"
