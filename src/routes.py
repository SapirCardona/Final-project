import os
import smtplib

from flask import render_template, request, make_response, before_render_template
from flask import current_app as app
from .Database import db, Users, Stores, Orders, Items


@app.route("/")
def home():
    title = "Fashi.on the way"
    return render_template("index.html", title=title)


@app.route("/login")
def login():
    title = "login"
    return render_template("Log-in.html", title=title)


@app.route("/login_customer", methods=["GET"])
def login_customer():
    title = "login customer"
    """Create a user via query string parameters."""
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    phone_number = request.form.get("phone_number")
    email = request.form.get("email")
    password = request.form.get("password")
    address = request.form.get("address")
    type = request.form.get("type")
    return render_template("Log-in_customer.html", title=title, first_name=first_name,
                           last_name=last_name, phone_number=phone_number,
                           email=email, address=address, password=password,
                           type=type)


@app.route("/store/nike")
def nike_store():
    store = Stores.query.get(1)
    return render_template("Nike_store.html", store=store)


@app.route("/store/h&m")
def hndm_store():
    store = Stores.query.get(2)
    return render_template("H&M_store.html", store=store)


@app.route("/store/noizz")
def noizz_store():
    store = Stores.query.get(3)
    return render_template("Noizz_store.html", store=store)

@app.route("/store/studio_pasha")
def studio_pasha_store():
    store = Stores.query.get(4)
    return render_template("Studio_Pasha_store.html", store=store)


@app.route("/form", methods=["POST"])
def form():
    email = request.form.get("email")

    message = "Your order has been confirmed!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("sapir.matari@gmail.com", os.environ.get("Password_google"))
    server.sendmail("sapir.matari@gmail.com", email, message)
    return render_template("index.html", email=email)


@app.route("/Cart", methods=["POST", "GET"])
def cart():
    title = "Shopping cart"
    color = request.form.get("color")
    size = request.form.get("size")
    price = request.form.get(("price"))
    if color is None:
        color = ""
    if size is None:
        size = ""
    return render_template("Cart.html", title=title, color=color, size=size, price=price)


@app.route("/User", methods=["POST"])
def user():
    title = "User's page"
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    phone_number = request.form.get("phone_number")
    address = request.form.get("address")
    password = request.form.get("password")
    type = request.form.get("type")
    if email:
        new_user = Users(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            password=password,
            address=address,
            type=type)
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return render_template("User.html", title=title, last_name=last_name, first_name=first_name,
                           address=address, phone_number=phone_number,
                           email=email, password=password, type=type)


# @app.route("/stores", methods=["GET"])
# def stores():
#     store = Stores.query.get(1)
#     render_template("stores.html", store=store)

