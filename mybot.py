import telebot
import time
import sys
import logging
import params
from objects import Response
from telebot import types
from request import weather
bot = telebot.TeleBot(params.API_TOKEN)

telebot.logger.setLevel(logging.DEBUG)
logger = telebot.logger


@bot.inline_handler(lambda query: len(query.query) > 3)
def default_query(inline_query):
    try:
        #check that the query is a location

        #convert the location to a lat,long

        #get the weather

        #send to the user
        location = inline_query.query
        response = weather(location)

        html1 = 'El tiempo actual en ' + location + 'es <b>'+response['currently']['summary'] + '</b>'
        html2 = '<a href="http://www.example.com/">inline URL</a> <a href="tg://user?id='+str(inline_query.from_user.id)+'">inline mention of a user</a>'
        html3 = ' <code>inline fixed-width code</code> <pre>pre-formatted fixed-width code block</pre>'
        resp1 = Response('El tiempo actual en ' + location, html1 )
        resp2 = Response('titulo 2', html2)
        resp3 = Response('titulo 3', html3)

        r1 = types.InlineQueryResultArticle(
            id = '1', 
            title = resp1.title, 
            input_message_content = types.InputTextMessageContent(message_text=resp1.content, parse_mode='HTML'))
        r2 = types.InlineQueryResultArticle(
            '2', resp2.title,             
            input_message_content = types.InputTextMessageContent(message_text=resp2.content, parse_mode='HTML'))
        r3 = types.InlineQueryResultArticle(
            '3', resp3.title,input_message_content = types.InputTextMessageContent(message_text=resp3.content, parse_mode='HTML'))
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
