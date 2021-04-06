#option

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

updater = Updater(token="ffff")
dispatcher = updater.dispatcher

def option(update: updater, context: CallbackContext) -> None:
    button = [
        [InlineKeyboardButton("Rabee Omran", callback_data="Rabee Omran"),
         InlineKeyboardButton("Gadeer Omran", callback_data="Gadeer Omran")],
        [InlineKeyboardButton("Mohammad Omran", callback_data="Mohammad Omran")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    update.message.reply_text(
                     text="Click anyone",
                     reply_markup=reply_markup)


option_handler = CommandHandler("option", option)
dispatcher.add_handler(option_handler)


def button(update: updater, _: CallbackContext) -> None:
    query = update.callback_query

    query.edit_message_text(text=f"Selected option: {query.data}")
 

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)
updater.start_polling()
