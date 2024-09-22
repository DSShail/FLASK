from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the home page!</h1>"


@app.route("/welcome/steve")
def welcome_steve():
    return "<h1>Hey Steve Welcome to the our home page!</h1>"


@app.route("/welcome/<name>")
def welcome_tonny(name):
    return f"<h1>Hey {name}, Welcome to the our home page!</h1>"

if __name__ == "__main__" :
    app.run(debug=True)