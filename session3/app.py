from flask import Flask,render_template,url_for
from employees import employees_data

#create the  flask app
app=Flask(__name__)

#home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home Page")

#about page
@app.route("/about")
def about():
    return render_template("about.html",title="About Page")

@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template(
        "evaluate.html",
        title="Evaluate",
        number=num
    )
@app.route("/employees")
def employees_info():
    return render_template("employees.html",
                           title="Employees",
                           employees=employees_data)
    
@app.route("/employees/managers")
def managers_info():
    return render_template("managers.html",
                           title="Managers",
                           employees=employees_data)    

#start the app in debug mode
if(__name__=="__main__"):
    app.run(debug=True)
