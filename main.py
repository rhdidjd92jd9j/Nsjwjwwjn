import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
BOT_TOKEN = '7808674214:AAFzx0mRxBdUPv4Xnf8tW-dT-tPPVLIyayk'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_alive(message):
    bot.reply_to(message, "I am alive")

print("Bot is running...")
bot.infinity_polling()
