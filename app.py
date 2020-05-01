from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main", methods = ["POST"])
def main():
    number = request.form.get("number")
    rando = random.randint(1,int(number))
    return render_template("main.html", number=number, rando=rando)

if __name__ == "__main__":
    app.run(debug=True)