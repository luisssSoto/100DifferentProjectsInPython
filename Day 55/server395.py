from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    u = request.url
    print(f"URL: {u}")
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"> </img>')

from random import randint

mysterious_num = randint(0, 9)
print(f"Mysterious number: {mysterious_num}")

# 1. Approach
def url_num_decorator(fun):
    def wrapper(*args):
        n = fun(*args)
        if n < mysterious_num:
            return ('<h1 style="color:red"> Too low, try again! </h1>'
                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="low-puppy">')
        elif n > mysterious_num:
            return ('<h1 style="color:purple"> Too high, try again! </h1>'
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="high-puppy">')
        else:
            return ('<h1 style="color:green"> You found me!</h1>'
                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="correct-puppy">')
    return wrapper


@app.errorhandler(404)
@url_num_decorator
def page_not_found(e):
    url = request.url.replace("/", "")
    num = int(url[18:])
    return num


# 2. Approach
@app.route("/<int:guess>")
def guess_num(guess):
    if guess < mysterious_num:
        return ('<h1 style="color:red"> Too low, try again! </h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="low-puppy">')
    elif guess > mysterious_num:
        return ('<h1 style="color:purple"> Too high, try again! </h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="high-puppy">')
    else:
        return ('<h1 style="color:green"> You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="correct-puppy">')


if __name__ == '__main__':
    app.run(debug=True)


