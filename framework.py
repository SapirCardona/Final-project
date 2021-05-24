from flask import Flask, render_template
from Sapir.Finalproject import POC
app = Flask(__name__)


@app.route("/")
def home():
    title = "Fashi.on the way"
    return render_template("index.html", title=title)

@app.route("/Sign")
def sign():
    return render_template("Sign.html")

@app.route("/Business_entry")
def business_entry():
    return render_template("Business_entry.html")

@app.route("/Shopping_bag")
def shopping_bag():
    return render_template("Shopping_bag.html")

@app.route("/POC")
def poc():
    Store_name = "Nike"
    Categories = ["Men", "Woman", "Boys", "Girls", "Baby"]
    Items=["Shirt", "Pants"]
    Sizes=["S", "M", "L"]
    return render_template("POC page.html", store_name=Store_name, categories=Categories, items=Items, sizes=Sizes)


@app.route("/add_to_shopping_bag")
def add_to_shopping_bag():



if __name__ == "__main__":
    app.run()
