import datetime as dt
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import os

SPOTIFY_ID = os.environ["SPOTIFY_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_SECRET"]
USER_NAME = os.environ["USER_NAME"]


def date_check() -> str:
    """Enter date until desired format and return date in string format"""
    input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        date = dt.datetime.strptime(input_date, "%Y-%m-%d")
    except ValueError:
        print("Enter date in above format")
        return date_check()
    else:
        formatted_date = date.strftime("%Y-%m-%d")
        return formatted_date


user_date = date_check()
# print(user_date)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}/")
billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")

# songs_tag = soup.find_all(name="h3", attrs={'class':'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only'})

# for song in songs_tag:
#     songs = song.getText().strip()
#     print(songs)

songs_tag = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in songs_tag]
# print(song_names)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt",
    username=USER_NAME
))
user_id = sp.current_user()["id"]
print(user_id)

year = user_date.split("-")[0]
song_urls = []

# Searching Spotify for songs by title
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint.pprint(result["tracks"]["items"][0]["uri"])
    # print(result)
    try:
        url = result["tracks"]["items"][0]["uri"]
        song_urls.append(url)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

# print(song_urls)

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)  # item is list of song urls
