from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def get_data():
    if request.method == "POST":
        print(request.form)
        user_name=request.form['user_name']
        user_password=request.form['user_password']
        return (f"<h1>{user_name} {user_password}</h1>")

if __name__ == '__main__':
    app.run(debug=True, port=5001)