from flask import render_template, url_for, redirect
from app.forms import Register, Login
from app.models import Students
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def index():
    return render_template('index.html', title='HomePage')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = Register()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        student = Students(username=form.username.data, email = form.email.data, password = hashed_pass)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title = 'Register', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = Login()
    if form.validate_on_submit():
        student = Students.query.filter_by(email=form.email.data).first()
        if student and bcrypt.check_password_hash(student.password, form.password.data):
            login_user(student, remember=form.remember.data)
            return redirect(url_for('user'))
        else:
            return render_template('404.html')
    return render_template('login.html', title = 'Login', form = form)

@app.route('/user')
def user():
    return render_template('user.html', title='Dashboard')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
   return render_template('account.html', title='Account')