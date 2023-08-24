import telebot

bot = telebot.TeleBot("6632027875:AAGbVLzklv6zs9nu2HdIn411hy2YmbNoLjQ")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome to my bot!")

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()