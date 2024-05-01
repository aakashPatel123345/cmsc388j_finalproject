import os
import requests
import base64

class Song(object):
    def __init__(self, omdb_json, detailed=False):
        # Add the stuff from get_song
        self.name = omdb_json['name']  
        self.album_name = omdb_json['album_name']
        self.artists = omdb_json['artists']
        self.release_date = omdb_json['release_date']
        self.duration = omdb_json['duration']
        self.popularity = omdb_json['popularity']
        self.image_url = omdb_json['image_url']
        self.id = omdb_json['id']
        self.preview_url = omdb_json['preview_url']


    def __repr__(self):
        return self.name



class SpotifyClient:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.access_token_expires = None

    def get_client_credentials(self):
        """Encodes the client_id and client_secret to base64 as required for Spotify OAuth."""
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_access_token(self):
        """Obtains the access token using the client credentials grant type."""
        auth_string = self.client_id + ":" + self.client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}
        result = requests.post(url, headers=headers, data=data)
        json_result = result.json()
        self.access_token = json_result["access_token"]
        print(self.access_token)

        
    def get_music_data(self, query):
        """Retrieves music data from Spotify."""
        search_url = "https://api.spotify.com/v1/search"
        search_headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        search_params = {
            "q": query,
            "type": "track",
            "limit": 16
        }
        response = requests.get(search_url, headers=search_headers, params=search_params)
        if response.status_code == 200:
            # Now I want to do the same as above but return a list of the songs
            data = response.json()
            tracks = []
            if data['tracks']['items']:
                for track in data['tracks']['items']:
                    track_info = {}
                    track_info['name'] = track['name']
                    track_info['album_name'] = track['album']['name']
                    track_info['artists'] = track['artists']
                    track_info['release_date'] = track['album']['release_date']
                    track_info['duration'] = track['duration_ms']
                    track_info['popularity'] = track['popularity']
                    track_info['image_url'] = track['album']['images'][0]['url']
                    track_info['id'] = track['id']
                    track_info['preview_url'] = track['preview_url']
                    tracks.append(track_info)
            return tracks
        else:
            raise ValueError("Failed to retrieve search results, status code: {response.status_code}")
        


    def get_song(self, song_id):
        url = f"https://api.spotify.com/v1/tracks/{song_id}"
        # We will return a dictionary with the song information
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200: 
            data = response.json()
            song_info = {
                'name': data['name'],
                'album_name': data['album']['name'],
                'artists': [artist['name'] for artist in data['artists']],
                'release_date': data['album']['release_date'],
                'duration': data['duration_ms'],
                'popularity': data['popularity'],
                'image_url': data['album']['images'][0]['url'],
                'id': data['id'],
                # Add preview after testing
                'preview_url': data['preview_url']
            }
            song = Song(song_info)
            return song
        else:
            raise ValueError(f"Failed to retrieve song, status code: {response.status_code}")