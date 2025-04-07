from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'

@app.route('/')
def index():
    return '<h2>ello world</h2>'

@app.route('/about')
def about():
    return 'About Page'

freezer = Freezer(app)

@freezer.register_generator
def url_generator():
    yield '/'
    yield '/about'

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
        freezer.freeze()
    else:
        app.run(debug=True)
