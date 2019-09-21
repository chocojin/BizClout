from apiclient.discovery import build
from static import API_KEY

youtube = build('youtube','v3', developerKey=API_KEY)
req = youtube.search().list(part='snippet', q='business', type='channel')
ref = req.execute()

print(ref)
