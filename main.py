from flask import Flask

app = Flask(__name__)

@app.route('/')
def init():
    return 'module initialized'

if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=True)