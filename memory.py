from database import collection


def load_memory(session_id):
    """
    Load all chat messages for a session.
    """
    chats = collection.find(
        {"session_id": session_id},
        {"_id": 0}
    )

    return list(chats)


def save_message(session_id, role, text):
    """
    Save one chat message.
    """
    collection.insert_one({
        "session_id": session_id,
        "role": role,
        "text": text
    })


def get_history(session_id):
    """
    Return conversation as a single string for Gemini.
    """
    chats = load_memory(session_id)

    history = ""

    for chat in chats:
        history += f"{chat['role']}: {chat['text']}\n"

    return history


def get_conversation(session_id):
    """
    Return conversation list for Flask templates.
    """
    return load_memory(session_id)


def clear_memory(session_id):
    """
    Delete all messages for a session.
    """
    collection.delete_many({
        "session_id": session_id
    })