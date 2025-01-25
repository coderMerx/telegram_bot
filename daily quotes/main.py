from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("7596323983:AAFY58EgQawxyWgICgyOicc-RIgKwiy9-WA")

# Main function to run the bot
def main():
    # Replace 'YOUR_API_TOKEN' with your bot's token
    api_token = "YOUR_API_TOKEN"

    # Create the Application (bot instance)
    application = ApplicationBuilder().token(api_token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))

    # Start polling
    application.run_polling()

if __name__ == "__main__":
    main()
