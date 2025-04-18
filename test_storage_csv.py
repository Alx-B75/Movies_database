from storage_csv import StorageCsv

storage = StorageCsv("test_data.csv")  # Make sure this file exists with correct headers
movies = storage.list_movies()

print("🎬 Movies from CSV:")
for title, details in movies.items():
    print(f"{title}: {details}")

try:
    storage.add_movie(
        title="Arrival",
        year=2016,
        rating=8.0,
        poster="https://bit.ly/arrival-poster"
    )
    print("✅ Movie added successfully.")
except ValueError as e:
    print(f"⚠️ {e}")