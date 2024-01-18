from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_text', methods=['POST'])
def receive_text():
    text = request.form['text']
    # Implement your logic to process received text here
    print(f"Received text from browser: {text}")
    if '*' in text.lower() or "кнопа" in text.lower():
        return jsonify({'status': True}), 200
    else:
        return jsonify({'status': False}), 200


if __name__ == '__main__':
    app.run(debug=True,port=4000,host="0.0.0.0")
