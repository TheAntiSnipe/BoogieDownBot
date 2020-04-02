import requests
from bs4 import BeautifulSoup

def stagetwo(url):
	baseURL = f'{url}'
	r = requests.get(baseURL)
	soup = BeautifulSoup(r.text, 'html.parser')
	stageTwo = soup.find('div', {'id':'main'}).find('div',{'id':'content'}).find('div',{'class':'postcontent download'}).find_all('p')[3].find_all('a')[0].get('href')
	return stageTwo

if __name__ == '__main__':
	print(stagetwo('https://www.clubdancemixes.com/download/2019/03/Daft-Punk-Derezzed-ATLAST-Remix.mp3/'))