from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from dotenv import load_dotenv

load_dotenv()
current_path = os.path.dirname(__file__)
app = Flask(__name__, instance_path=os.path.join(current_path, 'instance'))
SECRET_KEY = os.getenv("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

# SET UP THE LOGIN SESSIONS
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# with app.app_context():
#     db.create_all()

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        user_email = request.form['email']
        user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()
        if user:
            flash("You've already registered with that email, instead log in")
            return redirect(url_for('login'))
        else:
            plain_pwd = request.form['password']
            hash_salted_pwd = generate_password_hash(password=plain_pwd, method='pbkdf2:sha256', salt_length=8)
            user = User(
                name = request.form.get('name'),
                email = request.form.get('email'),
                password = hash_salted_pwd
            )
            db.session.add(user)
            db.session.commit()
            # Login and authenticate user after adding details to the db
            login_user(user)
            return redirect(url_for('login'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        pswd = request.form.get('password')
        user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()
        print(user)
        if user is None:
            flash("The email doesn't exist, please try again.")
            return render_template("login.html")
        elif check_password_hash(pwhash=user.password, password=pswd):
            login_user(user)
            return redirect(url_for('secrets', user_name=user.name, logged_in=current_user.is_authenticated))
        else:
            flash("Password incorrect. Please try again.")
            return render_template("login.html")
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    user_name = request.args.get("user_name")
    return render_template("secrets.html", user_name=user_name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    directory = 'static'
    path = 'files/cheat_sheet.pdf'
    return send_from_directory(directory=directory, path=path)


if __name__ == "__main__":
    app.run(debug=True)
