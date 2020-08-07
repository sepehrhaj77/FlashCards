from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main", methods = ["POST"])
def main():
    number = request.form.get("number")
    prev = request.form.get("previous")
    print(type(prev))
    print(type(number))

    attempts = 0
    rando = random.randint(1,12) 

    if prev: 
        while int(rando) == int(prev):
            rando = random.randint(1,int(number))
    answer = int(number) * rando

    return render_template("main.html", number=number, rando=rando, answer=answer)


if __name__ == "__main__":
    app.run(debug=True)