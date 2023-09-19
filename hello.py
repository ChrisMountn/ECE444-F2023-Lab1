from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'asdhsi-98h-2gh0179bh02937hb092-9nbnu'

class EmailNameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your email?', validators=[DataRequired(), Email("Please Enter Your U of T Email Address")])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    emailNameForm = EmailNameForm()
    if emailNameForm.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != emailNameForm.name.data:
            flash("Looks like you have changed your name!")
        if "utoronto" not in emailNameForm.email.data:
          flash("You have not submitted a U of T Email Address. Please submit a U of T Address.")
        else:
            session['name'] = emailNameForm.name.data
            session['email'] = emailNameForm.email.data
            return redirect(url_for('index'))
    return render_template('index.html', emailnameform=emailNameForm, name=session.get('name'), email = session.get('email'))

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500