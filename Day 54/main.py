from flask import Flask
import test
print(test.test1())
print(test.__name__)

app = Flask(__name__)

@app.route('/')
def hellow_world():
    return '<h1>Hello, World!</h1>'

if __name__ == "__main__":
    app.run()