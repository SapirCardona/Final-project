from flask import render_template, request, make_response, before_render_template
from flask import current_app as app
from .Database import db, Users, Stores, Orders, Items


@app.route("/")
def home():
    title = "Fashi.on the way"
    # users = Users.query.all()
    # stores = Stores.query.all()
    # orders = Orders.query.all()
    # items = Items.query.all()
    # print(users)
    # print(stores)
    # print(orders)
    # print(items)
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


# @app.route("/Business_entry")
# def business_entry():
#     title = "Business entry"
#     return render_template("Business_entry.html", title=title)


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


def user_login():
    """Create a user via query string parameters."""
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    phone_number = request.args.get('phone_number')
    address = request.args.get('address')
    type = request.args.get('type')
    email = request.args.get('email')
    if email:
        existing_user = Users.query.filter(
            Users.email == email
        ).first()
        if existing_user:
            return make_response(
                f'Sorry! ({email}) already exist in our system!'
            )
        else:
            new_user = Users(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                address=address,
                type=type,
                email=email,
            )  # Create an instance of the Users class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
