import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


@app.route("/")
def my_world():
    return render_template('index.html')

@app.route("/about.html")
def show_about():
    return render_template('about.html')

@app.route("/contact.html")
def show_contacts():
    return render_template('contact.html')

@app.route("/works.html")
def show_works():
    return render_template('works.html')



