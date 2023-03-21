import csv
import os
import spotipy
import spotipy.oauth2 as oauth2
from datetime import datetime, timedelta

def get_spotify_client():
    """
    gets and returns spotify client for scraping

    Parameters
    ----------
    None

    Returns
    -------
    spotify_client:  Spotify Object
        spotify client class object
    """
        
    # Replace with your own client_id and client_secret
    client_id = '95d9c291d27243a79d7df296c4e16ef5'
    client_secret = '0b5ea70492c24776851815b4ee39423b'

    # Set up OAuth2 client credentials
    credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    # Set up spotipy client with auth token
    spotify_client = spotipy.Spotify(client_credentials_manager=credentials)
    return spotify_client

def get_date():
    """
    gets and returns the date in a string format

    Parameters
    ----------
    None

    Returns
    -------
    last_week_str: str
        string representation of datetime
    """
    # Get the date for last week
    last_week = datetime.today() - timedelta(days=7)
    last_week_str = last_week.strftime('%Y-%m-%d')
    return last_week_str

def get_playlist(spotify_client, last_week_str):
    """
    Gets the Spotify Top 200 playlist, track URLs and Names, as well as the
    audio features provided by spotify for each track url

    Parameters
    ---------
    spotify_client: Spotify Instance
        class object for scraping
    last_week_str: str
        date in string format for naming the playlist

    Returns
    -------
    track_names: list
        list of track names 
    artist_names: list
        list of artist names
    audio_features: list
        list of audio features
    """

    # Get the Spotify Top 200 playlist from last week
    playlist_name = f'Top 200 Weekly - {last_week_str}'
    results = spotify_client.search(q=playlist_name, type='playlist')

    # if the playlist empty, exit
    if len(results['playlists']['items']) == 0:
        print(f"No playlist found with name '{playlist_name}'")
        exit()

    # otherwise get the list of tracks and results from the playlist id
    playlist_id = results['playlists']['items'][0]['id']
    results = spotify_client.playlist_items(playlist_id)
    tracks = results['items']

    # Get the track URLs and names, song names
    track_urls = []
    track_names = []
    artist_names = []
    song_ranks = []
    for i, item in enumerate(tracks):
        track = item['track']
        track_url = track['external_urls']['spotify']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        song_rank = i + 1
        track_urls.append(track_url)
        track_names.append(track_name)
        artist_names.append(artist_name)
        song_ranks.append(song_rank)

    # Scrape the audio features for each track
    audio_features = []
    for url in track_urls:
        # Get the track id from the url
        track_id = url.split('/')[-1]
        # Get the audio features for the track
        features = spotify_client.audio_features(track_id)[0]
        # Add the features to the list
        audio_features.append(features)
    return track_names, artist_names, audio_features, song_ranks

def write_to_csv(sp, last_week_str, track_names, artist_names, audio_features, song_ranks):
    """
    Given the scraped audio features, write them to a new csv file in a clean
    formatting

    Parameters
    ----------
    sp: Spotify Instance
        spotify class object
    last_week_str: str
        datetime string for the file name
    track_names: list
        list of track names to iterate through so we can write the names from
    artist_names: list
        list of artist names for each track
    audio_features: list
        list of audio_features to iterate through so we can write to our outfile
    song_ranks: list
        list of song ranks in order

    Returns
    -------
    None
    """

    # define a filename
    filename = os.path.join('..', '..', 'data', f'{last_week_str}spotify_features.csv')

    # Write the features to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Track Name', 
                         'Artist Name',
                         'Rank',
                         'Acousticness', 
                         'Danceability', 
                         'Energy', 
                         'Instrumentalness',
                         'Liveness', 
                         'Speechiness', 
                         'Tempo', 
                         'Valence'])
        
        # Write the features for each track
        for i, features in enumerate(audio_features):
            writer.writerow([track_names[i], 
                             artist_names[i],
                             song_ranks[i],
                             features['acousticness'], 
                             features['danceability'],
                             features['energy'], 
                             features['instrumentalness'],
                             features['liveness'], 
                             features['speechiness'],
                             features['tempo'], 
                             features['valence']])
            
def main():
    """
    Driver code for the scraping pipeline
    """

    spotify_client = get_spotify_client()
    date_string = get_date()
    track_names, artist_names, audio_features, song_ranks = get_playlist(spotify_client, date_string)
    write_to_csv(spotify_client, 
                 last_week_str=date_string, 
                 artist_names=artist_names,
                 track_names=track_names, 
                 audio_features=audio_features,
                 song_ranks=song_ranks)

if __name__ == '__main__':
    main()