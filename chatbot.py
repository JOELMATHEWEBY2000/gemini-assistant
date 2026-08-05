from google import genai

from config import GEMINI_API_KEY
from memory import save_message, get_history, clear_memory

from bitcoin import get_bitcoin_price
from weather import get_weather

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(user_message, session_id):
    """
    Generate a response using Gemini or external APIs.
    """

    conversation = get_history(session_id)
    conversation += f"User: {user_message}\n"

    try:

        message = user_message.lower()

        # Bitcoin
        if "bitcoin" in message or "btc" in message:

            answer = get_bitcoin_price()

        # Weather
        elif "weather" in message:

            city = (
                message.replace("weather", "")
                       .replace("in", "")
                       .strip()
            )

            if not city:
                city = "Mumbai"

            answer = get_weather(city)

        # Gemini
        else:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=conversation
            )

            answer = response.text or "Sorry, I couldn't generate a response."

    except Exception as e:

        answer = f"Error: {e}"

    # Save messages to MongoDB
    save_message(session_id, "User", user_message)
    save_message(session_id, "Assistant", answer)

    return answer


def clear_chat(session_id):
    """
    Delete all chat messages for the current session.
    """
    clear_memory(session_id)