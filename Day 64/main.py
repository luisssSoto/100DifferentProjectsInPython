from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests, os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__, instance_path=os.path.join(os.path.dirname(__file__), 'my_instance'))
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# API KEY for Movie's API
load_dotenv()
MOVIE_DB_API_KEY = os.environ.get("MOVIE_DB_API_KEY")
MOVIE_DB_SEARCH_URL = os.environ.get("MOVIE_DB_SEARCH_URL")
MOVIE_DB_GET_MOVIE_URL = os.environ.get("MOVIE_DB_GET_MOVIE_URL")
MOVIE_DB_IMG_URL = os.environ.get("MOVIE_DB_IMG_URL")


print(MOVIE_DB_API_KEY)
print(MOVIE_DB_SEARCH_URL)
print(MOVIE_DB_GET_MOVIE_URL)
print(MOVIE_DB_IMG_URL)

api_key = "92d8f4840154c48682e033161d8525d3"
token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MmQ4ZjQ4NDAxNTRjNDg2ODJlMDMzMTYxZDg1MjVkMyIsIm5iZiI6MTc4MDIyODIzOC44NTIsInN1YiI6IjZhMWMyMDhlOTVjYTExZDgwZjA4YmIyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GVfjlBXqaKtDgrEUEqL8i8OGRRIsNMTHm1i1NywQ9EU"

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
print(db)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movies-collection.db"
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False) 
    year: Mapped[int] = mapped_column(Integer, nullable=False) 
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# Adding the first movie
new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)

movies = []

@app.route("/")
def home():
    # db.create_all()        
    db.session.add(second_movie)
    db.session.commit()
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    print(f"Movies: {movies}")
    print(type(movies))
    length_movies = len(movies)
    for i in range(len(movies)):
        movies[i].ranking = length_movies - i
    return render_template("index.html", movies=movies)

class EditForm(FlaskForm):
    rating = FloatField(label='Rating from 0 to 10')
    review = StringField(label='Review why it is good or why not')
    submit = SubmitField(label='Done')

@app.route("/edit<int:id>", methods=["GET", "POST"])
def update(id):
    my_form = EditForm()
    if request.method == "POST" and my_form.validate_on_submit():
        movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie.rating = my_form.rating.data
        movie.review = my_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", my_form=my_form)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

class AddForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/add", methods=["GET", "POST"])
def add():
    my_form = AddForm()
    title = my_form.title.data
    print(f"the title of the movie: {title}")
    if my_form.validate_on_submit():
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": title})
        response.raise_for_status()
        print(response.status_code)
        print(response.text)
        print(type(response.text))
        data = response.json()
        print(f"JSON: {data}")
        print(type(data))
        movies = data["results"]
        print(f"the data: {movies}")
        for movie in movies:
            print(f"movie details: {movie["title"]}")
        return render_template("select.html", movies=movies)
    return render_template("add.html", my_form=my_form)
    
@app.route("/findMovie<int:id>")
def find_movie(id):
    id = str(id)
    movie_url = MOVIE_DB_GET_MOVIE_URL + "/" + id
    response = requests.get(url=movie_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
    response.raise_for_status()
    print(response.text)
    print(type(response.text))
    movie = response.json()
    print(type(movie))
    print(movie)
    title = movie["title"],
    img_url = movie["poster_path"]
    year = movie["release_date"][:4]
    description = movie["overview"] 
    print(f"title: {title}, img_url: {img_url}, year = {year}, description: {description}")
    new_movie = Movie(
        title = movie["title"],
        year = movie["release_date"][:4],
        description = movie["overview"],
        img_url = MOVIE_DB_IMG_URL + "/" + img_url
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for(f"update", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
