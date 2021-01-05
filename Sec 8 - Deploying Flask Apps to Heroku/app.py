import os
from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient
import dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
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
