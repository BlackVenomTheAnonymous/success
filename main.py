from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater
import os

# Function to load commands from the commands folder
def load_commands(dispatcher):
    commands_folder = "./commands"
    for filename in os.listdir(commands_folder):
        if filename.endswith(".py"):
            command_module = filename[:-3]
            module = __import__(f"commands.{command_module}", fromlist=[command_module])
            module.setup(dispatcher)

def start(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Welcome message content
    welcome_message = f"Hey {message.from_user.mention_markdown_v2()}\n\nI'm CARD CHECKER [FREE CC CHECKER]. I can do several Things!😆\n\nClick on the buttons below to get Commands and Format!\n━━━━━━━━━━━━━\n🤖Admin : @GodFatherMob\n🤖Bot By @xerrox_army"

    # Send the welcome message to the user
    context.bot.send_message(chat_id=chat_id, text=welcome_message)

def unknown(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Unknown command message content
    unknown_message = "Sorry, I don't understand that command. Please check the available commands and formats."

    # Send the unknown command message to the user
    context.bot.send_message(chat_id=chat_id, text=unknown_message)

def setup_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Load commands from the commands folder
    load_commands(dispatcher)

# Set up the Telegram Bot
def main():
    # Replace 'TOKEN' with your actual bot token
    updater = Updater(token='TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # Set up command handlers
    setup_dispatcher(dispatcher)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
