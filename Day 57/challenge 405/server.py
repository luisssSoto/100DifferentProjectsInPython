from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/fake')
def fake():
    response = requests.get(' https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    fake_news = response.json()
    print(f"fake_news: {fake_news}")
    return render_template('index.html', fake_news=fake_news)


if __name__ == '__main__':
    app.run(debug=True)