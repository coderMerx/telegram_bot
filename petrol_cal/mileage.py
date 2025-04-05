import telebot

BOT_TOKEN = 'enter your token'
bot = telebot.TeleBot(BOT_TOKEN)

# Temporary storage for user input
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Hi! Let's calculate your trip cost.")
    bot.send_message(message.chat.id, "🚗 Enter the mileage of the vehicle (km/L):")
    bot.register_next_step_handler(message, ask_km)

def ask_km(message):
    try:
        user_data[message.chat.id] = {'mileage': float(message.text)}
        bot.send_message(message.chat.id, "📏 Enter the number of kilometers traveled:")
        bot.register_next_step_handler(message, ask_price)
    except ValueError:
        bot.send_message(message.chat.id, "❌ Please enter a valid number for mileage.")
        bot.register_next_step_handler(message, ask_km)

def ask_price(message):
    try:
        user_data[message.chat.id]['km'] = float(message.text)
        bot.send_message(message.chat.id, "⛽ Enter today's petrol price (₹/L):")
        bot.register_next_step_handler(message, calculate_cost)
    except ValueError:
        bot.send_message(message.chat.id, "❌ Please enter a valid number for kilometers.")
        bot.register_next_step_handler(message, ask_price)

def calculate_cost(message):
    try:
        user_data[message.chat.id]['price'] = float(message.text)
        data = user_data[message.chat.id]
        
        petrol_used = data['km'] / data['mileage']
        total_cost = petrol_used * data['price']

        reply = (
            f"🛣️ Trip Summary:\n"
            f"Mileage: {data['mileage']} km/L\n"
            f"Distance: {data['km']} km\n"
            f"Petrol Price: ₹{data['price']}/L\n\n"
            f"⛽ Petrol Used: {petrol_used:.2f} L\n"
            f"💸 Total Cost: ₹{total_cost:.2f}"
        )
        bot.send_message(message.chat.id, reply)
        user_data.pop(message.chat.id)  # clean up
    except ValueError:
        bot.send_message(message.chat.id, "❌ Please enter a valid number for petrol price.")
        bot.register_next_step_handler(message, calculate_cost)

bot.polling()
