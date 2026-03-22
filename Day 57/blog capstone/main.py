from flask import Flask, render_template
from post import Post
import requests

response = requests.get(' https://api.npoint.io/c790b4d5cab58020d391')
response.raise_for_status()
fake_news = response.json()
posts = []

for new in fake_news:
    post = Post(new['id'], new['title'], new['subtitle'], new['body'])
    posts.append(post)


app = Flask(__name__)

@app.route('/blog')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:fake_id>')
def get_post(fake_id):
    chosen_post = posts[fake_id - 1]
    return render_template("post.html", chosen_post=chosen_post, id=fake_id)

if __name__ == "__main__":
    app.run(debug=True)
