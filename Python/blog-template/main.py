from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_data = response.json()
    return render_template("index.html", blog_list=blog_data)

@app.route('/posts/<int:post_id>')
def post(post_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_data = response.json()
    for blog in blog_data:
        if blog["id"] == post_id:
            requested_blog = blog
    return render_template("post.html", blog=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
