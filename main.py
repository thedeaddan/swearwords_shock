import speech_recognition as sr

def find_keyword(text):
    if "Человек" in text and "Жук" in text:
        print("Я нашел!")

def real_time_speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")

        try:
            while True:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)
                
                # Используем локальный движок PocketSphinx
                text = recognizer.recognize_sphinx(audio, language="ru-RU")
                
                print("Распознано:", text)
                find_keyword(text)
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания речи; {e}")

if __name__ == "__main__":
    real_time_speech_recognition()
