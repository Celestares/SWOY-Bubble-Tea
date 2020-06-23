from flask import Flask, request, render_template, redirect
from Forms import *

app = Flask(__name__)


@app.route("/home", methods=['GET', 'POST'])
def home():
    test_list = [
        {"name": "Green Tea", "image": "raymond.jpg"},
        {"name": "Puck you", "image": "raymond.jpg"},
        {"name": "Green Tea", "image": "bayek.jpg"},
        {"name": "Puck you", "image": "raymond.jpg"},
        {"name": "Green Tea", "image": "bayek.jpg"},
        {"name": "Puck you", "image": "raymond.jpg"}
    ]

    form = LoginForm()
    return render_template("home.html", test_list=test_list, form=form)


@app.route("/admin")
def admin_home():
    return render_template("admin_base.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
