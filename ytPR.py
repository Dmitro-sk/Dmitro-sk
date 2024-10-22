import telebot

token="8079271530:AAG07XZhwiwFnwULyRNE31XRTWwS5oEmjnM"

bot = telebot.Telebot(token)

@bot_massage_handler (content_type=["text"])
def repeat_all_massage(massage):