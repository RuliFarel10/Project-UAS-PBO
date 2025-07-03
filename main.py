#MY FAV MOVIES_RULIFARELRIFA'I TI23H

from models.manager import MovieListManager
from models.movie import Movie, WatchedMovie

def main():
    manager = MovieListManager()
    manager.load_from_file()

    while True:
        print("\n=== My Favorite Movies ===")
        print("1. Add New Movie")
        print("2. Remove Movie")
        print("3. Show All Movies")
        print("4. Save Data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Movie Title: ")
            genre = input("Genre: ")
            year = input("Year: ")
            rating = input("Rating (0-10): ")
            watched = input("Have you watched it? (y/n): ").lower()

            if watched == 'y':
                date_watched = input("Date Watched (YYYY-MM-DD): ")
                review = input("Your Review: ")
                movie = WatchedMovie(title, genre, year, rating, date_watched, review)
            else:
                movie = Movie(title, genre, year, rating)

            manager.add_movie(movie)
            print("Movie added!")

        elif choice == '2':
            title = input("Enter movie title to remove: ")
            manager.remove_movie(title)
            print("Movie removed if found.")

        elif choice == '3':
            print("\nYour Movie List:")
            manager.list_movies()

        elif choice == '4':
            manager.save_to_file()
            print("Data saved to file.")

        elif choice == '5':
            print("Exiting and saving data...")
            manager.save_to_file()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
