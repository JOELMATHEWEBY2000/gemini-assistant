import json
import os
from database import collection


# Global conversation list
conversation_history = []

def load_memory(session_id):

    chats = collection.find(
        {"session_id": session_id},
        {"_id": 0}
    )

    return list(chats)


def save_message(session_id, role, text):

    collection.insert_one({
        "session_id": session_id,
        "role": role,
        "text": text
    })


def add_message(session_id, role, text):

    collection.insert_one({
        "session_id": session_id,
        "role": role,
        "text": text
    })



def get_history(session_id):

    history = ""

    chats = get_conversation(session_id)

    for chat in chats:
        history += f"{chat['role']}: {chat['text']}\n"

    return history


def get_conversation(session_id):

    chats = collection.find(
        {"session_id": session_id},
        {"_id": 0}
    )

    return list(chats)


def clear_memory(session_id):

    collection.delete_many({
        "session_id": session_id
    })


# Load previous conversation when the application starts
load_memory()