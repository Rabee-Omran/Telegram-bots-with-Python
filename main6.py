
from telegram.ext import Updater, CommandHandler, CallbackContext

updater = Updater(token="fff")
dispatcher = updater.dispatcher


def command(update: updater, context: CallbackContext) -> None:
    update.message.reply_text(text="/Welcome_message \n /Hello_message")


start_handler = CommandHandler("command", command)
dispatcher.add_handler(start_handler)





def welcome_message(update: updater, context: CallbackContext) -> None:
    update.message.reply_text(f'Welcome {update.effective_user.first_name}')

welcome_message_handler = CommandHandler("welcome_message", welcome_message)
dispatcher.add_handler(welcome_message_handler)




def hello_message(update: updater, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

hello_message_handler = CommandHandler("hello_message", hello_message)
dispatcher.add_handler(hello_message_handler)





updater.start_polling()

