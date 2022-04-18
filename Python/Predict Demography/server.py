from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello!!"


@app.route("/guess/<name>")
def guess(name):
    params = {
        "name": name
    }
    response = requests.get("https://api.nationalize.io/", params=params)
    nationality = response.json()["country"][0]["country_id"]
    response = requests.get("https://api.genderize.io/", params=params)
    gender = response.json()["gender"]
    response = requests.get("https://api.agify.io/", params=params)
    age = response.json()["age"]
    return render_template("guess.html", nationality=nationality, gender=gender, age=age,name=name)
