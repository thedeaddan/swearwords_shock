import speech_recognition as sr
import pyaudio

def find_keyword(text):
    if "Человек" in text and "Жук" in text:
        print("Я нашел!")

def real_time_speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")

        # Задаем параметры аудиопотока
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)

        try:
            while True:
                audio_chunk = stream.read(1024)
                audio_data = recognizer.listen(audio_chunk)
                text = recognizer.recognize_google(audio_data, language="ru-RU", show_all=False)
                find_keyword(text)
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания речи: {e}")
        finally:
            stream.stop_stream()
            stream.close()

if __name__ == "__main__":
    p = pyaudio.PyAudio()
    real_time_speech_recognition()
    p.terminate()
