from flask import Flask, render_template, request
import requests
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a4ffd101371c286dc6a7ee35a7cb997e289a3e0d
import smtplib
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length
import os


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(
        min=8, max=50, message="Must contain 8 - 50 characters")])
    submit = SubmitField(label="Log In")


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    message = StringField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label="Send Mail")


MY_EMAIL = os.environ.get("SITE_EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
<<<<<<< HEAD
>>>>>>> a4ffd10... login and email validators now working
=======
>>>>>>> a4ffd101371c286dc6a7ee35a7cb997e289a3e0d

app = Flask(__name__)
app.secret_key = "ThisIsGold"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


<<<<<<< HEAD
<<<<<<< HEAD
@app.route('/contact')
=======
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


@app.route('/contact', methods=['GET', 'POST'])
>>>>>>> a4ffd101371c286dc6a7ee35a7cb997e289a3e0d
def contact():
    contact_form = ContactForm()
    if request.method == 'POST':
        if contact_form.validate_on_submit():
            data = request.form
            send_email(data["name"], data["email"], data["message"])
            return render_template('contact.html', msg_sent=True, form=contact_form)
    return render_template('contact.html', msg_sent=False, form=contact_form)


<<<<<<< HEAD
=======
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if request.method == 'POST':
        if contact_form.validate_on_submit():
            data = request.form
            send_email(data["name"], data["email"], data["message"])
            return render_template('contact.html', msg_sent=True, form=contact_form)
    return render_template('contact.html', msg_sent=False, form=contact_form)


=======
>>>>>>> a4ffd101371c286dc6a7ee35a7cb997e289a3e0d
def send_email(name, email, message):
    email_message = f"subject:NewMessage\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(str(MY_EMAIL), str(PASSWORD))
        connection.sendmail((MY_EMAIL), (MY_EMAIL), email_message)
<<<<<<< HEAD
>>>>>>> a4ffd10... login and email validators now working
=======
>>>>>>> a4ffd101371c286dc6a7ee35a7cb997e289a3e0d


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/67e7562537ada3f5a874"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
