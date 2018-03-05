import telebot
import time
import sys
import logging
from telebot import types

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)
logger = telebot.logger


@bot.inline_handler(lambda query: len(query.query) > 0)
def default_query(inline_query):
    try:
        #check that the query is a location

        #convert the location to a lat,long

        #get the weather

        #send to the user
        location = inline_query.query
        r1 = types.InlineQueryResultArticle(
            '1', 'El tiempo ahora en ' + location, types.InputTextMessageContent(
            'Contenido))
        r2 = types.InlineQueryResultArticle(
            '2', 'El tiempo esta noche en' + location, types.InputTextMessageContent(
            'Contenido'))
        r3 = types.InlineQueryResultArticle(
            '3', 'El tiempo manana en' + location, types.InputTextMessageContent(
            'Contenido'))
        bot.answer_inline_query(inline_query.id, [
                                r1, r2, r3], None, None, None, 'Recibe alertas del tiempo', 'x')
    except Exception as e:
        print(e)


def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
