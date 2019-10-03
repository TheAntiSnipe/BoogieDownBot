import requests
from bs4 import BeautifulSoup


def song_scrape(baseURL = "https://www.clubdancemixes.com/"):
    r=requests.get(baseURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    songs = {}
    track=0
    while track<5:
        post_content = soup.find('div', {'id':'main'}).find('div',{'id':'content_wrapper'}).find('div',{'id':'tracks'}).find_all('div',{'class':'post post-index clearfix'})[track].find_all('div',{'class':'clearfix'})[0].find_all('div',{'class':'post-content'})[0]
        track_title = post_content.find_all('h2',{'class':'post-title'})[0].text.strip()
        track_link = post_content.find_all('div',{'class':'track'})[0].find_all('a')[0].get('href')
        songs[track_title] = track_link
        track+=1
    return songs


if __name__=="__main__":
    print(song_scrape())
