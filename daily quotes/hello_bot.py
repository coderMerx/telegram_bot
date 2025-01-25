from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, World! Welcome to my Telegram bot!")

# Main function to run the bot
def main():
    # Load the API key from the environment variable
    api_token = os.getenv("API_KEY")
    
    # Check if the API key is available
    if not api_token:
        print("Error: API_KEY is not set in the environment variables.")
        return
    
    # Create the Application (bot instance)
    application = ApplicationBuilder().token(api_token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Start polling
    print("Bot is running... Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
