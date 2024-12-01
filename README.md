# Spotify Playlist Merger
This Python script merges tracks from one Spotify playlist into another using the Spotipy library and Spotify Web API.

### Features
- Fetch tracks from a source playlist.
- Add tracks to a target playlist.

### Requirements
- Python 3.10 or higher.
- A Spotify account.
- Spotify Developer credentials (Client ID, Client Secret, and Redirect URI).

### Setup Instructions
1. Clone the Repository
```
git clone <repository_url>
cd <repository_folder>
```
   
2. Install Dependencies
Install the required Python libraries using pip:
```
pip install spotipy
```

4. Configure Spotify Developer Account
- Log in to the Spotify Developer Dashboard.
- Create a new application.
- Note the Client ID, Client Secret, and set a Redirect URI (e.g., http://localhost:1234).

4. Update Script with Credentials
Replace the placeholders in the script with your Spotify Developer credentials:
```
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="SPOTIPY_CLIENT_ID",  # Replace this
                                               client_secret="SPOTIPY_CLIENT_SECRET",  # Replace this
                                               redirect_uri="http://localhost:1234", # Use your redirect URI
                                               scope="playlist-modify-public"
                                               ))
```

### Usage
- Run the script.
- Enter the playlist 1 link and playlist 2 link in terminal.
- Playlist merged!

### Notes
- Ensure both playlists are public or owned by your account.
- The script supports up to 100 tracks at a time due to Spotify API limitations. Modify as needed for larger playlists.
- If using a different scope (e.g., private playlists), update the scope in the script accordingly.

