from flask import Flask, render_template
import random, datetime

app = Flask(__name__)

@app.route('/')
def home():
    ran_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=ran_num, year=current_year)

if __name__ == '__main__':
    app.run(debug=True)