import random
import operator
from statistics import median


def list_movies(movies):
    """Prints movies along with their rating and how many total in database"""
    num_movies = len(movies)
    print(f"There are {num_movies} in the database.")
    for title, rating in movies.items():
        print(f"{title} - ({rating})")


def add_movie(movies):
    """asks user to add name and rating with no validation, assumes number 0-10"""
    title = input("Please enter your new movie title: ")
    rating = float(input("Please enter your rating: "))
    movies[title] = rating
    # could add validation but specifically not requested


def delete_movie(movies):
    """asks name, checks valid name, deletes if applicable, error if not"""
    remove_movie = input("Please enter the title of the movie you wish to delete: ")
    if remove_movie in movies:
        del movies[remove_movie]
    else:
        print(f"{remove_movie} not in Movie Database. Please choose another option.")


def update_movie(movies):
    """asks name, if existing asks to update rating, if not error msg"""
    movie_to_update = input("Please enter the title of the movie you would like to update:  ")
    if movie_to_update in movies:
        new_rating = input(f"Please enter new rating for {movie_to_update}: ")
        float(new_rating)
        movies[movie_to_update] = new_rating
    else:
        print(f"{movie_to_update} is not in the Movie Database. Please choose another option.")


def get_stats(movies):
    """prints stats about database - Avg rat, med rat, best, worst - This was the most difficult, tried 3 different ways!"""
    total_rat = sum(movies.values())
    count_of_movies = len(movies)
    avge_rat = total_rat / count_of_movies
    med_rat = median(list(movies.values()))

    sorted_movies = sorted(movies.items(), key=operator.itemgetter(1),
                           reverse=True)  # using the operator module to avoid internal function or lambda
    top_movie, top_rat = sorted_movies[0]
    bottom_movie, bottom_rat = sorted_movies[-1]

    print("\n** ** ** **  Movies Database Stats  ** ** ** **\n")
    print(f"Total movies in database: {count_of_movies}")
    print(f"Average rating is : {avge_rat:.2f}")
    print(f"Median rating is : {med_rat:.2f}")
    print(f"The highest rated movie is : {top_movie} ({top_rat})")
    print(f"The lowest rated movie is : {bottom_movie} ({bottom_rat})")


def get_random_movie(movies):
    """This selects a movie at random using the random module choice method"""
    random_movie = random.choice(list(movies.items()))
    print(f"Your random selection is: {random_movie}")


def search_movie(movies):
    """asks user to enter part of name, search and print all that apply not case-sensitive"""
    search_term = input("Please enter the movie (or part of the movie) you are looking for: ")
    for title, rating in movies.items():
        if search_term.lower() in title.lower():
            print(title, rating)
    # would also benefit from some error checks maybe


def movies_sorted_by_rating(movies):
    """returns all movies in descending order"""
    sorted_movies = sorted(movies.items(), key=operator.itemgetter(1),
                           reverse=True)  # using the operator module to avoid internal function or lambda
    for key, value in sorted_movies:
        print(f"{key}, {value}")


def main():
    """This is the main function to deal with the menu and contain the dictionary"""
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }
    # menu to handle the choices
    while True:
        print("")
        print("** ** ** ** ** My Movies Database ** ** ** ** **")
        print("")
        print("Menu:")
        print("1.  List movies")
        print("2.  Add movie")
        print("3.  Delete movie")
        print("4.  Update movie")
        print("5.  Stats")
        print("6.  Random movie")
        print("7.  Search movie")
        print("8.  Movies sorted by rating")
        print()

        try:  # added the trial because this is the main part of the program and needs to be robust
            user_choice = int(input("Enter choice(1 - 8): "))
            if user_choice == 1:
                list_movies(movies)
            elif user_choice == 2:
                add_movie(movies)
            elif user_choice == 3:
                delete_movie(movies)
            elif user_choice == 4:
                update_movie(movies)
            elif user_choice == 5:
                get_stats(movies)
            elif user_choice == 6:
                get_random_movie(movies)
            elif user_choice == 7:
                search_movie(movies)
            elif user_choice == 8:
                movies_sorted_by_rating(movies)
            elif user_choice == 0:
                print("Bye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")


main()

if __name__ == "__main__":
    main()
