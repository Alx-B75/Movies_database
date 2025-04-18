from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def main():
    storage = StorageJson("data_static_original.json")
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
