from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/goals")
def goals():
    return render_template("goals.html")

if __name__=="__main__":
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)