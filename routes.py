from app import app
from flask import render_template,request

@app.route("/")
def index():
    return render_template("start.html")

@app.route("/result", methods=["POST"])
def result():
    sukupuoli = request.form["sukupuoli"]
    return render_template("result.html", sukupuoli=sukupuoli)
