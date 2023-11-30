import spotipy
from spotipy.oauth2 import SpotifyOAuth
# spotipy 2.23.0

# Встановіть свої дані з Spotify Developer Dashboard
CLIENT_ID = 'client_id'
CLIENT_SECRET = 'client_secret'
REDIRECT_URI = 'http://localhost:8888/callback/'

# Створення об'єкта авторизації для доступу до лайкнутих треків
sp_likes = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                     client_secret=CLIENT_SECRET,
                                                     redirect_uri=REDIRECT_URI,
                                                     scope='user-library-read'))

# Ім'я файлу для зберігання назв лайкнутих треків
liked_tracks_output_file = 'liked_tracks.txt'

# Отримання лайкнутих треків
liked_tracks = sp_likes.current_user_saved_tracks()


# Запис назв лайкнутих треків у файл
with open(liked_tracks_output_file, 'w', encoding='utf-8') as file:
    file.write("Liked:\n")
    offset = 0
    while True:
        liked_tracks = sp_likes.current_user_saved_tracks(limit=50, offset=offset)
        if not liked_tracks['items']:
            break
        for item in liked_tracks['items']:
            track_info = item['track']
            track_name = track_info['name']
            artists = ', '.join([artist['name'] for artist in track_info['artists']])
            file.write(f"{track_name} - {artists}\n")
        offset += 50

print(f"like saved: {liked_tracks_output_file}")

        