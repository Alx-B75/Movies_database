import csv

from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """Returns a dictionary of all movies from the CSV file."""
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            movie_list = {}
            for row in reader:
                title = row["title"]
                movie_list[title] = {
                    "year": int(row["year"]),
                    "rating": float(row["rating"]),
                    "poster": row["poster"]
                }
            return movie_list

    def add_movie(self, title, year, rating, poster):
        """Adds a new movie to the CSV file."""
        movie_list = self.list_movies()

        if title in movie_list:
            raise ValueError(f"Movie '{title}' already exists.")

        with open(self.file_path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "rating", "year", "poster"])
            writer.writerow({"title": title,
                             "rating": rating,
                             "year": year,
                             "poster": poster
                             })

    def delete_movie(self, title):
        """Deletes a movie from the CSV file by title."""
        movie_list = self.list_movies()

        if title not in movie_list:
            raise ValueError(f"Movie '{title}' not found.")

        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "rating", "year", "poster", "imdb_url"])
            writer.writeheader()

            for movie_title, details in movie_list.items():
                if movie_title != title:
                    writer.writerow({
                        "title": movie_title,
                        "rating": details["rating"],
                        "year": details["year"],
                        "poster": details["poster"],
                        "imdb_url": details.get("imdb_url", "")
                    })

    def update_movie(self, title, rating):
        """Updates the rating of an existing movie in the CSV file."""
        movie_list = self.list_movies()

        if title not in movie_list:
            raise ValueError(f"Movie '{title}' doesn't exist.")

        movie_list[title]["rating"] = rating

        with open(self.file_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "rating", "year", "poster"])
            writer.writeheader()

            for movie_title, details in movie_list.items():
                writer.writerow({
                    "title": movie_title,
                    "rating": details["rating"],
                    "year": details["year"],
                    "poster": details["poster"],
                    "imdb_url": details.get("imdb_url", "")
                })
