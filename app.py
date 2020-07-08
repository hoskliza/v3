from flask import Flask
from flask import request
import json
from .bot import bot


app = Flask(__name__)


@app.route('/webhook')
def webhook():
    users = read2list('userData.log')
    # Вот тут надо доставать откуда-то ID для рассылки
    data = request.get_json()
    response = json.dumps(data, indent=2)
    data = json.load(data)
    # И слать по полученному списку
    # bot.send_message()
    for user in users:
        bot.send_message(user, rewriteJSON(data))
    return response, 200


def read2list(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    file.close()

    return lines

# x - на что изменено, у - доска, z - что изменено(заголовок/описание), а - название задачи, b - старая строка
def rewriteJSON(dictionary):
    x = dictionary["toString"]
    y = dictionary["key"]
    z = dictionary["field"]
    a = dictionary["summary"]
    b = dictionary["fromString"]
    if z == "description":
        line = "Описание задачи " + a + " изменено: " + x + "(Доска " + y + ")"

    else:
        line = "Задача " + b + " переименована в " + x

    return line