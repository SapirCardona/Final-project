from flask import render_template, request
from flask import current_app as app
from .Database import db, Users, Stores, Orders, Items


@app.route("/")
def home():
    title = "Fashi.on the way"
    users = Users.query.all()
    stores = Stores.query.all()
    orders = Orders.query.all()
    items = Items.query.all()
    print(users)
    print(stores)
    print(orders)
    print(items)
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


@app.route("/Cart", methods=["POST", "GET"])
def cart():
    title = "Shopping cart"
    color = request.form.get("color")
    size = request.form.get("size")
    if color is None:
        color = ""
    if size is None:
        size = ""
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

