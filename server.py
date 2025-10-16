from flask import Flask, request

app = Flask(__name__)

@app.route('/write', methods=['POST'])
def write():
    text = request.data.decode('utf-8')
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    return "OK", 200

@app.route('/read', methods=['GET'])
def read():
    try:
        with open('file.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "No file yet", 404

if name == '__main__':
    app.run(host='0.0.0.0', port=8080)