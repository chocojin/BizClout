from apiclient.discovery import build
from static import API_KEY

query = "business"
youtube = build('youtube','v3', developerKey=API_KEY)
req = youtube.search().list(part='snippet', q=query, type='channel', maxResults=50)
ref = req.execute()

for item in ref['items']:
    print(item['snippet']['title'])
