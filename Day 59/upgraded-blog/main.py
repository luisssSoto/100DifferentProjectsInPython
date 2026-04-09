from flask import Flask, render_template
import requests


app = Flask(__name__)

# Access this bin via the API at:

# https://api.npoint.io/36432034e91b2241461f

# You can even access nested data directly, like this:

# https://api.npoint.io/36432034e91b2241461f/0/id

def get_data():
    response = requests.get('https://api.npoint.io/36432034e91b2241461f')
    response.raise_for_status()
    response = response.json()
    return response

data = get_data()

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<id>')
def post(id):
    new_data = data[int(id) - 1]
    return render_template('post.html', new_data=new_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)