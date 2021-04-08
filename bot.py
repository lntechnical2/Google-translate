from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from google_trans_new import google_translator 
import os

BOT_TOKEN = os.environ.get('bot_token',None)

updater = Updater('BOT_TOKEN',use_context = True )

def start(updater,context):
 updater.message.reply_text('hi iam google translater ')
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator=google_translator()
 translate_text=translator.translate(usr_msg,lang_tgt='kn')
 updater.message.reply_text(translate_text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()