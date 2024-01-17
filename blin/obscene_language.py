import io

def is_obsence(word: str) :
    is_obsence_word = False
    with io.open('./some_text.txt', encoding='utf-8') as file:
        for line in file:
            if word in line:
                is_obsence_word = True
    if is_obsence_word == True:
        return True
    else:
        return False
 
            
if __name__ == '__main__':
    print(is_obsence("матюшок"))