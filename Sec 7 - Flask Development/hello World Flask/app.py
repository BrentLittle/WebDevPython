# Flask is a micro framework
# it allows us to receive and send back data per user requests
#

# $env:FLASK_APP = "app.py"
# $env:FLASK_ENV = "development"    This restarts the server when we make a save
# flask run

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def helloWorld():
    return render_template("first_page.html")


@app.route("/second")
def helloWorldHTML():
    return render_template("second_page.html")


@app.route("/jinja")
def jinja():
    return render_template(
        "jinjaIntro.html", name="Brent Littlefield", template_name="Jinja2"
    )


@app.route("/expressions")
def expressions():

    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # Add Subtract
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # Concatenation
    first_name = "Brent"
    last_name = "Littlefield"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }

    return render_template("expressions.html", **kwargs)


class Moons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/dataStructures")
def structures():

    movies = ["Apollo 11", "Apollo 13", "Apollo 7"]

    car = {
        "brand": "Tesla",
        "model": "Model 3",
        "year": "2021",
    }

    jupiterMoons = Moons("Io", "Europa", "Ganymade", "Callisto")

    return render_template("dataStructs.html", movies=movies, car=car, moons=jupiterMoons)


@app.route("/conditions")
def statements():
    company = "Apple"
    return render_template("conditionalStatements.html", company=company)


@app.route("/loops")
def looping():
    planets = ["Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune", ]

    users = {
        "Brent": "Linux",
        "Littlefield": "MacOS",
        "Kelston": "Windows",
        "Denny": "Windows",
    }

    return render_template("loops.html", planets=planets, user_os=users)
