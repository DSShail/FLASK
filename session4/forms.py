from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)

from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)
class SignupForm(FlaskForm):
    
    """Length takes min length,max length
        you can even pass message inside DataRequired if valid data is not available
    """
    username=StringField(
        "Username",
        validators=[DataRequired(),Length(2,30)]
    )
    """
    here Email() class does the validation else we had to write the complex regular expresssion
    under the hood Email() uses email-valiator library for validation   
    """
    email=StringField(
        "email",
        validators=[DataRequired(),Email()]
    )
    
    gender=SelectField(
        "Gender",
        choices=['Male','Female','other'],
        validators=[Optional()]
    )
    
    dob=DateField(
        "Date of Birth",
        validators=[Optional()],
        
    )
    
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    
    confirmpassword=PasswordField(
        "Confirm Password",
        validators=[DataRequired(),Length(5,25),EqualTo("password")]
    )
    
    submitfield=SubmitField("Sign Up")
    
    

class LoginForm(FlaskForm):    
    email=StringField(
        "email",
        validators=[DataRequired(),Email()]
    )
    
    password=PasswordField(
        "Password",
        validators=[DataRequired(),Length(5,25)]
    )
    
    remember_me=BooleanField(
        "Remember Me"
    )

    submitfield=SubmitField("Login")

    