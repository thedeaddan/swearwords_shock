from flask import Flask, render_template
from flask_socketio import SocketIO
import speech_recognition as sr
import threading
import io

app = Flask(__name__)
socketio = SocketIO(app)
recognizer = sr.Recognizer()

OBSERVE_TEXT_FILE = 'modules/find/some_text.txt'
LANGUAGE = "ru-RU"
PHRASE_TIME_LIMIT = 3

stop_listening_event = threading.Event()

def is_obscene(text):
    with io.open(OBSERVE_TEXT_FILE, encoding='utf-8') as file:
        for line in file:
            if any(word.lower() in line for word in text.split()):
                return True
    return False

def calibrate_microphone(source):
    recognizer.adjust_for_ambient_noise(source)

def listen_and_recognize(source):
    try:
        socketio.emit('message-from-backend', "Калибровка..")
        calibrate_microphone(source)
        
        while not stop_listening_event.is_set():
            socketio.emit('message-from-backend', "Говорите...")
            audio = recognizer.listen(source, phrase_time_limit=PHRASE_TIME_LIMIT)
            text = recognizer.recognize_google(audio, language=LANGUAGE)
            
            socketio.emit('message-from-backend', f"Распознано: {text}")
            if is_obscene(text):
                socketio.emit('obscene-detected')

    except sr.UnknownValueError:
        socketio.emit('message-from-backend', "Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")

@socketio.on('stop-listening')
def stop_listening():
    stop_listening_event.set()

@socketio.on('start-listening')
def start_listening():
    stop_listening_event.clear()

    with sr.Microphone() as source:
        thread = threading.Thread(target=listen_and_recognize, args=(source,))
        thread.start()

if __name__ == "__main__":
    socketio.run(app, debug=True, port=3333, host="0.0.0.0")
