from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
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
    Items=["Shirt", "Pants"]
    Sizes=["S", "M", "L"]
    return render_template("POC page.html", store_name=Store_name, categories=Categories, items=Items, sizes=Sizes, title=title)

@app.route("/Cart", methods=["POST"])
def cart():
    title = "Shopping cart"
    test = request.form.get("test")
    color = request.form.get("color")
    size = request.form.get("size")
    return render_template("Cart.html", title=title, test=test, color=color, size=size)

if __name__ == "__main__":
    app.run()
