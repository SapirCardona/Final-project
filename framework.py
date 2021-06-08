from flask import Flask, render_template

app = Flask(__name__)


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
    return render_template("Cart.html", title=title, color=color, size=size)

if __name__ == "__main__":
    app.run()
