from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    gender_response.raise_for_status()
    gender = gender_response.json()["gender"]

    age_response = requests.get(f'https://api.agify.io?name={name}')
    age_response.raise_for_status()
    age = age_response.json()["age"]

    return render_template('/index.html', name=name, gender=gender, age=age)



if __name__ == '__main__':
    app.run(debug=True)