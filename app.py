


from flask import Flask, render_template

app = Flask(__name__)

title = "neon monkey"

@app.route('/')
def index():
  # data=await read_index()
  return render_template('index.html', title=title)

@app.route("/login")
def login():
  return render_template('login.html', title='login | '+title)
