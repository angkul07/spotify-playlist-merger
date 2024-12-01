import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

os.environ["SPOTIPY_CLIENT_ID"] = "1ff17c647cc0470d8e43163cfcde1a90"
os.environ["SPOTIPY_CLIENT_SECRET"] = "bad7e35779d040f1a73ae6a1b0a3ebde"

auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1ff17c647cc0470d8e43163cfcde1a90",
                                               client_secret="bad7e35779d040f1a73ae6a1b0a3ebde",
                                               redirect_uri="http://localhost:1234/",
                                               scope="playlist-modify-public"
                                               ))

# playlist, playlist_add_items, playlist_tracks, spotify:track:6rqhFgbbKwnb9MLmUQDhG6, https://open.spotify.com/track/5ubHAQtKuFfiG4FXfLP804?si=3675caa50d2548c9

url1 = input("Enter the url of playlist 1: ")
url1 = url1.split('/')
id1 = url1[len(url1)-1]

url2 = input("Enter the url of playlist 2: ")
url3 = url2

play2_tracks = sp.playlist_tracks(url2, fields='items.track.id,total', additional_types=('track',))

uri2 = []
for item in play2_tracks['items']:
    uri2.append(item['track']['id'])

uri_list = []
for uri in uri2:
    uri_list.append("https://open.spotify.com/track/"+uri)

# print(uri_list)


# add_to_lists = []
# for uri in uri_list:
add_to_list = sp.playlist_add_items(id1, uri_list)
# add_to_lists.append(add_to_list)

# print(add_to_lists)



