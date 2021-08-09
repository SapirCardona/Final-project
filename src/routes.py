import os
import smtplib

from flask import render_template, request
from flask import current_app as app
from .Database import db, Users, Stores


@app.route("/")
def home():
    title = "Fashi.on the way"
    Nike_store = Stores.query.get(1)
    HndM_store = Stores.query.get(2)
    Noizz_store = Stores.query.get(3)
    Studio_Pasha_store = Stores.query.get(4)
    return render_template("Index.html", title=title, Nike_store=Nike_store,
                           HndM_store=HndM_store, Noizz_store=Noizz_store,
                           Studio_Pasha_store=Studio_Pasha_store)


@app.route("/login")
def login():
    title = "login"
    return render_template("Log-in.html", title=title)


@app.route("/sign_up", methods=["GET"])
def sign_up():
    title = "Sign up"
    """Create a user via query string parameters."""
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    phone_number = request.form.get("phone_number")
    email = request.form.get("email")
    password = request.form.get("password")
    address = request.form.get("address")
    type = request.form.get("type")
    return render_template("Sign_up.html", title=title, first_name=first_name,
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
    if email:
        message = """Subject: Subject of mail!\n

                content of mail."""

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("fashi.on.the.way.mail@gmail.com", os.environ.get("Password_google"))
        server.sendmail("fashi.on.the.way.mail@gmail.com", email, message)
        return render_template("Cart.html", email=email)
    else:
        return render_template("Cart.html")


@app.route("/cart", methods=["POST", "GET"])
def cart():
    title = "Shopping cart"
    color = request.form.get("color")
    size = request.form.get("size")
    price = request.form.get("price")
    if color is None:
        color = ""
    if size is None:
        size = ""
    if price is None:
        price = ""
    return render_template("Cart.html", title=title, color=color, size=size, price=price)


@app.route("/user", methods=["POST"])
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