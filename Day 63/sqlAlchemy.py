"""SQLAlchemy"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
print(db)

app = Flask(__name__, instance_path=os.path.join(os.path.dirname(__file__), 'my_instance'))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)
print(app.instance_path)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
  db.create_all()

# CRUD Operations:
# Create
# with app.app_context():
#   book1 = Books(title="Harry Potter", author="J.K. Rowling", rating=9.3)
#   db.session.add(book1)
#   db.session.commit()

# Read
with app.app_context():
   result = db.session.execute(db.select(Books).order_by(Books.title))
   print(result)
  #  for row in result:
  #     print(f"row: {row}")
   all_books = result.scalars()
   print(all_books)
   for item in all_books:
      print(item.title)
      print(item.id)

# Read a particular element (scalar instead scalars)
# with app.app_context():
#    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potterson")).scalar()
#    print(book.author)

# # Update
# with app.app_context():
#    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potterson")).scalar()
#    book.title = "Harry Potterson"
#    db.session.commit()

# with app.app_context():
#    book = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
#    print(book.title)

# # Updata a Record by Primary Key
# with app.app_context():
#    book = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
#    book.title = "Harry The Lucky Magician"
#    book.author = "Alex Soto"
#    db.session.commit()

# with app.app_context():
#    book = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
#    print(book.title)

# Deleete a Particular Record By Primary Key
# with app.app_context():
#    book = db.session.execute(db.select(Books).where(Books.id == 1)).scalar()
#    db.session.delete(book)
#    db.session.commit()

# get_or_404()
with app.app_context():
   book = db.get_or_404(Books, 1)
   print(f"book: {book.title}")