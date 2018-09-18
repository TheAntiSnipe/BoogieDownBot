import time
import json
import requests
import urllib
import webscrap
from os import environ
import textwrap
try:
    import configparser
    from configparser import NoSectionError
except ImportError:
    import ConfigParser as configparser
    from ConfigParser import NoSectionError

from datetime import datetime
from threading import Timer
TOKEN = environ['TOKEN']
print(TOKEN)
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content



def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
            url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=markdown".format(text, chat_id)
    get_url(url)

def handle_updates(updates):
    for update in updates["result"]:
        if "channel_post" in update:
            text = update["channel_post"]["text"]
            chat = update["channel_post"]["chat"]["id"]
        else:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
        if text == "/start":
            intro_message = textwrap.dedent("""
            Welcome to MusicBot! This chatbot will give you the top 5 tracks on the www.clubdancemixes.com website! Hit /tracks to get the tracks!
            """)
            send_message(intro_message, chat)
        elif text == "/tracks":
            try:
                text1 = webscrap.song_scrape()
                chat = update["message"]["chat"]["id"]
                send_message(text1, chat)
            except Exception as e:
                print(e)

    

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
