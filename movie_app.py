class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """Prints all movies in the database along with their year and rating."""
        movies = self._storage.list_movies()
        num_movies = len(movies)
        print(f"\nThere are {num_movies} movies in the database:")
        for title, details in movies.items():
            print(f"{title} ({details['year']}) - Rating: {details['rating']}")

    def _command_add_movie(self):
        """ Adds a movie to the movies database """

        movies = self._storage.list_movies()

        title = input("Enter new movie name: ").strip()
        if title in movies:
            print(f"Movie {title} already exist!")
            return
        try:
            year = int(input("Enter movie year: "))
            rating = float(input("Enter movie rating: "))
        except ValueError:
            print("That's not going to work! We are going to need a whole number for year and the rating must be "
                  "entered like this for example '7.0' or '8.5'")
            return
        poster = input("Type or paste the movie poster url: ").strip()
        if not poster:
            poster = "https://bit.ly/3Kf5e2L"

        self._storage.add_movie(title, year, rating, poster)
        print(f"Movie {title} successfully added")

    def _command_update_movie(self):
        """Updates the rating of an existing movie."""
        movies = self._storage.list_movies()
        title = input("Enter the movie title to update: ").strip()
        if title in movies:
            try:
                rating = float(input(f"Enter new rating for {title}: "))
                self._storage.update_movie(title, rating)
                print(f"Rating updated for {title}: {rating}")
            except ValueError:
                print("Invalid rating. Please enter a number.")
        else:
            print(f"{title} is not in the database.")

    def _command_delete_movie(self):
        """Deletes a movie from the database if it exists."""
        movies = self._storage.list_movies()

        title = input("Enter the title of the movie to delete: ").strip()
        if title not in movies:
            print(f"{title} is not listed in the database")
        else:
            self._storage.delete_movie(title)
            print(f"{title} has been removed from the database.")

    def _command_movie_stats(self):
        print("📊 Stats feature coming soon!")

    def _command_random_movie(self):
        print("🎲 Random movie feature coming soon!")

    def _command_search_movie(self):
        print("🔍 Search feature coming soon!")

    def _command_movies_sorted_by_rating(self):
        print("📈 Sort by rating feature coming soon!")

    def run(self):
        """dispatcher for CLI"""
        commands = {
            "1": self._command_list_movies,
            "2": self._command_add_movie,
            "3": self._command_delete_movie,
            "4": self._command_update_movie,
            "5": self._command_movie_stats,
            "6": self._command_random_movie,
            "7": self._command_search_movie,
            "8": self._command_movies_sorted_by_rating,
        }

        while True:
            print("\n🎬 Movie Database Menu")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Stats")
            print("6. Random movie")
            print("7. Search movie")
            print("8. Movies sorted by rating")
            print("0. Exit")

            choice = input("Select an option (0-8): ").strip()

            if choice == "0":
                print("👋 Goodbye!")
                break
            elif choice in commands:
                commands[choice]()
            else:
                print("❌ Invalid option. Please choose a number from 0 to 8.")



