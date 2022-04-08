from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/giver')
def giver():
    return render_template("giver.html")

@app.route('/taker')
def taker():
    return render_template("takerhtml")


if __name__ == "__main__":
    app.run(debug=True)
