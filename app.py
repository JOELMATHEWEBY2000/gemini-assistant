from flask import Flask, render_template, request, redirect, url_for,session

from chatbot import ask_gemini
from memory import get_conversation, clear_memory
import secrets

app = Flask(__name__)

app.secret_key = "change_this_to_a_random_secret"


@app.route("/", methods=["GET", "POST"])
def home():

    if "session_id" not in session:

        session["session_id"] = secrets.token_hex(16)

    session_id = session["session_id"]

    if request.method == "POST":

        user_message = request.form["message"]

        ask_gemini(user_message, session_id)

        return redirect(url_for("home"))

    conversation = get_conversation(session_id)

    return render_template(
        "index.html",
        conversation=conversation
    )

@app.route("/clear", methods=["POST"])
def clear_chat():

    clear_memory(session["session_id"])

    return redirect(url_for("home"))

import os

if __name__ == "__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)