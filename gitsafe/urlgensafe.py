import json
import urllib.request
import string
import random
from pytube import Search

def get_url():
    count = 1
    API_KEY = ''
    rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,rand)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))
    vid_id     = results['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v={vid_id}"  

def busca(query, search=False):

    pesquisa = Search(query).results
    if search:
         videoList = []
         for item in range(10):
              videoList.append(f"https://www.youtube.com/watch?v={pesquisa[item].video_id}")
         return videoList
    videoUrl = f"https://www.youtube.com/watch?v={pesquisa[0].video_id}"
    return videoUrl



def itsNothing():
    nothings = ('tuc ' * (random.randint(0,20)) + 'tuc')
    return nothings