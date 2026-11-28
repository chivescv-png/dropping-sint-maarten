#!/usr/bin/env python3
"""Generate the data used by the Sint Maarten crossword pages."""

import json
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(SCRIPT_DIR, "crossword_data.json")

TOTAL_COLS = 20
SECRET_COL = 12

ROWS = [
    {"length": 7, "start": 9, "artist": "Suzan & Freek", "spotifyId": "2ZodgwtywVovNUNIcKDpbD", "appleId": "1845874656"},
    {"length": 9, "start": 11, "artist": "Roxy Dekker & Ronnie Flex", "spotifyId": "6MUfSTr5MKTgX9oziFxx8c", "appleId": "1753741796"},
    {"length": 8, "start": 6, "artist": "DIKKE", "spotifyId": "4BTiunrWSAMGCB4HuvqYJr", "appleId": "1638882049"},
    {"length": 7, "start": 6, "artist": "Olivia Rodrigo", "spotifyId": "55pBIZO1cqoldeqpp5WR7H", "appleId": "6771598356"},
    {"length": 4, "start": 12, "artist": "Justin Bieber", "spotifyId": "6epn3r7S14KUqlReYr77hA", "appleId": "1440803626"},
    {"length": 4, "start": 10, "artist": "Mauvais Djo", "spotifyId": "0PMhBcbq0a5EDngAlVQLAy", "appleId": "6813131671"},
    {"length": 9, "start": 10, "artist": "Tate McRae", "spotifyId": "2sFepQNyl1WjpROruP8bJ0", "appleId": "6822497774"},
    {"length": 9, "start": 10, "artist": "Pommelien Thijs", "spotifyId": "3bxhuc9hkpZpOJFHxq2qri", "appleId": "1829654536"},
    {"length": 11, "start": 2, "artist": "Frenna", "spotifyId": "4skvJoTBLEYUfS3Z1xvGjs", "appleId": "1808950758"},
    {"length": 7, "start": 9, "artist": "Lil' Kleine", "spotifyId": "0JdKB06zZsPXmfvQVeJS35", "appleId": "1440878599"},
    {"length": 7, "start": 9, "artist": "Ronnie Flex", "spotifyId": "1riPE3NCV1OBmSXqpYiMJY", "appleId": "1440899681"},
    {"length": 9, "start": 6, "artist": "Bilal Wahid", "spotifyId": "1PHlNckjnBedkWSNhQ6nvr", "appleId": "1831696505"},
]


def build_data():
    return {
        "title": "Sint Maarten gaat op stap",
        "eyebrow": "Dropping · Muziekpuzzel",
        "subtitle": "Vul de liedjes in - de gouden kolom verraadt het geheim",
        "totalCols": TOTAL_COLS,
        "secretCol": SECRET_COL,
        "rows": ROWS,
    }


def main():
    data = build_data()
    with open(OUTPUT_JSON, "w", encoding="utf-8") as output:
        json.dump(data, output, ensure_ascii=False, indent=2)
        output.write("\n")

    print("Generated crossword_data.json")


if __name__ == "__main__":
    main()
