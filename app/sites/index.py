from flask import url_for, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from flask_wtf          import FlaskForm, RecaptchaField
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, DataRequired

from app import app
from app.database.database import *


""" ############# """
""" login manager """
""" ############# """

login_manager = LoginManager()
login_manager.init_app(app)

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'        , validators=[DataRequired()])
	password    = PasswordField(u'Password'        , validators=[DataRequired()])
	remember    = BooleanField('remember me')

@login_manager.user_loader
def load_user(user_id):
    return GET_USER_BY_ID(user_id)


""" ################### """
""" site login / logout """
""" ################### """

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    
    # define login form here
    form = LoginForm()

    # Flask message injected into the page, in case of any errors
    msg = None

    # custommize your page title / description here
    page_title = 'Login - Flask Dark Dashboard | AppSeed App Generator'
    page_description = 'Open-Source Flask Dark Dashboard, login page.'

    if form.validate_on_submit():
        user = GET_USER_BY_NAME(form.username.data)

        if user:
            
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

            else:
                return redirect(url_for('logout'))


    # try to match the pages defined in -> themes/light-bootstrap/pages/
    return render_template( 'layouts/default.html',
                            title=page_title,
                            content=render_template( 'pages/login.html', 
                                                    form=form,
                                                    msg=msg) )


# logout user
@app.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('index'))