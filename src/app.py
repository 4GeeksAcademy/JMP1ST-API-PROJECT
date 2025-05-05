import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()


# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#Conecting with spotify api 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id='d6c92358581247659bd96971f897cda4', client_secret='ce7217aee183458d8d4c4001987d2f43')
spotify = spotipy.Spotify(auth_manager=auth_manager)

#Requesting api info 
#ID for Singer Rory Gallagher
Singer_ID = '1kcWyDvrlPUbyxkIoM6pAV' 

#Getting the most famous tracks from this singer (Rory Gallagher)
response = spotify.artist_top_tracks('1kcWyDvrlPUbyxkIoM6pAV') 

#Getting artist info to extract the genres 
artist_info = spotify.artist('1kcWyDvrlPUbyxkIoM6pAV')
genres = artist_info['genres']

#Empty list to store the songs values 
songs = list() 

#Getting the ms in minutes is done by div the t times 60000!!

for track in response['tracks']:
    songs.append({
        'name':             track['name'],
        'length':           round(((track['duration_ms']/1000)/60),2),
        'date':             track['album']['release_date'],
        'popularity':       track['popularity'],
        'expilict_lyrics':   track['explicit'],
        'genres':           genres[0]
        
    })

#Creating the DF
df = pd.DataFrame(songs)

#Ploting
sorted_df = df.sort_values(by='popularity', ascending=False)

#Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_df['name'], sorted_df['popularity'])
plt.xlabel('Songs')
plt.ylabel('Popularity')
plt.title("Popularity of Rory Gallagher's Most Listened Songs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()