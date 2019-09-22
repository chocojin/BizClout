from apiclient.discovery import build
from assets.static import API_KEY

class Channel():
    def __init__(self, channelId, title, **kwargs):
        self.channelId = channelId
        self.title = title
        for key, value in kwargs.items():
            setattr(self, key, value)

def channelSC(query, maxResults, safeSearch, **kwargs):
    """
    Searches youtube for channels

    Parameter query: Query to search for.
    Precondition: string, length > 0

    Parameter maxResults: How many channels to search for.
    Preconditiion: int > 0
    """
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    req = youtube.search().list(part='snippet', q=query, type='channel',
                                maxResults=maxResults, safeSearch=safeSearch)
    ref = req.execute()
    channelIds = []
    for item in ref['items']:
        channelIds.append(item['id']['channelId'])

    channelIds = ','.join(channelIds)
    req = youtube.channels().list(part='id, snippet, statistics',id=channelIds)
    ref = req.execute()
    channels = []
    for item in ref['items']:
        channels.append(Channel(item['id'], item['snippet']['title'],
                        subscriberCount=item['statistics']['subscriberCount']))

    return channels

def quickSort(channels, low, high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(channels, low, high):
    i = (low-1)
    pivot = channels[high].subscriberCount

    for j in range(low, high):
        if channels[j].subscriberCount < pivot:
            i += 1
            channels[i], channels[j] = channels[j], channels[i]

    channels[i+1], channels[high] = channels[high], channels[i+1]

if __name__ == "__main__":
    pass
