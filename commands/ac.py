import requests
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def ac(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Extract the CC raw link from the user's message
    _, cc_raw_link = message.text.split()

    # Fetch the raw content of the CC paste
    response = requests.get(cc_raw_link)
    if response.status_code == 200:
        cc_paste = response.text
        # Send the Stripe checkout link to the user
        context.bot.send_message(chat_id=chat_id, text="Please provide a Stripe Checkout Link.")
        context.user_data["cc_paste"] = cc_paste
    else:
        context.bot.send_message(chat_id=chat_id, text="Unable to fetch CC paste content.")

def fx(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Retrieve the CC paste from user data
    cc_paste = context.user_data.get("cc_paste")

    if cc_paste:
        # Perform actions with the CC paste for /fx command
        # Replace the following code with your desired logic
        response_text = f"Performing /fx action with CC paste:\n{cc_paste}"
        context.bot.send_message(chat_id=chat_id, text=response_text)
    else:
        context.bot.send_message(chat_id=chat_id, text="No CC paste found. Please use /ac command first.")

def fr(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Retrieve the CC paste from user data
    cc_paste = context.user_data.get("cc_paste")

    if cc_paste:
        # Perform actions with the CC paste for /fr command
        # Replace the following code with your desired logic
        response_text = f"Performing /fr action with CC paste:\n{cc_paste}"
        context.bot.send_message(chat_id=chat_id, text=response_text)
    else:
        context.bot.send_message(chat_id=chat_id, text="No CC paste found. Please use /ac command first.")

def nx(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Retrieve the CC paste from user data
    cc_paste = context.user_data.get("cc_paste")

    if cc_paste:
        # Perform actions with the CC paste for /nx command
        # Replace the following code with your desired logic
        response_text = f"Performing /nx action with CC paste:\n{cc_paste}"
        context.bot.send_message(chat_id=chat_id, text=response_text)
    else:
        context.bot.send_message(chat_id=chat_id, text="No CC paste found. Please use /ac command first.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("ac", ac))
    dispatcher.add_handler(CommandHandler("fx", fx))
    dispatcher.add_handler(CommandHandler("fr", fr))
    dispatcher.add_handler(CommandHandler("nx", nx))
