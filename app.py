import telebot

TOKEN = 'TOKEN_SHOMA' # توکن را اینجا بگذار
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_resume(message):
    bot.reply_to(message, "🚀 پروژه فریلنسری پایتون فعال است.\nآماده برای کسب درآمد در کارلنسر.")

print("ربات آماده است...")
bot.polling()