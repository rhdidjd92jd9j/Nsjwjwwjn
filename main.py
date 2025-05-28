from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Will get from Railway environment variables

async def alive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am alive!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("alive", alive))
    app.run_polling()
