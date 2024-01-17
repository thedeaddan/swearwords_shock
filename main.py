from flask import Flask, render_template
from flask_socketio import SocketIO
import speech_recognition as sr
import threading
import time
import modules.find as find

app = Flask(__name__)
socketio = SocketIO(app)
recognizer = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start-listening')
def start_listening():
    def background_thread():
        with sr.Microphone() as source:
            try:
                print("Калибровка..")
                recognizer.adjust_for_ambient_noise(source)
                print("Говорите...")
                while True:
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio, language="ru-RU")
                    print("Распознано:", text)
                    if find.is_obscene(text):
                        socketio.emit('obscene-detected')
            except sr.UnknownValueError:
                print("Не удалось распознать речь")
            except sr.RequestError as e:
                print(f"Ошибка сервиса распознавания речи; {e}")

    thread = threading.Thread(target=background_thread)
    thread.start()

if __name__ == "__main__":
    socketio.run(app, debug=True,port=123,host="0.0.0.0")
