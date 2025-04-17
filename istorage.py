from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """Returns all movies in storage."""

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """ Adds a movie to storage """

    @abstractmethod
    def delete_movie(self,title):
        """Deletes a movie by title."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """Updates the rating of an existing movie."""
        pass
