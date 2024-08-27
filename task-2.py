from flask import Flask, render_template
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def main_screen():
    return render_template("index.html")

@app.route("/blog1/")
def blog1():
    return render_template("blog1.html")

@app.route("/blog2/")
def blog2():
    return render_template("blog2.html")

@app.route("/blog3/")
def blog3():
    return render_template("blog3.html")

@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contacts/")
def contacts():
    current_time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("contacts.html", current_time=current_time)


if __name__ == "__main__":
    app.run()