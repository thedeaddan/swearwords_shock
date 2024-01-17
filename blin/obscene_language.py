import io

def is_obsence(word: str) :
    is_obsence_word = False
    with io.open('./blin/some_text.txt', encoding='utf-8') as file:
        for line in file:
            if word in line:
                is_obsence_word = True
    return is_obsence_word
