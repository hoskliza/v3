import telebot


tokenbot = "1199790744:AAHJm58PvSbg4QaKX9dN3EAQ6Z7OcHao_Lk"
bot = telebot.TeleBot(tokenbot)


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Если вы хотите подписться на уведомления - отправьте '/agree'")


@bot.message_handler(commands=['agree'])
def agree(message):
    # Вот здесь надо куда-нибудь записывать ID пользователя для рассылки
    user = message.chat.id
    file = open('userData.log', 'a+')
    data = read2list('userData.log')
    if user not in data:
        file.write(str(user) + '\n')
    bot.send_message(user, 'Подписка на уведомления оформлена')


@bot.message_handler(commands=['stop'])
def stop(message):
    user = message.chat.id
    bot.send_message(user, 'Подписка приостановлена')
    file = open('userData.log', 'a+')
    file = file.replace(user, '\n', '')
    file.close()



def read2list(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    file.close()

    return lines


if __name__ == '__main__':
    bot.polling(none_stop=True)
