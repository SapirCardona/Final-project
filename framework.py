from flask import Flask, render_template


app = Flask(__name__)




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Sign")
def sign():
    return render_template("Sign.html")

@app.route("/Business_entry")
def business_entry():
    return render_template("Business_entry.html")

@app.route("/Shopping_bag")
def shopping_bag():
    return render_template("Shopping_bag.html")

if __name__ == "__main__":
    app.run()