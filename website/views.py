from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route("/")
def home():
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/donate")
def donate():
    return render_template("donate.html")

@views.route("/tutors")
def tutors():
    return render_template("tutors.html")

@views.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")