from flask import Flask, render_template, request
from goPredict import get_go_predict_object

app = Flask(__name__)
l =666655
global data

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/giver')
def giver():
    return render_template("giver.html")


@app.route('/taker')
def taker():
    return render_template("taker.html")


# @app.route('/handle_data', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save("output.jpg")
#         go_predict = get_go_predict_object()
#         go_predict.pass_to_predict()
#     return render_template("giver.html")
#

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        adress = request.form['fname']
        list_of_products = request.form['lname']
        f = request.files['file']
        f.save("output.jpg")
        go_predict = get_go_predict_object()
        go_predict.pass_to_predict()
        go_predict.add_adress_and_products(adress, list_of_products)
        go_predict.save_to_database()
        go_predict.adress=None
        go_predict.list_of_products=[]
    return render_template("giver.html")

@app.route('/taker')
def post():
    go_predict = get_go_predict_object()
    data123 = go_predict.check_available_dishes()
    pass_data1 = data123[0]
    pass_data2 = data123[1]
    print(data123)
    l = ["Spaghetti", "Pizza"]
    return render_template("post.html", data=l, data1=l)

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#
#             go_predict = get_go_predict_object()
#         # f.save("output.jpg")
#
#
#         go_predict.pass_to_predict()
#     return render_template("giver.html")
if __name__ == "__main__":
    app.run(debug=True)
