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
    # И слать по полученному списку
    # bot.send_message()
    for user in users:
        bot.send_message(user, ':)')
    return response, 200


def read2list(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    file.close()

    return lines