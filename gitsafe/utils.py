import json
import urllib.request
import string
import random
from pytube import Search
import requests
from bs4 import BeautifulSoup


def get_url():
    count = 1
    API_KEY = 'SUA API DO YOUTUBE'
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


def tuc(beast=False):
    if  beast and random.randrange(1,100) <= 8:
        noTucs = ["A verdade sempre está com a minoria, e a minoria é sempre mais forte do que a maioria, porque a minoria geralmente é formada por quem realmente tem opinião, enquanto a força da maioria é ilusória, formada pelas gangues que não têm opinião; e que, portanto, no próximo instante (quando é evidente que a minoria é a mais forte) assume sua opinião… Enquanto isso, a verdade novamente se reverte para uma nova minoria.", "Existir significa 'escolher', mas isso não representa a riqueza, mas a miséria do homem. Sua liberdade de escolha não é sua grandeza, mas seu drama permanente. De fato, ele sempre se depara com a alternativa de uma 'possibilidade de sim' e uma 'possibilidade de não', sem possuir qualquer critério seguro. E tateando no escuro numa posição instável de indecisão permanente.", "Não existe pátria para quem desespera e, quanto a mim, sei que o mar me precede e me segue, e minha loucura está sempre pronta. Aqueles que se amam e são separados podem viver sua dor, mas isso não é desespero: eles sabem que o amor existe. Eis porque sofro, de olhos secos, este exílio. Espero ainda. Um dia chega, enfim...", "Há um incêndio no interior de um teatro. O palhaço sobe ao palco para avisar o público. Eles pensam que é uma piada e aplaudem. O palhaço repete e é aplaudido com mais entusiasmo. É como eu penso que o mundo chegará ao seu fim: sendo aplaudido por testemunhas que acreditam que tudo não passa de uma piada", "De repente, estou só no mundo. Vejo tudo isto do alto de um telhado espiritual. Estou só no mundo. Ver é estar distante. Ver claro é parar. Analisar é ser estrangeiro. Toda a gente passa sem roçar por mim. Tenho só ar à minha volta. Sinto-me tão isolado que sinto a distância entre mim e o meu fato.", "De repente, estou só no mundo. Vejo tudo isto do alto de um telhado espiritual. Estou só no mundo. Ver é estar distante. Ver claro é parar. Analisar é ser estrangeiro. Toda a gente passa sem roçar por mim. Tenho só ar à minha volta. Sinto-me tão isolado que sinto a distância entre mim e o meu fato. "]
        return random.choice(noTucs)
    tucs = ('tuc ' * (random.randint(1,15)) + "tuc")
    return tucs


def getTitle(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = (soup.find("title").text)[:-10]
    
    return title


def spotifyToQuery(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = (soup.find("title").text)[:-10]
    title = title.replace(" - song and lyrics by", "")
    
    return title
