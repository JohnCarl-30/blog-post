from flask import Flask, render_template
from post import Post
import requests

post = requests.get("https://api.npoint.io/dab69ed9f515d4dcf336").json()
post_objects = []
for p in post:
    post_objects.append(Post(p["id"], p["title"], p["subtitle"], p["body"]))
    

app = Flask(__name__)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


if __name__ == "__main__":
    app.run
