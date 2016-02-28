from flask import Flask
app = Flask(__name__)

@app.route("/")
def setWebhook():
    return "OK, Telegram Bot!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)