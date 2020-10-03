import datetime
from flask import Flask, render_template, request
import database

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        body = request.form.get("body")
        print(name, body)
        if name and body:
            database.create_entry(name, body, datetime.datetime.today().strftime("%b %d, %Y"))

    return render_template("index.html", entries=database.retrieve_entries())