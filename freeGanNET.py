from flask import Flask, render_template, request
from goPredict import get_go_predict_object

app = Flask(__name__)


def test():
    print("test")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/giver')
def giver():
    return render_template("giver.html")


@app.route('/taker')
def taker():
    return render_template("taker.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # f.save("output")
        go_predict = get_go_predict_object()
        go_predict.pass_to_predict(f)
    return render_template("giver.html")


if __name__ == "__main__":
    app.run(debug=True)
