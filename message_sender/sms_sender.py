import requests

BOT_TOKEN = '' #enter the token here

# List of chat IDs (separate them by comma, no quotes around the whole list)
CHAT_IDS = ['chat id 1', 'chat id 2','chat id 3']  # ✅ List of string IDs

# Get message from user input
message = input("Type the message to send: ")

# Telegram API endpoint
url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

# Send the message to each chat ID
for chat_id in CHAT_IDS:
    response = requests.post(url, data={
        'chat_id': chat_id,
        'text': message
    })

    if response.status_code == 200:
        print(f"✅ Message sent to chat ID {chat_id}")
    else:
        print(f"❌ Failed to send to {chat_id}: {response.text}")
