from flask import Flask

app=Flask(__name__)

#creating a endpoint - when someone calls our endpoint we are going to call home function
@app.route("/") #forward slash means the home page
@app.route("/home") # we can have multiple endpoints for the same function
def home():
    return "<h1>Welcome to the home page</h1>"


@app.route("/about") #creating another endpoint
def about():
    return "<h1>Welcome to the about page </h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi {name.title()},you're welcome to this page!</h1>"


@app.route("/addition/<int:num>")
def additon(num):
    return f"<h1>Input is {num}, output is {num + 10} </h1>"

@app.route("/addition2/<int:num1>/<int:num2>")
def additon2(num1,num2):
    return f"<h1>Input is {num1} + {num2} is, output is {num1 + num2} </h1>"
if __name__=="__main__":
    app.run(debug=True)