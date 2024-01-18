from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_text', methods=['POST'])
def receive_text():
    text = request.form['text']
    # Implement your logic to process received text here
    print(f"Received text from browser: {text}")
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
