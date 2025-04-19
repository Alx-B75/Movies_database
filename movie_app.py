import os
import random
import statistics

import tmdb_client
from tmdb_client import get_imdb_id


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

        user_input_title = input("Enter new movie name: ").strip()

        search_results = tmdb_client.search_movies_by_title(user_input_title)
        if not search_results:
            print(f"No matches found for {user_input_title}, please try another.")
            return
        if not search_results:
            print(f"No matches found for {user_input_title}, please try another.")
            return
        options = []
        for index, movie in enumerate(search_results, start=1):
            movie_title = movie['title']
            year = movie.get('release_date')
            if year:
                year = year[:4]
            rating = movie.get('vote_average')
            if not rating:
                rating = 5
            poster = movie.get('poster_path')
            if not poster:
                poster = "https://bit.ly/3Kf5e2L"
            options.append({
                "index": index,
                "title": movie_title,
                "year": year,
                "rating": rating,
                "poster": poster
            })
        for option in options:
            print(f"{option['index']}. {option['title']} ({option['year']}) - Rating: {option['rating']}")

        try:
            user_selection = int(input("Please enter the number of the title you would like to add: "))
        except ValueError:
            print("That's not going to work, we need a number listed")
            return

        try:
            selected_movie = options[user_selection - 1]

        except IndexError:
            print("That's not going to work, we need a number listed")
            return

        title_raw = selected_movie['title']
        year = selected_movie['year']
        title = f"{title_raw} ({year})"
        rating = selected_movie['rating']
        poster = selected_movie['poster']
        movie_id = search_results[user_selection - 1]['id']
        imdb_id = get_imdb_id(movie_id)
        imdb_url = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else None

        self._storage.add_movie(title, year, rating, poster, imdb_url)

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
        """Displays statistics: total movies, average rating, median, highest and lowest rated."""
        movies = self._storage.list_movies()
        ratings = [float(details["rating"]) for details in movies.values()]

        if not ratings:
            print("No movies in database to calculate stats.")
            return

        avg = round(statistics.mean(ratings), 2)
        median = round(statistics.median(ratings), 2)
        highest = max(movies.items(), key=lambda x: float(x[1]["rating"]))
        lowest = min(movies.items(), key=lambda x: float(x[1]["rating"]))

        print("📊 Stats 📊")
        print(f"Total movies: {len(movies)}")
        print(f"Average rating: {avg}")
        print(f"Median rating: {median}")
        print(f"Highest rated: {highest[0]} ({highest[1]['rating']})")
        print(f"Lowest rated: {lowest[0]} ({lowest[1]['rating']})")

    def _command_random_movie(self):
        """Selects and displays a random movie."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
            return

        title, details = random.choice(list(movies.items()))
        print(f"🎲 Random pick: {title} ({details['year']}) - Rating: {details['rating']}")

    def _command_search_movie(self):
        """Searches for movies by title (case-insensitive, partial match)."""
        query = input("Enter search term: ").strip().lower()
        movies = self._storage.list_movies()
        results = {title: details for title, details in movies.items() if query in title.lower()}

        if results:
            for title, details in results.items():
                print(f"{title} ({details['year']}) - Rating: {details['rating']}")
        else:
            print("No matches found.")

    def _command_movies_sorted_by_rating(self):
        """Displays all movies sorted by rating in descending order."""
        movies = self._storage.list_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: float(x[1]["rating"]), reverse=True)

        if sorted_movies:
            for title, details in sorted_movies:
                print(f"{title} ({details['year']}) - Rating: {details['rating']}")
        else:
            print("No movies to display.")

    def _generate_website(self):
        """Generates an HTML website from the movie database with posters and IMDb links."""
        movies = self._storage.list_movies()

        if not movies:
            print("No movies to display. Please add some first.")
            return

        with open("index_template.html", "r", encoding="utf-8") as template_file:
            template_content = template_file.read()

        html_title = "Movie Lovers Library"
        template_content = template_content.replace("__TEMPLATE_TITLE__", html_title)

        movie_blocks = []
        for title, details in movies.items():
            poster = details.get('poster', 'https://bit.ly/3Kf5e2L')
            if poster.startswith("/"):
                poster = f"https://image.tmdb.org/t/p/w500{poster}"

            imdb_url = details.get("imdb_url")
            imdb_link_html = (
                f'<div class="movie-imdb"><a class="imdb-button" href="{imdb_url}" target="_blank">View on IMDb</a></div>'
                if imdb_url else ""
            )

            movie_html = f"""
                <div class="movie">
                    <img class="movie-poster" src="{poster}" alt="Poster for {title}">
                    <div class="movie-title">{title} ({details['year']})</div>
                    <div class="movie-rating">⭐ {details['rating']}</div>
                    <div class="movie-footer">
                        <a class="imdb-button" href="{imdb_url}" target="_blank">View on IMDb</a>
                    </div>
                </div>
            """
            movie_blocks.append(movie_html)

        movie_grid_html = "\n".join(movie_blocks)
        final_html = template_content.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)

        output_path = os.path.join(os.getcwd(), "index.html")
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(final_html)

        print("✅ Website was generated successfully: index.html")

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
            "9": self._generate_website,
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
            print("9. Generate website")
            print("0. Exit")

            choice = input("Select an option (0-9): ").strip()

            if choice == "0":
                print("👋 Goodbye!")
                break
            elif choice in commands:
                commands[choice]()
            else:
                print("❌ Invalid option. Please choose a number from 0 to 8.")
