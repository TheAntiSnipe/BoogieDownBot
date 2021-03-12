import requests
from bs4 import BeautifulSoup

def getThumbnail(tracks):
    baseURL = f'https://www.clubdancemixes.com/'
    r=requests.get(baseURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    tracksPane = soup.find('div', {'id':'main'}).find('div',{'id':'content_wrapper'}).find('div',{'id':'tracks'})
    songTile = tracksPane.find_all('div',{'class':'post post-index clearfix'})[tracks].find_all('div',{'class':'clearfix'})[0]
    thumbnail = songTile.find_all('div',{'class':'featured-image-box'})[0].find_all('a')[0].find_all('img')[0].get('src')
    return thumbnail

if __name__ == '__main__':
 	print(getThumbnail(1)) 