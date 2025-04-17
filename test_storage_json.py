from storage_json import StorageJson

storage = StorageJson("data_static_original.json")  # or whatever file you're using

# Try adding a new movie
storage.add_movie("Interstellar", 2014, 8.6, "http://poster.url")

# # Try adding the same movie again (should raise an error)
# storage.add_movie("Interstellar", 2014, 8.6, "http://poster.url")

# storage.delete_movie("Interstellar")   # Should succeed if it's in the file
# storage.delete_movie("Interstellar")   # Should raise ValueError the second time

storage.update_movie("Interstellar", 9.9)

