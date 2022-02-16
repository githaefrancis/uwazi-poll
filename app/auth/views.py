from flask import render_template
from . import auth
from .forms import AdminLoginForm, RegistrationForm, StudentLoginForm
@auth.route('/login')
def login():
  login_form=StudentLoginForm()
  return render_template('auth/login.html',login_form=login_form)

@auth.route('/admin/login')
def admin_login():
  login_form=AdminLoginForm()
  return render_template('auth/adminLogin.html',login_form=login_form)

@auth.route('/register')
def register():
  register_form=RegistrationForm()
  return render_template('auth/register.html',register_form=register_form)