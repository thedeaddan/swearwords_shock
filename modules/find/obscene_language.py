import io
from config import OBSERVE_TEXT_FILE


def is_obsence(text: str):
    is_obsence_word = False
    with io.open(OBSERVE_TEXT_FILE, encoding='utf-8') as file:
        for line in file:
            for word in text.split(" "):
                if word.lower() in line:
                    is_obsence_word = True
    return is_obsence_word