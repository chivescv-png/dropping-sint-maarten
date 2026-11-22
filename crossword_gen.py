#!/usr/bin/env python3
"""Generate the data used by the Sint Maarten crossword pages."""

import json
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(SCRIPT_DIR, "crossword_data.json")

TOTAL_COLS = 14
SECRET_COL = 6

ROWS = [
    {"word": "NIEMAND", "start": 3, "song": "Niemand", "artist": "Susan & Freek", "spotifyId": None},
    {"word": "GAANWEWEG", "start": 5, "song": "Gaan we weg", "artist": "Roxy Dekker & Ronnie Flex", "spotifyId": None},
    {"word": "GASOLINA", "start": 0, "song": "Gasolina", "artist": "DIKKE", "spotifyId": None},
    {"word": "THECURE", "start": 0, "song": "The Cure", "artist": "Olivia Rodrigo", "spotifyId": None},
    {"word": "BABY", "start": 6, "song": "Baby", "artist": "Justin Bieber", "spotifyId": None},
    {"word": "PILE", "start": 4, "song": "Pile", "artist": "Mauvais Djo", "spotifyId": None},
    {"word": "HOUSEWIFE", "start": 4, "song": "Housewife", "artist": "Tate McRae", "spotifyId": None},
    {"word": "CASSANDRA", "start": 4, "song": "Cassandra", "artist": "Pommelien Thijs", "spotifyId": None},
    {"word": "GIRLS", "start": 2, "song": "Pretty Girls", "artist": "Frenna", "spotifyId": None},
    {"word": "DUREGEINTJE", "start": 3, "song": "Dure Geintje", "artist": "LASSA & Mensa", "spotifyId": None},
    {"word": "ENERGIE", "start": 3, "song": "Energie", "artist": "Ronnie Flex", "spotifyId": None},
    {"word": "OVERDOSIS", "start": 0, "song": "Overdosis", "artist": "Bilal Wahid", "spotifyId": None},
]


def build_data():
    secret_word = "".join(
        row["word"][SECRET_COL - row["start"]]
        for row in ROWS
        if row["start"] <= SECRET_COL < row["start"] + len(row["word"])
    )

    return {
        "title": "Sint Maarten gaat op stap",
        "eyebrow": "Dropping · Muziekpuzzel",
        "subtitle": "Vul de liedjes in - de gouden kolom verraadt het geheim",
        "totalCols": TOTAL_COLS,
        "secretCol": SECRET_COL,
        "rows": ROWS,
        "secretWord": secret_word,
    }


def main():
    data = build_data()
    with open(OUTPUT_JSON, "w", encoding="utf-8") as output:
        json.dump(data, output, ensure_ascii=False, indent=2)
        output.write("\n")

    print("Generated crossword_data.json")
    print("Secret word:", data["secretWord"])


if __name__ == "__main__":
    main()
