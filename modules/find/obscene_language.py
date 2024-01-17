import io

def is_obsence(text: str) :
    is_obsence_word = False
    with io.open('modules/find/some_text.txt', encoding='utf-8') as file:
        for line in file:
            for word in text.split(" "):
                if word.lower() in line:
                    is_obsence_word = True
    return is_obsence_word
