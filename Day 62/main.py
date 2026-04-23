from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    p = '🔌'
    wrong = '❌'
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[URL()])
    opening = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing = StringField('Closing Time e.g. 5PM', validators=[DataRequired()])
    coffe_rating = SelectField('Coffe rating', validators=[DataRequired()], choices=[('☕'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')])
    wifi_rating = SelectField('Wifi Strength Rating', validators=[DataRequired()], choices=[(wrong), ('💪'), ('💪' * 2), ('💪' * 3), ('💪' * 4), ('💪' * 5)])
    power = SelectField('Power Socket Availability', validators=[DataRequired()], choices=[(wrong), (p), (p * 2), (p * 3), (p * 4), (p * 5)])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

import os
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    render_page = "add.html"
    if request.method == "POST":
        if form.validate_on_submit():
            render_page = "cafes.html"
            try:
                with open(".\\Day 62\\cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
                    cafe = form.cafe.data + ","
                    location = form.location.data + ","
                    opening = form.opening.data + ","
                    closing = request.form["closing"] + ","
                    coffe_rating = request.form["coffe_rating"] + ","
                    wifi_rating = request.form["wifi_rating"] + ","
                    power = request.form["power"]
                    cafe_row = cafe + location + opening + closing + coffe_rating + wifi_rating + power
                    csv_file.write(f"\n{cafe_row}")
                    return redirect(url_for('cafes'))
            except Exception as e:
                print(f"It has ocurred an error: {e}")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    print(request.method)
    return render_template(render_page, form=form)


@app.route('/cafes')
def cafes():
    print("request method")
    print(request.method)
    with open('./Day 62/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
