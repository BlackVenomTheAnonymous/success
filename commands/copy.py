import os
import shutil
import zipfile
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
import requests

def copy_website(update: Update, context: CallbackContext):
    # Retrieve the message and chat ID
    message = update.message
    chat_id = message.chat_id

    # Extract the website URL from the user's message
    _, url = message.text.split()

    # Copy the website to a temporary folder
    temp_folder = 'temp'
    try:
        # Create the temporary folder if it doesn't exist
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        # Download the website content
        response = requests.get(url)
        if response.status_code == 200:
            # Save the website content to a file
            temp_file = os.path.join(temp_folder, 'website.html')
            with open(temp_file, 'w', encoding='utf-8') as file:
                file.write(response.text)

            # Create a ZIP file containing the website content
            zip_file = 'website.zip'
            with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(temp_file, 'website.html')

            # Send the ZIP file to the user
            with open(zip_file, 'rb') as file:
                context.bot.send_document(chat_id=chat_id, document=file)

            # Remove the temporary files and folder
            os.remove(temp_file)
            os.remove(zip_file)
    except Exception as e:
        context.bot.send_message(chat_id=chat_id, text='An error occurred while copying the website.')
        print(str(e))
    finally:
        # Clean up the temporary folder
        shutil.rmtree(temp_folder, ignore_errors=True)

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("copy", copy_website))
