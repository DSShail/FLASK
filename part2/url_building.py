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
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        time.sleep(1)
        #redirect to pass page
        return redirect(url_for("passed",sname=name,marks=num))
    
   
        
@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):    
    return f"<h1> Congrats {sname}, you have passed with {marks} marks</h1>"
        
@app.route("/fail/<sname>/<marks>")
def failed(sname,marks):
    return f"<h1> Sorry {sname}, you have failed with {marks} marks</h1>"

if __name__ == "__main__":
    app.run(debug=True)