# -*- coding: utf-8 -*-
import os
import logging
import textwrap
import random
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import webscrap

TOKEN = os.environ['TOKEN']
updater = Updater(TOKEN)

APP_URL = os.environ['APP_URL']
PORT = int(os.environ.get('PORT', '8443'))
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    intro_message = textwrap.dedent("""
    Welcome to BoogieDownBot! This chatbot will give you the top 5 tracks on the www.clubdancemixes.com website! Hit /tracks to get the tracks!
    """)
    bot.sendMessage(chat_id=update.message.chat_id, text=intro_message, parse_mode='markdown')

def tracks(bot, update):
    tracksFound = webscrap.song_scrape()
    bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
    bot.sendMessage(chat_id=update.message.chat_id, text=tracksFound, parse_mode='markdown')

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I don't know how to answer to that.")

def main():
    """Start the bot and use webhook to detect and respond to new messages."""
    dispatcher = updater.dispatcher
    # Handlers
    start_handler = CommandHandler('start', start)
    tracks_handler = CommandHandler('tracks', tracks)
    unknown_message = MessageHandler(Filters.text | Filters.command, unknown)

    # Dispatchers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(tracks_handler)
    dispatcher.add_handler(unknown_message)

    updater.start_webhook(listen='0.0.0.0',
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(APP_URL + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
