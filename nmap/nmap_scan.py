import telebot
import subprocess

# Your bot token from BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(BOT_TOKEN)

# Replace with your own Telegram ID to limit access
ALLOWED_USER_ID = 123456789

@bot.message_handler(commands=['scan'])
def scan_handler(message):
    if message.from_user.id != ALLOWED_USER_ID:
        bot.reply_to(message, "Access denied.")
        return

    target = message.text.split(' ', 1)[-1]
    if not target:
        bot.reply_to(message, "Please specify a target. Usage: /scan 192.168.1.1")
        return

    try:
        result = subprocess.check_output(['nmap', '-sV', target], stderr=subprocess.STDOUT, timeout=60)
        bot.reply_to(message, f"Scan results for {target}:\n```\n{result.decode()}\n```", parse_mode='Markdown')
    except subprocess.CalledProcessError as e:
        bot.reply_to(message, f"Scan error:\n{e.output.decode()}")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.polling()
