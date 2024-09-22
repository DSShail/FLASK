from flask import Flask,redirect,url_for
import time

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"


@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        #redirect to fail page
        #url_for will generate the url for failed function and redirect will redirect to the fail page
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        #redirect to pass page
        return redirect(url_for("passed"))
        
@app.route("/pass")
def passed():    
    return "<h1> Congrats, you have passed </h1>"
        
@app.route("/fail")
def failed():
    return "<h1> Sorry, you have failed</h1>"

if __name__ == "__main__":
    app.run(debug=True)