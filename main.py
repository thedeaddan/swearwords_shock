import speech_recognition as sr

def find_keyword(text):
    if "Человек" in text and "Жук" in text:
        print("Я нашел!")

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            while True:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language="ru-RU")
                print("Распознано:", text)
                find_keyword(text)
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания речи; {e}")

if __name__ == "__main__":
    main()
