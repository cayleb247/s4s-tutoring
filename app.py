from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "a507cf82d9cd01dcc897937bf985231c32eca78bd16efae7597519ddf982da57" # required for sessions

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/tutors")
def tutors():
    return render_template("tutoring.html")

@app.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")

@app.route("/signup" methods=["POST", "GET"])
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)