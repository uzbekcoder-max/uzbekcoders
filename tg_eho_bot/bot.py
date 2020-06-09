#!/usr/bin/python3

# importlar
import telebot

# bot tokenini token degan joyga qo'yamiz "ctrl+v"
bot = telebot.TeleBot(token)

# botni faqat textga javob beradigan qilamiz
@bot.message_handler(content_types=["text"])
def welcome(message):
    # bot yozilgan textga huddi o'sha text bilan javob beradigan qilamiz
    bot.send_message(message.chat.id, message.text)


# botni faqat online turishini buyuryapmiz
bot.infinity_polling(none_stop=True)