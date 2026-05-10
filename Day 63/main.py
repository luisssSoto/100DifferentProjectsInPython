from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from werkzeug.exceptions import NotFound
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

all_books = []

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
print(db)

app = Flask(__name__, instance_path=os.path.join(os.path.dirname(__file__), 'my_instance'))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)
print(app.instance_path)

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


@app.route('/', methods=["GET", "POST"])
def home():
    with app.app_context():
        # The above command don't forget to run it the first time
        # db.create_all()
        result = db.session.execute(db.select(Books).order_by(Books.title))
        all_books = result.scalars().all()
    if all_books != 0:
        return render_template('index.html', books = all_books, length = len(all_books))
    else:
        return render_template('index.html', title="The Library is empty", length = len(all_books))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    elif request.method == "POST":
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        book_rating = request.form['book_rating']
        with app.app_context():
            new_book = Books(
                title = book_name
            )
            new_book.author = book_author
            new_book.rating = book_rating
            db.session.add(new_book)
            db.session.commit()
        all_books.append(new_book)
        return redirect(url_for('home'))

@app.route("/edit/id=<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        with app.app_context():
            book = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
            print(book.title)
        return render_template('edit.html', book = book)
    else:
        with app.app_context():
            book = db.get_or_404(Books, id)
            book.rating = request.form["new_rating"]
            db.session.commit()
        return redirect(url_for('home'))

@app.route('/delete/id=<id>')
def delete(id):
    with app.app_context():
        book = db.get_or_404(Books, id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)

