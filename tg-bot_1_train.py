#if you use windows: pip install telebot
#if you use mac: pip3 install telebot
#This bot take user-name who writing message.

import telebot

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Здарова. Напиши мне что-то.")

# In this block bot save user-name in text_file.
@bot.message_handler(content_types=['text'])
def message_handler1(message):
    userid4 = message.from_user.username
    with open("test.txt") as f:
        fd = f.read()
        fd=fd.split()
    if len(fd)==0:
        with open("bot_user.txt", 'a+') as f1:
            f1.write(str(userid4) + '\n')
    else:
        z=False
        for i in fd:
            print(str(userid4))
            if i==str(userid4):
                z=True
        if z==False:
            with open("bot_user.txt", 'a+') as f1:
                f1.write(str(userid4) + '\n')
    f.close()


bot.polling()
