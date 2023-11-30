from bs4 import BeautifulSoup 
import requests


date = input(" Which yaers do you want to travel to?  type the date in thid format YYYY-MM-DD : ")
response = requests.get("https://www.billboard.com/charts/hot-100/ " + date )

soup = BeautifulSoup(response.text , 'html.parser')

song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=" https://github.com/Tayyba27/CV-index ",
        client_id="18fa3292e3ab463dac374ef3d0ffdc54",
        client_secret="41fba742a5d2410a86fe59f07eb53aa8",
        show_dialog=True,
        cache_path="token.txt",
        username="tayaba anwer", 
    )
)
user_id = sp.current_user()["id"]

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



