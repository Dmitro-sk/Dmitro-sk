

import telebot

token='8079271530:AAG07XZhwiwFnwULyRNE31XRTWwS5oEmjnM'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ ==  '__main__':
     bot.polling()
