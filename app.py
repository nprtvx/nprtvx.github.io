


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

async def read_index():
    with open("index.html", "r") as file:
        filist = file.readlines()
        file.close()
    return filist

filist = await read_index()

