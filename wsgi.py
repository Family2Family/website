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
    return render_template("about_es.html")


@app.route("/timeline")
def timeline():
    return render_template("timeline.html")
@app.route("/timeline/es")
def timeline_es():
    return render_template("timeline_es.html")


@app.route("/donate")
def about():
    return render_template("donate.html")
@app.route("/donate/es")
def about_es():
    return render_template("donate_es.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/contact/es")
def contact_es():
    return render_template("contact_es.html")

@app.route("/vision")
def donate():
    return render_template("vision.html")
@app.route("/vision/es")
def donate_es():
    return render_template("vision_es.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
