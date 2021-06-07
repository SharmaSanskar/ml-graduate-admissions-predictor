from flask import Flask, render_template, redirect, request
from pickle import load

app = Flask(__name__)

MODEL = load(open("./model/graduate_admissions_classifier.pkl", "rb"))
PREDICTION = None


def predict(gre, toefl, uni, sop, lor, cgpa, research):
    return MODEL.predict([[gre, toefl, uni, sop, lor, cgpa, research]])[0]


@app.route("/", methods=["POST", "GET"])
def index():
    global PREDICTION
    if request.method == "POST":
        gre = int(request.form["gre"])
        toefl = int(request.form["toefl"])
        uni = int(request.form["uni"])
        sop = int(request.form["sop"])
        lor = int(request.form["lor"])
        cgpa = float(request.form["cgpa"])
        research = int(request.form["research"])

        PREDICTION = predict(gre, toefl, uni, sop, lor, cgpa, research)
        return redirect("/")
    else:
        return render_template("index.html", prediction=PREDICTION)


if __name__ == "__main__":
    app.run()
