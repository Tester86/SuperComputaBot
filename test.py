import telebot 

bot = telebot.TeleBot("1711714436:AAGIcTRmYJR8NhKxZJovXawhnuW9lWBRxdk")

#print(bot.get_me())

# --- structure for data ---

data = {'title': "", 'text': "", 'comments': ""}

# --- states use in conversation ---

state = None

TITLE = 1
TEXT = 2
COMMENTS = 3

@bot.message_handler(commands=['add'])
def test(message):
    global state
    global data

    data = {'title': "", 'text': "", 'comments': ""}

    bot.send_message(message.chat.id, 'add title, text, comments in separated messages\n\nnow write title')

    state = TITLE

@bot.message_handler()
def unknown(message):
    global state

    if state == TITLE:
        data['title'] = message.text
        bot.send_message(message.chat.id, f"title: {message.text}\n\nnow write text")
        state = TEXT
    elif state == TEXT:
        data['text'] = message.text
        bot.send_message(message.chat.id, f"text: {message.text}\n\nnow write comments")
        state = COMMENTS
    elif state == COMMENTS:
        data['comments'] = message.text
        bot.send_message(message.chat.id, f"comments: {message.text}")
        msg = """I got all data

title: {}
text: {}
comments: {}""".format(data['title'], data['text'], data['comments'])

        bot.send_message(message.chat.id, msg)
        state = None
    #else:
    #    print('unknown message')
    #    bot.send_message(msg.chat.id, 'unknown message')

@bot.message_handler(commands=['cancel'])
def test(message):
    global state

    bot.send_message(message.chat.id, 'canceled')

    state = None

bot.polling()