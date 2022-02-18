from flask import render_template,request,redirect,url_for,flash
from flask_login import current_user,login_required
from app.models import Election, User
from . import main
from werkzeug.utils import secure_filename
import os
from ..request import get_elections, get_posts_count_for_all_elections,get_candidates_for_all_posts_per_election, get_posts_per_election, has_voted_all_posts,vote_for_candidate,get_all_election_winners


ALLOWED_EXTENSIONS={'png','jpg','jpeg','gif'}

@main.route('/')
def index():
  if current_user.is_authenticated and current_user.role_id==2:
    return redirect(url_for('admin.admin_view')) 
  elif current_user.is_authenticated and current_user.role_id==1:
    return redirect(url_for('main.home'))
  else:
    return render_template('main/index.html')

@main.route('/student')
def student():
  return render_template('main/student.html',title='Student')  

@main.route('/home')
@login_required
def home():
  election_list=get_elections()
  post_count=get_posts_count_for_all_elections()
  return render_template('main/home.html',election_list=election_list,post_count=post_count)

@main.route('/election/<id>/vote')
def vote(id):
  election=Election.query.filter_by(id=id).first()
  posts=get_posts_per_election(id)
  all_candidates=get_candidates_for_all_posts_per_election(id)
  vote_status=has_voted_all_posts(current_user.id,id)

  election_winners={}
  if election.status=='closed':
    election_winners=get_all_election_winners(election.id)


  return render_template('main/vote.html',election=election,all_candidates=all_candidates,posts=posts,vote_status=vote_status,election_winners=election_winners)

@main.route('/election/<id>/vote/post/<post_id>/candidate/<candidate_id>')
def cast_vote(id,post_id,candidate_id):
  vote_for_candidate(current_user.id,post_id,candidate_id)
  return redirect(url_for('main.vote',id=id))



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