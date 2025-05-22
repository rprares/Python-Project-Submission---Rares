import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

def fetch_movies_by_genre(genre):
    url = f"https://www.imdb.com/search/title/?genres={genre}&groups=top_1000&sort=user_rating"

    headers = {"Accept-Language": "en-US,en;q=0.5",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    movies = []
    for card in soup.select('li.ipc-metadata-list-summary-item'):

        title_tag = card.select_one('a.ipc-title-link-wrapper')
        print(title_tag.text)
        if title_tag:
            title = title_tag.text.strip()
            movies.append({"title": title, "genre": genre})
    return pd.DataFrame(movies)

user_genre = input("Enter genre (e.g. action, comedy, drama): ").lower()
df = fetch_movies_by_genre(user_genre)

if df.empty:
    print("No Movies Found. Make sure the genre is valid")
else:
    df.to_csv("scraped_movies.csv", index=False)
    print (f"Found {len(df)} '{user_genre}' movies")
    suggestion = random.choice(df["title"].tolist())
    print (f"Movie suggestion for you: **{suggestion}**")