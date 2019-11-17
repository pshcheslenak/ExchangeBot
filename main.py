import telebot
from config import token
from datetime import datetime

bot = telebot.TeleBot(token)

print(bot.get_me())

def log(message, answer):
    print("\n-----------" + str(datetime.now()) + "---------------")
    print("Message from: {0} {1}, (id = {2})\n Text: {3}".format(message.from_user.first_name,
                    message.from_user.last_name,
                    str(message.from_user.id),
                    message.text))
    print("Answer:" + answer)

@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello:)")

@bot.message_handler(content_types = ["text"])
def handle_text(message):
    answer = "djgkfdhgkdhfkghfdk"
    if message.text == "a":
        answer = "b"
    elif message.text == "b":
        answer = "a"
    log(message, answer)
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True, interval = 0)
