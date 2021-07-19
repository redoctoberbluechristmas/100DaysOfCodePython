import azure
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from bs4 import BeautifulSoup
import os
import requests
import spotipy
import logging
from spotipy.oauth2 import SpotifyOAuth

# logger = logging.getLogger('examples.getPlaylist')
# logging.basicConfig(level='DEBUG')
scope = "user-library-read playlist-modify-private playlist-read-private"


def get_spotify_user_id():
    try:
        spotify_user_id = client.get_secret('spotify-user-id').value
    except azure.core.exceptions.ResourceNotFoundError:
        spotify_user_id = sp.current_user()['id']
        client.set_secret('spotify-user-id', spotify_user_id)
    return spotify_user_id

def get_track_uris(list_of_songs):
    song_uris = []
    # Get song ids
    for song in list_of_songs:
        result = sp.search(q=f"track:{song} year:{year_4_digit}", type="track")
        try:
            track_uri = result['tracks']['items'][0]['uri']
            song_uris.append(track_uri)
        except IndexError:
            print(f"{song} not in Spotify, skipped.")
    return song_uris

def manage_playlists(song_uris):
    playlist_name = f"Playlist: {month_2_digit}-{day_2_digit}-{year_4_digit}"
    existing_playlists = sp.user_playlists(user=spotify_user_id)['items']

    existing_playlist_names = []
    for i in existing_playlists:
        existing_playlist_names.append(i['name'])

    if playlist_name not in existing_playlist_names:
        create_and_update_playlist(playlist_name, song_uris)
    else:
        print("Playlist present. Exit.")
        exit

def create_and_update_playlist(playlist_name, song_uris):
    playlist = sp.user_playlist_create(
        user=spotify_user_id,
        name=f"Playlist: {playlist_name}",
        public=False,
        collaborative=False,
        description=f"Playlist of the top hits of {month_2_digit}-{day_2_digit}-{year_4_digit}"
    )

    playlist_id = playlist['id']
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)



# AUTHENTICATION BLOCK

keyvault_url = os.environ.get('KEYVAULT_URL')
credential = DefaultAzureCredential()
client = SecretClient(keyvault_url, credential)

#spotify_user_id = client.get_secret('spotify-user-id').value
spotify_playlist_id = "2hKYL1ZDp4rOlGnkDmCywf"
spotify_app_client_id = client.get_secret('spotify-app-client-id').value
spotify_app_client_secret = client.get_secret('spotify-app-client-secret').value
spotify_callback_url = client.get_secret('spotify-callback-url').value

# Instantiate client to get app token.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_app_client_id,
                                               client_secret=spotify_app_client_secret,
                                               redirect_uri=spotify_callback_url,
                                               scope=scope))

spotify_user_id = get_spotify_user_id()

SPOTIFY_BASE_URL = "https://api.spotify.com/v1"
SPOTIFY_CREATE_PLAYLIST_URL = f"{SPOTIFY_BASE_URL}/users/{spotify_user_id}/playlists"
SPOTIFY_ADD_PLAYLIST_URL = f"{SPOTIFY_BASE_URL}/playlists/{spotify_playlist_id}/tracks"
SPOTIFY_SEARCH_URL = f"{SPOTIFY_BASE_URL}/search"

# ACTUAL EXECUTION

travel_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

split_days = travel_date.split('-')
year_4_digit = split_days[0]
month_2_digit = split_days[1]
day_2_digit = split_days[2]

billboard_url = f"https://www.billboard.com/charts/hot-100/{year_4_digit}-{month_2_digit}-{day_2_digit}"

response = requests.get(billboard_url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

songs = soup.find_all(name='span', class_="chart-element__information__song text--truncate color--primary")
artists = soup.find_all(name='span', class_="chart-element__information__artist text--truncate color--secondary")

artists_list = [artist_name.getText() for artist_name in artists]
songs_list = [song_title.getText() for song_title in songs]

# Don't actually need this dictionary, just wanted to do it.
artist_and_song = [
    {
        'artist': artist,
        'song': song,
    } for artist,song in zip(artists_list, songs_list)
]

song_uris = get_track_uris(songs_list)

# CREATE AND POPULATE THE PLAYLIST

manage_playlists(song_uris)