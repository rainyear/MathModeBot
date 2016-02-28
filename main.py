from flask import Flask
from flask import render_template, request
import logging
import telegram

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

global bot
bot = telegram.Bot(token='205078009:AAE972IeXUB9Ay4easvMN4ABMTmfXCYf4xA')
botName = "@MathModeBot"

@app.route("/")
def setWebhook():
    return "OK, Telegram Bot!"

@app.route("/<token>", methods=["POST"])
def mathmode(token):
    print(token)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True))
        logging.info("Calling {}".format(update.message))
        haddle_message(update.message)
        return "ok"
    else:
        return "Bye~"

def handdle_message(msg):
    text = msg.text
    if "/echo" in text:
        helpInfo(msg)
    if "/greek" in text:
        helpInfo(msg)
    if "/help" in text:
        helpInfo(msg)
    else:
        helpInfo(msg)
def helpInfo(msg):
    text = ('/greek - Return LaTex Greek Letters\n'
            '/help  - Help Info')
    bot.sendMessage(chat_id=msg.chat.id, text=text)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)