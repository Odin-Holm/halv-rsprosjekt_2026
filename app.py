from flask import Flask, render_template
from db import disorders, passives
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/disorders')
def disorder_list():
    data = disorders()
    return render_template("disorders.html", disorders = data)

@app.route('/passives')
def passivelist():
    data2 = passives()
    return render_template("passives.html", passives = data2)
if __name__ == '__main__':
    app.run(debug=True)

 