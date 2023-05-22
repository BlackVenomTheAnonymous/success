import requests
import json
import emoji
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def check(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Extract the bin from the user's message
    _, bin_number = message.text.split()

    # Make a request to the binlist API
    response = requests.get(f"https://lookup.binlist.net/{bin_number}")

    if response.status_code == 200:
        card_data = response.json()

        # Extract relevant card details
        scheme = card_data.get("scheme", "Unknown")
        brand = card_data.get("brand", "Unknown")
        country = card_data.get("country", {}).get("name", "Unknown")
        emoji_flag = emoji.emojize(f":flag_{card_data.get('country', {}).get('emoji', 'white')}:")
        bank = card_data.get("bank", {}).get("name", "Unknown")

        # Format the response message
        response_text = f"Card Information:\n\n" \
                        f"BIN: {bin_number}\n" \
                        f"Scheme: {scheme}\n" \
                        f"Brand: {brand}\n" \
                        f"Country: {emoji_flag} {country}\n" \
                        f"Bank: {bank}"

        # Send the response back to the user
        context.bot.send_message(chat_id=chat_id, text=response_text, parse_mode="Markdown")
    else:
        # Handle the case when the API request fails
        context.bot.send_message(chat_id=chat_id, text="Unable to retrieve card information at the moment.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("check", check))
