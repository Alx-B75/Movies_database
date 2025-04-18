import json
import csv

# Update with your actual JSON file name
with open("data_static_original.json", "r") as json_file:
    json_data = json.load(json_file)

# Choose a CSV file to write to
with open("test_data.csv", "w", newline='') as csv_file:
    fieldnames = ["title", "rating", "year", "poster"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for title, details in json_data.items():
        writer.writerow({
            "title": title,
            "rating": details["rating"],
            "year": details["year"],
            "poster": details.get("poster", "")
        })
