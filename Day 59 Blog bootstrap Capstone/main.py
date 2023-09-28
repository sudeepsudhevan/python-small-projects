from flask import Flask, render_template

import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
posts = response.json()
print(posts)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_post=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
