import json


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    try:
        with open("data_static_original.json", "r") as fileobj:
            return json.load(fileobj)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if file doesn't exist


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("data_static_original.json", "w") as fileobj:
        json.dump(movies, "data_static_original.json", indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    try:
        with open("data_static_original.json", "r") as fileobj:
            movies = json.load(fileobj)
    except FileNotFoundError:
        movies = []

    new_movie = {
        "year": year,
        "rating": rating
    }

    movies[title] = new_movie

    with open("data_static_original.json", "w") as fileobj:
        json.dump(movies, fileobj, indent=4)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data_static_original.json", "r") as fileobj:
        movies = json.load(fileobj)

        if title in movies:
            del movies[title]

    with open("data_static_original.json", "w") as fileobj:
        json.dump(movies, fileobj, indent=4)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open("data_static_original.json", "r") as fileobj:
        movies = json.load(fileobj)

        if title in movies:
            movies[title]["rating"] = rating

    with open("data_static_original.json", "w") as fileobj:
        json.dump(movies, fileobj, indent=4)
