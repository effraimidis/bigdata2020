import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_id = "92478d7941d144c7a79bb77eac8e422d"
client_secret = "e05180be387640c48efd73cbd03f7930"


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = ["Leonard Cohen"]
result = sp.search(name)
artist_id = result['tracks']['items'][1]['album']['artists'][0]['id']

# print(response.text)
# import base64
#
# encodedData = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")
# authorization_header_string = f"Authorization: Basic {encodedData}"
# print(authorization_header_string)

import requests

url = "https://api.spotify.com/v1/artists/" + artist_id

headers = {
    'Authorization': 'Bearer BQCjEXc4vm9trdWcoPsG1BH9UGjxEtb-lscgCwctvOKH_hSkYBAbYIdT9vIqRu7LrnuOCIZmjWCjxk48j4ahA02P1YMCVcq8S3PX6Zu0eQvui8V4X11_a5arvv1rqRN6RuM5F2z8On01EbQCu1XN'
}

response1 = requests.get(url, headers=headers)



url = "https://api.spotify.com/v1/artists/"+artist_id+"/albums"

headers = {
    'Authorization': 'Bearer BQCjEXc4vm9trdWcoPsG1BH9UGjxEtb-lscgCwctvOKH_hSkYBAbYIdT9vIqRu7LrnuOCIZmjWCjxk48j4ahA02P1YMCVcq8S3PX6Zu0eQvui8V4X11_a5arvv1rqRN6RuM5F2z8On01EbQCu1XN'
}

response2 = requests.get(url, headers=headers)



url = "https://api.spotify.com/v1/artists/"+artist_id+"/related-artists"

headers = {
    'Authorization': 'Bearer BQCjEXc4vm9trdWcoPsG1BH9UGjxEtb-lscgCwctvOKH_hSkYBAbYIdT9vIqRu7LrnuOCIZmjWCjxk48j4ahA02P1YMCVcq8S3PX6Zu0eQvui8V4X11_a5arvv1rqRN6RuM5F2z8On01EbQCu1XN'
}

response3 = requests.get(url, headers=headers)



url = "https://api.spotify.com/v1/artists/"+artist_id+"/top-tracks?country=GB"

headers = {
    'Authorization': 'Bearer BQCjEXc4vm9trdWcoPsG1BH9UGjxEtb-lscgCwctvOKH_hSkYBAbYIdT9vIqRu7LrnuOCIZmjWCjxk48j4ahA02P1YMCVcq8S3PX6Zu0eQvui8V4X11_a5arvv1rqRN6RuM5F2z8On01EbQCu1XN'
}

response4 = requests.get(url, headers=headers, )



