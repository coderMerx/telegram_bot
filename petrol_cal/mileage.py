import telebot

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! Send me your data like this:\n\n/mileage km=120 price=105 petrol=2")

@bot.message_handler(commands=['mileage'])
def mileage(message):
    try:
        text = message.text.replace('/mileage', '').strip()
        data = dict(item.split('=') for item in text.split())

        km = float(data['km'])
        price = float(data['price'])
        petrol = float(data['petrol'])

        mileage = km / petrol
        total_cost = petrol * price

        reply = (
            f"🛵 Ride Summary:\n"
            f"Distance: {km} km\n"
            f"Petrol Used: {petrol} L\n"
            f"Petrol Price: ₹{price}/L\n\n"
            f"📊 Mileage: {mileage:.2f} km/L\n"
            f"💸 Cost: ₹{total_cost:.2f}"
        )
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "❌ Invalid input. Please use this format:\n/mileage km=120 price=105 petrol=2")

bot.polling()
