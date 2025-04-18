import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

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

if __name__ == "__main__":
    from tmdb_client import search_movies_by_title

    try:
        movie = search_movies_by_title("Game")
        print("Movie data fetched successfully:")
        print(movie)
    except Exception as e:
        print("Error:", e)

