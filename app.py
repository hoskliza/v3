from flask import Flask
from flask import request
import telebot

tokenbot = "1199790744:AAHJm58PvSbg4QaKX9dN3EAQ6Z7OcHao_Lk"
bot = telebot.TeleBot(tokenbot)


app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    users = read2list('userData.log')
    data = request.get_json()
    for user in users:
        bot.send_message(int(user), rewriteJSON2(data))
    return '', 200


def read2list(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    file.close()

    return lines

# t - какое событие, x - на что изменено, у - доска, z - что изменено(заголовок/описание), а - название задачи, b - старая строка

def rewriteJSON2(dictionary):
    y = dictionary["issue"["key"]]
    x = dictionary["changelog"["items"["toString"]]]
    z = dictionary["changelog"["items"["field"]]]
    a = dictionary["issue"["components"["fields"["summary"]]]]
    b = dictionary["changelog"["items"["fromString"]]]
    event = dictionary["webhookEvent"]
    comment = dictionary["comment"["body"]]
    if z == "description":
        line = "Описание задачи " + a + " изменено: " + x + "(Доска " + y + ")"

    if event == "comment_created":
            line = "Добавлен комментарий" + comment

    if z == "summary":
        line = "Задача " + b + " переименована в " + x

    return line