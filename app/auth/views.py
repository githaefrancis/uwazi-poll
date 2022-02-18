from flask import render_template,url_for,redirect,flash,request
from flask_login import current_user, login_required,login_user,logout_user
from . import auth
from .forms import AdminLoginForm, RegistrationForm, StudentLoginForm
from ..models import User,Role

@auth.route('/login',methods=['GET','POST'])
def login():
  login_form=StudentLoginForm()
  if current_user.is_authenticated and current_user.role_id==1:
    return redirect(url_for('main.home'))
  if login_form.validate_on_submit():
    user=User.query.filter_by(student_id=login_form.student_id.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user)
      flash(f'Welcome, {user.name}','success')
      return redirect(request.args.get('next') or url_for('main.home'))
    flash('Invalid username or password','error')


  return render_template('auth/login.html',login_form=login_form)
  # return render_template('auth/login.html',login_form=login_form)

@auth.route('/admin/login',methods=['GET','POST'])
def admin_login():
  login_form=AdminLoginForm()

  if current_user.is_authenticated and current_user.role_id==2:
    
    return redirect(url_for('admin.admin_view'))
  elif current_user.is_authenticated and current_user.role_id==1:
     logout_user()
     return redirect(url_for('auth.admin_login'))
    
  if login_form.validate_on_submit():
    user=User.query.filter_by(email=login_form.email.data,role_id=2).first()
    print('validated')
    if user is not None and user.verify_password(login_form.password.data):
      print('password_verified')
      login_user(user)
      flash(f'Welcome, {user.name}','success')
      
      return redirect(request.args.get('next') or url_for('admin.admin_view'))
    flash('Invalid username or password','error')
  return render_template('auth/adminLogin.html',login_form=login_form)

@auth.route('/register',methods=['GET','POST'])
def register():
  register_form=RegistrationForm()
  if register_form.validate_on_submit():
    name_input=register_form.name.data
    email_input=register_form.email.data
    student_id=register_form.student_id.data
    password_input=register_form.password.data
    user_role=Role.query.filter_by(name='User').first()
    # user_role=Role.query.filter_by(name='Admin').first()
    user=User(name=name_input,email=email_input,password=password_input,role=user_role,student_id=student_id)
    user.save_user()
    # admin=User(name=name_input,email=email_input,password=password_input,role=user_role)
    # admin.save_user()
    
    # mail_message("Welcome to Fluent Exchange","email/welcome",user.email,user=user)
    flash('Registration Successful','success')
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html',register_form=register_form)


@auth.route('/user/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for("main.index"))

