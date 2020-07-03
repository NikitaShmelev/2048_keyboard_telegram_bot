from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ReplyKeyboardRemove, Bot, Update
from telegram.utils.request import Request
from logging import getLogger

from user import users, User
from decorators import debug_requests, load_config
from tokens import BOT_API_TOKEN




@debug_requests
def do_start(update: Update, context=CallbackContext):
    user_id = update.message.chat_id
    if user_id in users.keys():
        print('good')
    else:
        print('shit')

def main():
    
    request = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    
    bot = Bot(
        request=request,
        token=BOT_API_TOKEN,
    )
    updater = Updater(
        bot=bot,
        use_context=True
        )
    
    print(bot.get_me())
    
    start_handler = CommandHandler(
        "start",
        do_start
    )
    # # Message handlers
    # text_message_handler = MessageHandler(
    #     Filters.text,
    #     take_text
    # )
    
    updater.dispatcher.add_handler(start_handler)
    # updater.dispatcher.add_handler(text_message_handler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()