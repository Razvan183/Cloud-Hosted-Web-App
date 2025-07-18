from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my web app!"

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)