# Movie Suggestion Bot

A Python script that scrapes IMDb's top-rated movies by genre and provides random movie suggestions.

## Description

This script allows users to:
- Input a movie genre of their choice
- Fetch top-rated movies in that genre from IMDb
- Save the movie list to a CSV file
- Get a random movie suggestion from the fetched list

## Requirements

- Python 3.x
- Required Python packages:
  - requests
  - beautifulsoup4
  - pandas

## Installation

Clone this repository:
``bash
git clone (https://github.com/rprares/Python-Project-Submission---Rares/)

Install required packages:

pip install requests beautifulsoup4 pandas

Usage
Run the script:

python movie_suggestion_bot.py


Enter a movie genre when prompted (e.g., action, comedy, drama)
  The script will:
    Fetch movies from IMDb
    Save them to 'scraped_movies.csv'
    Provide a random movie suggestion

Features

  Web scraping from IMDb's top 1000 movies
  Genre-based movie filtering
  CSV file export of movie data
  Random movie suggestion generator
  
  Data Output

The script creates a CSV file ('scraped_movies.csv') containing:

Movie titles
Associated genres

Notes

  This script uses IMDb's public web interface and should be used in accordance with IMDb's terms of service
  Internet connection required
  Some genres might return fewer results than others
