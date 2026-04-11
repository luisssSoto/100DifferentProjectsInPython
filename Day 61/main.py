from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

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
bootstrap = Bootstrap5(app)

app.secret_key = "my secret key"

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log in')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    my_form = MyForm()
    render_page = "login.html"
    if my_form.validate_on_submit():
        print(my_form.email.data)
        entry_email = my_form.email.data
        entry_password = my_form.password.data
        if entry_email == "admin@email.com" and entry_password == "12345678":
            render_page = "success.html"
        else:
            render_page = "denied.html"
    return render_template(render_page, my_form=my_form)

if __name__ == '__main__':
    app.run(debug=True)
