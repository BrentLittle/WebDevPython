from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient(
        "mongodb+srv://user:u20MTQCJ8a3c9xrY@webdevpython.bd7t5.mongodb.net/test")
    app.db = client.microblog


    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":

            entryContent = request.form.get("content")
            date = datetime.datetime.today().strftime("%y-%m-%d")
            app.db.entries.insert({"content": entryContent, "date": date})

        entrydate = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(
                    entry["date"], "%y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries=entrydate)

    return app
