from flask import Flask, render_template, request, make_response, url_for
from flask import current_app as app
from werkzeug.utils import redirect

from Database import User
from __init__ import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def home():
    title = "Fashi.on the way"
    return render_template("index.html", title=title)


@app.route("/Sign")
def sign():
    title = "Sign"
    return render_template("Sign.html", title=title)


@app.route("/Business_entry")
def business_entry():
    title = "Business entry"
    return render_template("Business_entry.html", title=title)


@app.route("/POC")
def poc():
    title = "POC"
    Store_name = "Nike"
    Categories = ["Men", "Woman", "Boys", "Girls", "Baby"]
    Items = ["Shirt", "Pants"]
    Sizes = ["S", "M", "L"]
    return render_template("POC page.html", store_name=Store_name, categories=Categories, items=Items, sizes=Sizes,
                           title=title)


@app.route("/Cart", methods=["POST"])
def cart():
    title = "Shopping cart"
    color = request.form.get("color")
    size = request.form.get("size")
    return render_template("Cart.html", title=title, color=color, size=size)


@app.route("/User", methods=["POST"])
def user():
    title = "User's page"
    email = request.form.get("email")
    name = request.form.get("name")
    country = request.form.get("country")
    street_and_number = request.form.get("street_and_number")
    zip = request.form.get("zip")
    return render_template("User.html", title=title, email=email, name=name, country=country,
                           street_and_number=street_and_number, zip=zip)

if __name__ == "__main__":
    app.run()
