# AIzaSyAqpWHpInnry3J5CqRfTsRWGlJWi7Csw2Q
# pip install google-api-python-client
from googleapiclient.discovery import build

def meklēt_youtube_video(api_atslēga, vaicājums, maksimālais_rezultāti=5):
    youtube = build('youtube', 'v3', developerKey=api_atslēga)

# Video meklēšana
    meklēšanas_atbilde = youtube.search().list(
        q=vaicājums,
        part='id,snippet',
        type='video',
        maxResults=maksimālais_rezultāti
    ).execute()
    video_saites = []

# Video detaļu iegūšana
    for meklēšanas_rezultāts in meklēšanas_atbilde.get('items', []):
        video_id = meklēšanas_rezultāts['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        video_saites.append(video_url)
    return video_saites

api_atslēga = 'AIzaSyAqpWHpInnry3J5CqRfTsRWGlJWi7Csw2Q'
vaicājums = 'Python programmēšanas pamācība'
rezultātu_saites = meklēt_youtube_video(api_atslēga, vaicājums)

print(f"Top {len(rezultātu_saites)} YouTube video par '{vaicājums}':")
for saite in rezultātu_saites:
    print(saite)
