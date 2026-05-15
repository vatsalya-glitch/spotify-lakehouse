import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "../data/spotify_tracks.csv")

with open(csv_path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(f"Loaded {len(rows)} rows")