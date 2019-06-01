
from bs4 import  BeautifulSoup
from urllib.request import urlopen
class Bucks:
    def __init__(self, url):
        url = urlopen(url)
        soup = BeautifulSoup(url, 'html.parser')
        n_artists = 0
        n_title = 0

        for i in soup.find_all('p',attrs=({'class' : 'artist'})):
            n_artists += 1
            print('{} 위'.format(n_artists))
            print('아티스트 : {} '.format(i.find('a').text)) #text는 메소드가 아니라 속성값
        print('-----------')

        for i in soup.find_all(name='p', attrs=({'class':'title'})):
            n_title += 1
            print('{} 위'.format(str(n_title)))
            print('노래제목 : {}'.format(i.text))






