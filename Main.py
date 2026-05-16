import os
import telebot
import anthropic

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_KEY'])

SYSTEM = """Tu Panda hai - ek funny masti wala desi best friend AI! Tu Hinglish mein baat karta hai. Bhai yaar bro use karta hai. Emoji use karta hai. Short punchy replies deta hai."""

@bot.message_handler(func=lambda m: True)
def reply(message):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        system=SYSTEM,
        messages=[{"role": "user", "content": message.text}]
    )
    bot.reply_to(message, response.content[0].text)

bot.polling()
