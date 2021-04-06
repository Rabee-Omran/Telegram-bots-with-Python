#Callback

from telegram.ext import Updater, CommandHandler, CallbackContext

updater = Updater(token="fff")
dispatcher = updater.dispatcher


# def start(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="Hello man")

def start(update: updater, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
updater.start_polling()
