import telebot
import time
import sys
import logging
import params
from objects import Response
from telebot import types

bot = telebot.TeleBot(params.API_TOKEN)

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
        resp1 = Response('titulo 1', 'El tiempo en' + location)
        resp2 = Response('titulo 2', 'El tiempo en' + location)
        resp3 = Response('titulo 3', 'El tiempo en' + location)

        r1 = types.InlineQueryResultArticle(
            '1', resp1.title, types.InputTextMessageContent(resp1.content))
        r2 = types.InlineQueryResultArticle(
            '2', resp2.title, types.InputTextMessageContent(resp2.content))
        r3 = types.InlineQueryResultArticle(
            '3', resp3.title, types.InputTextMessageContent(resp3.content))
        bot.answer_inline_query(inline_query.id, [r1, r2, r3], None, None, None, 'Recibe alertas del tiempo', 'x')
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
