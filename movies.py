import random
# import operator
from statistics import median
import movie_storage


def list_movies():
    """Prints all movies in the database along with their year and rating."""
    movies = movie_storage.get_movies()
    num_movies = len(movies)
    print(f"\nThere are {num_movies} movies in the database:")
    for title, details in movies.items():
        print(f"{title} ({details['year']}) - Rating: {details['rating']}")


def add_movie():
    """ Adds a movie to the movies database """

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    title = input("Enter new movie name: ")
    if title in movies:
        print(f"Movie {title} already exist!")
        return
    year = input("Enter movie year: ")
    rating = input("Enter movie rating: ")

    movie_storage.add_movie(title, year, rating)

    print(f"Movie {title} successfully added")


def delete_movie():
    """Deletes a movie from the database if it exists."""
    movies = movie_storage.get_movies()

    title = input("Enter the title of the movie to delete: ").strip()
    if title not in movies:
        print(f"{title} is not listed in the database")
    else:
        movie_storage.delete_movie(title)


def update_movie():
    """Updates the rating of an existing movie."""
    movies = movie_storage.get_movies()

    title = input("Enter the movie title to update: ").strip()
    if title in movies:
        try:
            rating = float(input(f"Enter new rating for {title}: "))
            movie_storage.update_movie(title,rating)
            print(f"Rating updated for {title}: {rating}")
        except ValueError:
            print("Invalid rating. Please enter a number.")
    else:
        print(f"{title} is not in the database.")


def get_stats():
    """Displays statistics: total movies, average rating, median, highest and lowest rated."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in the database.")
        return
    ratings = [float(details["rating"]) for details in movies.values()]
    avg_rating = sum(ratings) / len(ratings)
    med_rating = median(ratings)

    sorted_movies = sorted(movies.items(), key=lambda x: float(x[1]["rating"]), reverse=True)
    top_movie, top_details = sorted_movies[0]
    bottom_movie, bottom_details = sorted_movies[-1]

    print("\n** Movie Database Stats **")
    print(f"Total movies: {len(movies)}")
    print(f"Average rating: {avg_rating:.2f}")
    print(f"Median rating: {med_rating:.2f}")
    print(f"Highest rated movie: {top_movie} ({top_details['rating']})")
    print(f"Lowest rated movie: {bottom_movie} ({bottom_details['rating']})")


def get_random_movie():
    """Selects a random movie from the database."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in the database.")
        return
    title, details = random.choice(list(movies.items()))
    print(f"Random selection: {title} ({details['year']}) - Rating: {details['rating']}")


def search_movie():
    """Searches for movies by title (case-insensitive, partial match)."""
    search_term = input("Enter a movie title or part of a title to search: ").strip().lower()
    movies = movie_storage.get_movies()
    results = [(title, details) for title, details in movies.items() if search_term in title.lower()]
    if results:
        for title, details in results:
            print(f"{title} ({details['year']}) - Rating: {details['rating']}")
    else:
        print("No movies found matching your search.")


def movies_sorted_by_rating():
    """Displays all movies sorted by rating in descending order."""
    movies = movie_storage.get_movies()
    sorted_movies = sorted(movies.items(), key=lambda x: float(x[1]["rating"]), reverse=True)
    for title, details in sorted_movies:
        print(f"{title} ({details['year']}) - Rating: {details['rating']}")


def cli_for_movies():
    """Displays the menu and gets user input."""
    print("\n** My Movies Database **")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("0. Exit")
    return input("\nEnter your choice: ").strip()


COMMANDS = {
    "1": list_movies,
    "2": add_movie,
    "3": delete_movie,
    "4": update_movie,
    "5": get_stats,
    "6": get_random_movie,
    "7": search_movie,
    "8": movies_sorted_by_rating
}


def main():
    """Main function that runs the CLI and calls the respective functions."""
    while True:
        user_command = cli_for_movies()

        if user_command == "0":
            print("Exiting movie database...")
            break

        elif user_command in COMMANDS:
            func_to_exe = COMMANDS[user_command]  
            func_to_exe()

        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
