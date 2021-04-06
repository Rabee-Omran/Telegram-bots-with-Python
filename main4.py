#Echo

from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

updater = Updater(token="fff")
dispatcher = updater.dispatcher


# def echo(bot, update):
#     bot.send_message(chat_id=update.message.chat_id,
#                      text=update.message.text.upper())


def echo(update: updater, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text.upper())


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
