from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message")
    
    response = requests.post(
        RASA_URL,
        json={"sender": "user", "message": user_message}
    )

    bot_response = response.json()
    return jsonify(bot_response)

if __name__ == "__main__":
    app.run(debug=True)