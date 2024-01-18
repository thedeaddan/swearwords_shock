import pymorphy2
from config import txt_file_path

def profanity_list():
    with open(txt_file_path, "r", encoding="utf-8") as file:
        return [word.strip() for word in file]

def check_text(text):
    morph = pymorphy2.MorphAnalyzer()
    found_profanities = set()

    for word in text.split():
        word = word.replace("ё","е")
        parsed_word = morph.parse(word)[0]
        normal_form = parsed_word.normal_form
        bad_words_list = profanity_list()
        if normal_form in bad_words_list or word in bad_words_list:
            found_profanities.add(normal_form)

    return found_profanities