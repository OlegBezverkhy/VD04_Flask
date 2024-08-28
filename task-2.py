from flask import Flask, render_template
from datetime import datetime as dt
import blogs_text as bt

app = Flask(__name__)

@app.route("/")
def main_screen():
    return render_template("index.html")

@app.route("/blog1/")
def blog1():
    context = {'b_text': bt.blogs['blog1'],
               'b_title': bt.title['blog1'],
               'b_date': bt.blog_date['blog1'],
               'b_author': bt.author['blog1'],
               'b_href': bt.href['blog1']}
    return render_template("blog.html", context=context)

@app.route("/blog2/")
def blog2():
    context = {'b_text': bt.blogs['blog2'],
               'b_title': bt.title['blog2'],
               'b_date': bt.blog_date['blog2'],
               'b_author': bt.author['blog2'],
               'b_href': bt.href['blog2']}
    return render_template("blog.html", context=context)

@app.route("/blog3/")
def blog3():
    context = {'b_text': bt.blogs['blog2'],
              'b_title': bt.title['blog2'],
              'b_date': bt.blog_date['blog2'],
              'b_author': bt.author['blog2'],
              'b_href': bt.href['blog2']}
    return render_template("blog.html", context=context)

@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contacts/")
def contacts():
    current_time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("contacts.html", current_time=current_time)


if __name__ == "__main__":
    app.run()