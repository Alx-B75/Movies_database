from istorage import IStorage
import json

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """Returns all movies in storage."""
        with open(self.file_path, "r") as file_obj:
            data = json.load(file_obj)
            return data

    def add_movie(self, title, year, rating, poster):
        """Adds a movie to storage"""
        with open(self.file_path, "r") as file_obj:
            data = json.load(file_obj)
            if title in data:
                raise ValueError(f"The entry '{title}' already exists.")
            else:
                data[title] = {
                "year": year,
                "rating": rating,
                "poster": poster
            }

        with open(self.file_path, "w") as file_obj:
            json.dump(data, file_obj)


    def delete_movie(self, title):
        """Deletes a movie by title."""
        with open(self.file_path, "r") as file_obj:
            data = json.load(file_obj)
            if title not in data:
                raise ValueError(f"Movie '{title}' not found")
            else:
                del data[title]
        with open(self.file_path, "w") as file_obj:
            json.dump(data, file_obj)

    def update_movie(self, title, rating):
        """Updates the rating of an existing movie."""
        with open(self.file_path, "r") as file_obj:
            data = json.load(file_obj)
            if title not in data:
                raise ValueError(f"The entry '{title}' doesn't exist.")
            else:
                data[title]["rating"] = rating

        with open(self.file_path, "w") as file_obj:
            json.dump(data, file_obj)