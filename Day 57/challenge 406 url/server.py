from flask import Flask, render_template
import random, datetime, requests

app = Flask(__name__)

@app.route('/')
def home():
    ran_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=ran_num, year=current_year)

@app.route('/fake/<num>')
def get_fake(num):
    response = requests.get(' https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    fake_news = response.json()
    print(f"fake_news: {fake_news}")
    print(num)
    return render_template('fakes.html', fake_news=fake_news)

if __name__ == '__main__':
    app.run(debug=True)