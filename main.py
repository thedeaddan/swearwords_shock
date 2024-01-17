from flask import Flask, render_template
from flask_socketio import SocketIO
import speech_recognition as sr
import threading
import time
import io

def is_obsence(text: str):
    is_obsence_word = False
    with io.open('modules/find/some_text.txt', encoding='utf-8') as file:
        for line in file:
            for word in text.split(" "):
                if word.lower() in line:
                    is_obsence_word = True
    return is_obsence_word

app = Flask(__name__)
socketio = SocketIO(app)
recognizer = sr.Recognizer()
stop_listening_flag = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('stop-listening')
def stop_listening():
    global stop_listening_flag
    stop_listening_flag = True

@socketio.on('start-listening')
def start_listening():
    global stop_listening_flag
    stop_listening_flag = False

    def background_thread():
        global stop_listening_flag
        with sr.Microphone() as source:
            while not stop_listening_flag:
                print(stop_listening_flag)
                try:
                    socketio.emit('message-from-backend', "Калибровка..")
                    recognizer.adjust_for_ambient_noise(source)
                    socketio.emit('message-from-backend',"Говорите...")
                    audio = recognizer.listen(source,phrase_time_limit=3)
                    text = recognizer.recognize_google(audio, language="ru-RU")
                    socketio.emit('message-from-backend',f"Распознано:{text}")
                    if is_obsence(text):
                        socketio.emit('obscene-detected')
                except sr.UnknownValueError:
                    socketio.emit('message-from-backend',"Не удалось распознать речь")
                except sr.RequestError as e:
                    print(f"Ошибка сервиса распознавания речи; {e}")


    thread = threading.Thread(target=background_thread)
    thread.start()

if __name__ == "__main__":
    socketio.run(app, debug=True, port=3333, host="0.0.0.0")
