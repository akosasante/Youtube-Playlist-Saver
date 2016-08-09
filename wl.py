""" Pull All Youtube Videos from a Playlist """

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyBNT2tMNl9z6-_fBCVtm2Qq9JnYLuijaXc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def fetch_all_youtube_videos(playlistId):
    """
    Fetches a playlist of videos from youtube
    We splice the results together in no particular order

    Parameters:
        parm1 - (string) playlistId
    Returns:
        playListItem Dict
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    res = youtube.playlistItems().list(
    part="snippet",
    playlistId=playlistId,
    maxResults="50"
    ).execute()


    nextPageToken = res.get('nextPageToken')
    while ('nextPageToken' in res):
        nextPage = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlistId,
        maxResults="50",
        pageToken=nextPageToken
        ).execute()
        res['items'] = res['items'] + nextPage['items']

        if 'nextPageToken' not in nextPage:
            res.pop('nextPageToken', None)
        else:
            nextPageToken = nextPage['nextPageToken']

    return res

if __name__ == '__main__':
  # comedy central playlist, has 332 video
  # https://www.youtube.com/watch?v=tJDLdxYKh3k&list=PLD7nPL1U-R5rDpeH95XsK0qwJHLTS3tNT
  videos = fetch_all_youtube_videos("PLpQkXmSxI4N9pvT537s9IuHwLkZn9z6hB")

  f = open("list3.txt", "w")
  f.write(str(videos))
  f.close()
