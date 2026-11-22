#!/usr/bin/env python3
"""Generate the data used by the Sint Maarten crossword pages."""

import json
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(SCRIPT_DIR, "crossword_data.json")

TOTAL_COLS = 14
SECRET_COL = 6

ROWS = [
    {"length": 7, "start": 3, "artist": "Suzan & Freek", "spotifyId": "2ZodgwtywVovNUNIcKDpbD"},
    {"length": 9, "start": 5, "artist": "Roxy Dekker & Ronnie Flex", "spotifyId": "6MUfSTr5MKTgX9oziFxx8c"},
    {"length": 8, "start": 0, "artist": "DIKKE", "spotifyId": "4BTiunrWSAMGCB4HuvqYJr"},
    {"length": 7, "start": 0, "artist": "Olivia Rodrigo", "spotifyId": "55pBIZO1cqoldeqpp5WR7H"},
    {"length": 4, "start": 6, "artist": "Justin Bieber", "spotifyId": "6epn3r7S14KUqlReYr77hA"},
    {"length": 4, "start": 4, "artist": "Mauvais Djo", "spotifyId": "0PMhBcbq0a5EDngAlVQLAy"},
    {"length": 9, "start": 4, "artist": "Tate McRae", "spotifyId": "2sFepQNyl1WjpROruP8bJ0"},
    {"length": 9, "start": 4, "artist": "Pommelien Thijs", "spotifyId": "3bxhuc9hkpZpOJFHxq2qri"},
    {"length": 11, "start": 2, "artist": "Frenna", "spotifyId": "4skvJoTBLEYUfS3Z1xvGjs"},
    {"length": 7, "start": 3, "artist": "Lil' Kleine", "spotifyId": "0JdKB06zZsPXmfvQVeJS35"},
    {"length": 7, "start": 3, "artist": "Ronnie Flex", "spotifyId": "1riPE3NCV1OBmSXqpYiMJY"},
    {"length": 9, "start": 0, "artist": "Bilal Wahid", "spotifyId": "1PHlNckjnBedkWSNhQ6nvr"},
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
