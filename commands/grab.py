import requests
from urllib.parse import urlparse, parse_qs
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def grab(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Extract the checkout link from the user's message
    _, checkout_link = message.text.split()

    # Parse the URL and extract query parameters
    parsed_url = urlparse(checkout_link)
    query_params = parse_qs(parsed_url.query)

    # Extract the desired information from the query parameters
    cs_live = query_params.get('cs_live')
    pk_live = query_params.get('pk_live')
    amount = query_params.get('amount')
    email = query_params.get('email')

    # Check if the required information is present
    if cs_live and pk_live and amount and email:
        cs_live = cs_live[0]
        pk_live = pk_live[0]
        amount = amount[0]
        email = email[0]

        # Send the extracted information as a response
        response_text = f"CS Live: {cs_live}\nPK Live: {pk_live}\nAmount: {amount}\nEmail: {email}"
        context.bot.send_message(chat_id=chat_id, text=response_text)
    else:
        context.bot.send_message(chat_id=chat_id, text="Unable to extract required information.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("grab", grab))
