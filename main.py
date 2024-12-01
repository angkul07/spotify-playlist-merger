import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID",
                                               client_secret="SPOTIPY_CLIENT_SECRET",
                                               redirect_uri="http://localhost:1234", # Please enter your redirect uri. If not then leave it.
                                               scope="playlist-modify-public"
                                               ))


url1 = input("Enter the url of playlist 1: ")
url1 = url1.split('/')
id1 = url1[len(url1)-1]

url2 = input("Enter the url of playlist 2: ")

play2_tracks = sp.playlist_tracks(url2, fields='items.track.id,total', additional_types=('track',))

uri2 = []
for item in play2_tracks['items']:
    uri2.append(item['track']['id'])

uri_list = []
for uri in uri2:
    uri_list.append("https://open.spotify.com/track/"+uri)


add_to_list = sp.playlist_add_items(id1, uri_list)

print("Playlists merged!")



