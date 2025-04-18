import sys
from flask import Flask, render_template
from flask_frozen import Freezer
import auth

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'
app.register_blueprint(auth.bp)

@app.route('/')
def index():
    return render_template('index.html')

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
