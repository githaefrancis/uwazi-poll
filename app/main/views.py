from flask import render_template,request,redirect,url_for,flash
from flask_login import current_user,login_required
from app.models import User
from . import main
from werkzeug.utils import secure_filename
import os
from ..request import get_elections, get_posts_count_for_all_elections


ALLOWED_EXTENSIONS={'png','jpg','jpeg','gif'}

@main.route('/')
def index():
  return render_template('main/index.html')


@main.route('/student')
def student():
  return render_template('main/student.html',title='Student')  

@main.route('/home')
def home():
  election_list=get_elections()
  post_count=get_posts_count_for_all_elections()
  return render_template('main/home.html',election_list=election_list,post_count=post_count)

@main.route('/election/<id>/vote')
def vote(id):
  return render_template('main/vote.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/user/<user_name>/profile',methods=['GET','POST'])
def profile(user_name):

  user=User.query.filter_by(id=current_user.id).first()
  if request.method=='POST':
    photo=request.files['photo']
    if photo and allowed_file(photo.filename):
      filename=secure_filename(photo.filename)
      photo.save(os.path.join('app/static/photos',filename))
      user.profile_pic_path=f'photos/{filename}'
      user.save_user()
      flash('Update Successful','success')
    else:
      flash('Please provide a valid file','error')

  return render_template('main/profile/profile.html')