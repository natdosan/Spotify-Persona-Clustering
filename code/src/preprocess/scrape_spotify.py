import csv
import os
import spotipy
import spotipy.oauth2 as oauth2
from datetime import datetime, timedelta

def get_spotify_client():
        
    # Replace with your own client_id and client_secret
    client_id = '95d9c291d27243a79d7df296c4e16ef5'
    client_secret = '0b5ea70492c24776851815b4ee39423b'

    # Set up OAuth2 client credentials
    credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    # Set up spotipy client with auth token
    sp = spotipy.Spotify(client_credentials_manager=credentials)
    return sp

def get_date():
    # Get the date for last week
    last_week = datetime.today() - timedelta(days=7)
    last_week_str = last_week.strftime('%Y-%m-%d')
    return last_week_str

def get_playlist(sp, last_week_str):

    # Get the Spotify Top 200 playlist from last week
    playlist_name = f'Top 200 Weekly - {last_week_str}'
    results = sp.search(q=playlist_name, type='playlist')
    if len(results['playlists']['items']) == 0:
        print(f"No playlist found with name '{playlist_name}'")
        exit()
    playlist_id = results['playlists']['items'][0]['id']
    results = sp.playlist_items(playlist_id)
    tracks = results['items']

    # Get the track URLs and names
    track_urls = []
    track_names = []
    for item in tracks:
        track = item['track']
        track_url = track['external_urls']['spotify']
        track_name = track['name']
        track_urls.append(track_url)
        track_names.append(track_name)

    # Scrape the audio features for each track
    audio_features = []
    for url in track_urls:
        # Get the track id from the url
        track_id = url.split('/')[-1]
        # Get the audio features for the track
        features = sp.audio_features(track_id)[0]
        # Add the features to the list
        audio_features.append(features)
    return track_names, audio_features

def write_to_csv(sp, last_week_str, track_names, audio_features):

    # Write the features to a CSV file
    filename = os.path.join('..', '..', 'data', f'{last_week_str}spotify_features.csv')
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(['Track Name', 'Acousticness', 'Danceability', 'Energy', 'Instrumentalness',
                        'Liveness', 'Speechiness', 'Tempo', 'Valence'])
        # Write the features for each track
        for i, features in enumerate(audio_features):
            writer.writerow([track_names[i], features['acousticness'], features['danceability'],
                            features['energy'], features['instrumentalness'],
                            features['liveness'], features['speechiness'],
                            features['tempo'], features['valence']])
            
def main():
    spotify_client = get_spotify_client()
    date_string = get_date()
    track_names, audio_features = get_playlist(spotify_client, date_string)
    write_to_csv(spotify_client, last_week_str=date_string, track_names=track_names, audio_features=audio_features)

if __name__ == '__main__':
    main()