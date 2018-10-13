import requests
from bs4 import BeautifulSoup
def song_scrape():
    baseURL = f'https://www.clubdancemixes.com/'
    r=requests.get(baseURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    songNames=""
    track=0
    while track<5:
        songNames = songNames+ (soup.find('div', {'id':'main'}).find('div',{'id':'content_wrapper'}).find('div',{'id':'tracks'}).find_all('div',{'class':'post post-index clearfix'})[track].find_all('div',{'class':'clearfix'})[0].find_all('div',{'class':'post-content'})[0].find_all('h2',{'class':'post-title'})[0].text).strip()+"\n"
        track+=1
    return songNames
if __name__=="__main__":
    print(song_scrape())