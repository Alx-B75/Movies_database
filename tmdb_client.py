import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"


def search_movies_by_title(title):
    """
    Fetch the movie data from TMDb by title.
    Returns a response object.
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": os.getenv("TMDB_API_KEY"),
        "query": title
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data["results"]:
        raise ValueError("Movie not found.")

    result_list = data["results"][:5]

    return result_list


def get_imdb_id(movie_id: int) -> Optional[str]:
    url = f"{BASE_URL}/movie/{movie_id}/external_ids"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("imdb_id")
    return None


if __name__ == "__main__":
    from tmdb_client import search_movies_by_title

    try:
        movie = search_movies_by_title("Game")
        print("Movie data fetched successfully:")
        print(movie)
    except Exception as e:
        print("Error:", e)
