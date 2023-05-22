import random
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def generate_card(update: Update, context: CallbackContext):
    # Available card brands
    brands = ["Visa", "Mastercard", "American Express", "Discover", "JCB", "Maestro"]

    # Extract the brand from the command arguments
    args = context.args
    if not args:
        message = "Please provide a card brand as a command argument."
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return

    brand = args[0].title()
    if brand not in brands:
        message = "Invalid card brand. Available brands are: {}".format(", ".join(brands))
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return

    # Generate a random card number
    card_number = generate_card_number(brand)
    
    # Validate the generated card number using the Luhn algorithm
    is_valid = validate_card_number(card_number)

    # Send the generated card number to the user
    if is_valid:
        message = "Brand: {}\nCard Number: {}".format(brand, card_number)
    else:
        message = "An error occurred while generating the card number."
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def generate_card_number(brand):
    # Generate a random card number based on the brand's format
    if brand == "Visa":
        return "4" + "".join(random.choice("0123456789") for _ in range(15))
    elif brand == "Mastercard":
        return "5" + "".join(random.choice("123456789") for _ in range(15))
    elif brand == "American Express":
        return "34" + "".join(random.choice("0123456789") for _ in range(13))
    elif brand == "Discover":
        return "6011" + "".join(random.choice("0123456789") for _ in range(11))
    elif brand == "JCB":
        return "35" + "".join(random.choice("0123456789") for _ in range(14))
    elif brand == "Maestro":
        return "6759" + "".join(random.choice("0123456789") for _ in range(11))

def validate_card_number(number):
    # Validate the card number using the Luhn algorithm
    qCheck = 0
    bEven = False
    number = number.replace("-", "").replace(" ", "")

    for n in range(len(number) - 1, -1, -1):
        cDigit = number[n]
        nDigit = int(cDigit)

        if bEven:
            if (nDigit := nDigit * 2) > 9:
                nDigit -= 9

        qCheck += nDigit
        bEven = not bEven

    return qCheck % 10 == 0

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("create", generate_card))
