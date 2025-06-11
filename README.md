from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_NAME = "يوكي"
TELEGRAM_TOKEN = "8090627940:AAGcqn97Zwbxc4hn6_Z2f00G17Lvw3EK9vE"

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"مرحبًا! أنا {BOT_NAME} 💙 جاهزة للدردشة معك 😘")

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    print("✅ البوت يعمل الآن... أرسل /start في تيليغرام.")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
