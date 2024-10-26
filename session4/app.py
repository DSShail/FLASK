from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash
)

from forms import LoginForm,SignupForm
app=Flask(__name__)

#add secret token for csrf(cross-site request forgery)
app.config['SECRET_KEY']="this is a secret key"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='home')


@app.route("/signup",methods=['GET','POST'])
def signup():
    signup_form=SignupForm()
    if signup_form.validate_on_submit():
        flash(f"successfully registered {signup_form.username.data}!")
        return  redirect(url_for("home"))

    return render_template('signup.html',title='Signup',form=signup_form)

@app.route("/login",methods=['GET','POST'])
def login():
    login_form=LoginForm()
    email=login_form.email.data
    pw=login_form.password.data
    if login_form.validate_on_submit():
        if email=="shaileshvbs0@gmail.com" and pw=='123456':
            flash('Login successfully')
            return redirect(url_for("home"))
        else:
            flash("Incorrect email or password")
    return render_template('login.html',title='Login',form=login_form)


if __name__=="__main__":
    app.run(debug=True)