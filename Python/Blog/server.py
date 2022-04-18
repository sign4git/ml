from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_data = response.json()
    return render_template(template_name_or_list="blog.html", blog_list=blog_data)
