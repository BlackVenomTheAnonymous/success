import os
from telegram import Update
from telegram.ext import Updater, CommandHandler

# Set up the bot
def main():
    # Initialize the updater and dispatcher
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    # Load all command modules from the "commands" folder
    command_folder = "commands"
    for filename in os.listdir(command_folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Remove the file extension ".py"
            module = __import__(f"{command_folder}.{module_name}", fromlist=[module_name])
            module.setup(dispatcher)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
