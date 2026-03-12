from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/username/<name>/<int:years>/<path:last>")
def greetings(name, years, last):
    return f"<p>Hello, {name}, you are {years} old, last: {last}</p>"

# 392. Rendering HTML elements
@app.route('/render')
def render_func():
    return ('<h1 style="text-align:center"> Render Elements </h1>'
            '<p> This is a paragraph </p>'
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3pucWptZXl4bHl2Yzk2ejFpdWh2MzlyY2tneDBqMW10M3dqY3pjOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3NtY188QaxDdC/giphy.gif" width="200" height="200"></img>')
render_func()

# 393. Challenge
def make_bold(func):
    def wrapper():
        text = func()
        return f'<b>{text}</b>'
    return wrapper

def make_emphasis(func):
    def wrapper():
        text = func()
        return f'<em>{text}</em>'
    return wrapper

def make_underline(func):
    def wrapper():
        text = func()
        return f'<u>{text}</u>'
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)
