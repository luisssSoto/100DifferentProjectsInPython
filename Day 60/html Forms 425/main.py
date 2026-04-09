from flask import Flask, render_template, request
import requests, os, smtplib
from dotenv import load_dotenv

load_dotenv()
my_npoint = os.getenv("NPOINT")
posts = requests.get(my_npoint).json()

from_email = os.getenv("FROM_EMAIL")
my_password = os.getenv("FROM_PASSWORD")
owner_email = os.getenv("OWNER_EMAIL")
     
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_fun():
    if request.method == "GET":
        return render_template('contact.html')
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                print(f"email: {from_email}, password: {my_password}")
                connection.starttls()
                connection.login(user=from_email, password=my_password)
                connection.sendmail(from_addr=from_email, to_addrs=owner_email, msg=f"Subject:Customer Service\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
                msg = "Successfully sent a message"
        except Exception as e:
            print(e)
            msg = f"Something Failed: {e}"
        return render_template('contact.html', msg=msg)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
