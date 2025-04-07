from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>ello world</h2>'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
