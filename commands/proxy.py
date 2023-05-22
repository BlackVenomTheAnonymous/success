import requests
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from free_proxy import FreeProxy

def fetch_proxy(update: Update, context: CallbackContext):
    # Get a free working proxy
    proxy = FreeProxy().get()

    if proxy:
        # Send the proxy information to the user
        message = f"🔒 Proxy: {proxy}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        message = "Failed to fetch a proxy 😔"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("proxy", fetch_proxy))
