from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/experience")
def experience():
    return render_template("experiance.html")


@app.route("/projects")
def projects():
    return render_template("project.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/contact")
def contact():
    return render_template("contract.html")


if __name__ == "__main__":
    app.run(debug=True)
