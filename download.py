import requests
import stagetwo
from bs4 import BeautifulSoup

def download_track(trackNo):
    baseURL = f'https://www.clubdancemixes.com/'
    r=requests.get(baseURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    tracklist= soup.find('div', {'id':'main'}).find('div',{'id':'content_wrapper'}).find('div',{'id':'tracks'})
    trackDetailsPane = tracklist.find_all('div',{'class':'post post-index clearfix'})[trackNo].find_all('div',{'class':'clearfix'})[0]
    songAnchorTag = trackDetailsPane.find_all('div',{'class':'post-content'})[0].find_all('div',{'class':'track'})[0].find_all('a')[0]
    songBaseLink = songAnchorTag.get('href')
    songBaseLink=songBaseLink[:-1]
    songBaseLink = 'https://www.clubdancemixes.com'+  stagetwo.stagetwo(songBaseLink)
    #songBaseLink+='?st=Tb43un7paxA8Ci9-XNmWzw&e=1539484241?fdl=1'
    return songBaseLink

if __name__ == '__main__':
    print(download_track(1))
