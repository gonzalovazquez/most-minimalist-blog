import datetime
from flask import Flask, render_template, request
import database


app = Flask(__name__)

database.create_tables()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        database.create_entry(entry_content, datetime.datetime.today().strftime("%b %d"))

    return render_template("index.html", entries=database.retrieve_entries())