from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return f"""
    <div id='home-page'></div>
  """

@app.route('/about')
def about():
  return f"""
    <div id='about-page'></div>
  """
