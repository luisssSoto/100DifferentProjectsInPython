from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os
from random import choice

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

current_path = os.path.dirname(__file__)
app = Flask(__name__, instance_path=os.path.join(current_path, 'instance'))
app.config['SECRET_KEY'] = 'MySecretKey'
API_KEY = 'MySecretKey'

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for col in self.__table__.columns:
            dictionary[col.name] = getattr(self, col.name)
        return dictionary
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# with app.app_context():
#     db.create_all()
class ForbiddenError(Exception):
    pass

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_coffe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    random_cafe = choice(result)
    return jsonify(your_cafe = random_cafe.to_dict())
    
@app.route("/all")
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    cafes_list = []
    for cafe in cafes:
        print(f"cafe: {cafe}")
        cafe_dict = cafe.to_dict()
        print(f"cafe dict: {cafe_dict}")
        cafes_list.append(cafe_dict)
    return jsonify(cafes = cafes_list)

@app.route("/search")
def get_cafe():
    query_loc = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id).where(Cafe.location==query_loc)).scalars().all()
    print(f"my cafes: {cafes}")
    if cafes:
        cafes_list = [cafe.to_dict() for cafe in cafes]
        print(f"my cafes_list: {cafes_list}")
        return jsonify(cafes = cafes_list)
    else:
        return jsonify(error = {"Not found": f"Sorry the location:{query_loc} is not available yet"}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        query_name = request.values.get("name")
        query_map_url = request.form.get("map_url")
        query_img = request.form.get("img_url")
        query_location = request.form.get("location")
        query_seats = request.form.get("seats")
        query_has_toilet = bool(request.form.get("has_toilet"))
        query_has_wifi = bool(request.form.get("has_wifi"))
        query_has_sockets = bool(request.form.get("has_sockets"))
        query_can_take_calls = bool(request.form.get("can_take_calls"))
        query_coffee_price = request.form.get("coffee_price")
        new_cafe = Cafe()
        new_cafe.name = query_name
        new_cafe.map_url = query_map_url
        new_cafe.img_url = query_img
        new_cafe.location = query_location
        new_cafe.seats = query_seats
        new_cafe.has_toilet = query_has_toilet
        new_cafe.has_wifi = query_has_wifi
        new_cafe.has_sockets = query_has_sockets
        new_cafe.can_take_calls = query_can_take_calls
        new_cafe.coffee_price = query_coffee_price
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response = {"Success": f"Your cafe: {query_name} was added into the DB"})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    if request.method == "PATCH":
        try:
            cafe = db.session.get(Cafe, cafe_id)
            query_coffee_price = request.args.get("coffee_price")
            cafe.coffee_price = query_coffee_price
            db.session.commit()
            return jsonify(response = {"Success": f"The price for the cafe with the id: {cafe_id} was updated"}), 200
        except AttributeError as ae:
            print(f"sorry error found: {ae}")
            return jsonify(error = {"The Cafe wasn't found": f"id: {cafe_id} is invalid"}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    print(f"cafe id: {cafe_id}")
    try:
        query_user_key = request.args.get("api_key")
        cafe = db.session.get(Cafe, cafe_id)
        print(cafe) 
        if query_user_key != API_KEY:
            raise ForbiddenError("You don't have access for this content")
        elif cafe is None:
            raise AttributeError
        else: 
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response = {"Success": f"We delete the cafe with id: {cafe_id}"}), 200
    except AttributeError as ae:
        print(f"Name Error: {ae}")
        return jsonify(error = {"Not Found: ": f"The cafe with id: {cafe_id} wasn't found"}), 404
    except ForbiddenError as fe:
        print(f"Name Error: {fe}")
        return jsonify(error = {"error": str(fe)}), 403
        

if __name__ == '__main__':
    app.run(debug=True)
