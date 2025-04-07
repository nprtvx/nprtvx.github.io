from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return '<h2>ello world</h2>'

if __name__ == '__main__':
    freezer.freeze()
