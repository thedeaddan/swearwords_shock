from flask import Flask, render_template, request, jsonify,redirect
from libs.find import check_text
from config import PORT,HOST
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_text', methods=['POST'])
def receive_text():
    text = request.form['text']
    print(f"Received text from browser: {text}")
    if '*' in text.lower() or check_text(text.lower()):
        return jsonify({'status': True}), 200
    else:
        return jsonify({'status': False}), 200

if __name__ == '__main__':
    
    app.run(debug=True,port=PORT,host=HOST)
