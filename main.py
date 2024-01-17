import speech_recognition as sr
import modules.find as find

def real_time_speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:       
        while True:
            try: 
                print("Калибровка..")
                recognizer.adjust_for_ambient_noise(source)
                print("Говорите...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language="ru-RU")
                print("Распознано:", text)
                for word in text.split(" "):
                    if find.is_obsence(word.lower()):
                        print("Маты найдены!")
            except sr.UnknownValueError:
                print("Не удалось распознать речь")
            except sr.RequestError as e:
                print(f"Ошибка сервиса распознавания речи; {e}")

if __name__ == "__main__":
    real_time_speech_recognition()
