from google import genai

from config import GEMINI_API_KEY
from memory import load_memory, save_message, get_history

from bitcoin import get_bitcoin_price
from weather import get_weather

client = genai.Client(api_key=GEMINI_API_KEY)

history = load_memory() or []


def build_conversation(session_id):

    history = load_memory(session_id)

    conversation = ""

    for item in history:

        conversation += f"{item['role']}: {item['text']}\n"

    return conversation


def ask_gemini(user_message,session_id):

    global history

    conversation = get_history(session_id)

    conversation += f"User: {user_message}"

    try:

        message = user_message.lower()

        # Bitcoin
        if "bitcoin" in message or "btc" in message:

            answer = get_bitcoin_price()

        # Weather
        elif "weather" in message:

            city = message.replace("weather", "").replace("in", "").strip()

            if city == "":
                city = "Mumbai"

            answer = get_weather(city)

        # Gemini
        else:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=conversation
            )

            answer = response.text

            if not answer:
                answer = "Sorry, I couldn't generate a response."

    except Exception as e:

        answer = f"Error: {e}"

    history.append({
        "role": "User",
        "text": user_message
    })

    history.append({
        "role": "Assistant",
        "text": answer
    })

    save_message(history)

    return answer


def clear_history():

    global history

    history = []

    save_message(history)