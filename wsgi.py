# Web Sever Gateway Interface Python file

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/about")
def index():
    return render_template("about.html")

@app.route("/es")
@app.route("/about/es")
def index_es():
    return render_template("about.html")


@app.route("/timeline")
def timeline():
    return render_template("timeline.html")


@app.route("/donate")
def about():
    return render_template("donate.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/vision")
def donate():
    return render_template("vision.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
