import requests
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

API_URL = "https://cex.io/api"

def check_crypto_price(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Get the cryptocurrency symbol from the user's message
    _, symbol = message.text.split()

    # Send a request to the ticker API to get the cryptocurrency price
    ticker_url = f"{API_URL}/ticker/{symbol.upper()}/USD"
    ticker_response = requests.get(ticker_url)

    if ticker_response.status_code == 200:
        ticker_data = ticker_response.json()
        last_price = ticker_data.get('last')
        if last_price:
            emoji = '📈' if float(last_price) > 0 else '📉'
            message = f"The current price of {symbol.upper()} is {last_price} USD {emoji}"
        else:
            message = f"Could not find data for {symbol.upper()}"
    else:
        message = "Failed to fetch cryptocurrency price"

    # Send the price information to the user
    context.bot.send_message(chat_id=chat_id, text=message)

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("price", check_crypto_price))
