from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Folder to store the downloaded files
DOWNLOAD_FOLDER = "downloaded_files"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! Send me a file and I'll store it for you!")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = None
    filename = None

    if update.message.document:
        file = await update.message.document.get_file()
        filename = update.message.document.file_name
    elif update.message.photo:
        file = await update.message.photo[-1].get_file()
        filename = f"{update.message.from_user.id}_photo.jpg"
    elif update.message.video:
        file = await update.message.video.get_file()
        filename = update.message.video.file_name or "video.mp4"
    elif update.message.audio:
        file = await update.message.audio.get_file()
        filename = update.message.audio.file_name or "audio.mp3"
    elif update.message.voice:
        file = await update.message.voice.get_file()
        filename = "voice.ogg"

    if file and filename:
        await file.download_to_drive(f"{DOWNLOAD_FOLDER}/{filename}")
        await update.message.reply_text(f"✅ File '{filename}' saved!")
    else:
        await update.message.reply_text("❌ Unsupported file type.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_file))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
