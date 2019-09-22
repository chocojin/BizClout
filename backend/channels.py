from googleapiclient.discovery import build
from .key import API_KEY

class Channel():
    def __init__(self, channelId, title, **kwargs):
        self.channelId = channelId
        self.title = title
        for key, value in kwargs.items():
            setattr(self, key, value)

    def toJSON(self):
        return {self.title :
                            {"subscriber" : self.subscriberCount,
                             "description" : self.description}
                             }

def channelSC(query, maxResults, safeSearch, **kwargs):
    """
    Searches youtube for channels,

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
                        subscriberCount=item['statistics']['subscriberCount'],
                        description=item['snippet']["localized"]['description']))

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

def minMax(channels, min, max):
    cha = len(channels)
    mi = 0
    ma = cha - 1
    while mi <= len(channels):
        if channels[mi].subscriberCount >= min:
            break
        if mi == cha:
            return []

        mi += 1

    while ma >= 0:
        if channels[ma].subscriberCount <= max:
            break
        if ma == cha:
            return []

        max -= 1

    return channels[mi:ma+1]

def channelJSONS(channels):
    dict = {}
    for channel in channels:
        dict.update(channel.toJSON())

    return dict


if __name__ == "__main__":
    pass
