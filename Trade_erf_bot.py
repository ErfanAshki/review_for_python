import telebot

bot = telebot.TeleBot("7493602619:AAHdWiW2SFsyRAlx9lmbNzlcspaJttUbzeg")

@bot.message_handler(commands=['start', 'hello'])
def something(message):
    bot.reply_to(message, 'slm chetori ?')
    
bot.infinity_polling()

