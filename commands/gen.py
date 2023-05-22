import random
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def gen(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Extract the BIN and amount from the user's message
    _, bin_number, amount = message.text.split()

    try:
        amount = int(amount)
    except ValueError:
        context.bot.send_message(chat_id=chat_id, text="Invalid amount provided.")
        return

    if amount <= 0:
        context.bot.send_message(chat_id=chat_id, text="Amount should be a positive integer.")
        return

    # Generate the specified number of random credit card numbers based on the BIN
    credit_cards = []
    for _ in range(amount):
        card_number = f"{bin_number}{random.randint(1000000000, 9999999999)}"
        credit_cards.append(card_number)

    # Generate a filename for the text file
    filename = f"credit_cards_{bin_number}.txt"

    # Create the text file and write the credit card numbers
    with open(filename, "w") as file:
        file.write("\n".join(credit_cards))

    # Send the text file to the user
    context.bot.send_document(chat_id=chat_id, document=open(filename, "rb"))

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("gen", gen))
