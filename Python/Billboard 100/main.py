import requests
from bs4 import BeautifulSoup
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# GET BILLBOARD TOP 100 SONGS FOR THE GIVEN DATE
historical_date = input("Which historical Date you want to travel to? Type the date in YYYY-MM-DD: ")
year = historical_date.split("-")[0]
bill_board_hot_100 = "https://www.billboard.com/charts/hot-100/" + historical_date
print(bill_board_hot_100)

response = requests.get(bill_board_hot_100)
soup = BeautifulSoup(response.text, "html.parser")
billboard_song_tags = soup.select(selector="li ul li h3")
billboard_song_list = []
for songs in billboard_song_tags:
    billboard_song_list.append(songs.getText().strip())

# GET SPOTIFY SECRET KEY, ID AND REDIRECT URI
SPOTIFY_ID = config('SPOTIFY_ID', default='')
SPOTIFY_SECRET = config('SPOTIFY_SECRET', default='')
SPOTIFY_REDIRECT_URI = config('SPOTIFY_REDIRECT_URI', default='')

# CREATE TOKENS
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI,
                                               show_dialog=True, cache_path="token.env"))
user_id = sp.current_user()["id"]
spotify_uri = "spotify:track:"

# GET SPOTIFY TRACKS FROM THE TOP 10 BILLBOARD LIST
spotify_list = []

for song in billboard_song_list[:10]:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        spotify_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# ADD TO SPOTIFY PLAYLIST
playlist = sp.user_playlist_create(user=user_id, name=f"{historical_date} Billboard 10", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_list)

print(spotify_list)
