from re import A
from flask import redirect, render_template,request,url_for
from flask_login import current_user, login_required
from . import admin
from .forms import ElectionForm, PostForm
from ..models import Candidate, Election, Post,User
from datetime import datetime
from ..request import get_elections

@admin.route('/admin',methods=['GET','POST'])
@login_required
def admin_view():
  if current_user.is_authenticated and current_user.role_id==1:
     return redirect(url_for('main.student'))
  election_form=ElectionForm()
  elections=Election.query.order_by(Election.id.desc()).all()
  if request.method=='POST':
    if election_form.validate_on_submit():
      election_title=election_form.title.data
      start_time=election_form.start_time.data
      end_time=election_form.end_time.data
      date_time_obj=datetime.strptime(str(end_time), '%Y-%m-%d %H:%M:%S')
      new_election=Election(title=election_title,start_time=start_time,end_time=date_time_obj)
      new_election.save_election()
      return redirect(request.referrer)

  return render_template('admin/admin.html',election_form=election_form,elections=elections)

@admin.route('/admin/election/<id>/posts',methods=['GET','POST'])
@login_required
def election(id):
  if current_user.is_authenticated and current_user.role_id==1:
     return redirect(url_for('main.student'))
  election=Election.query.filter_by(id=id).first()
  post_form=PostForm()
  posts=Post.query.filter_by(election=election).all()

  if request.method=='POST':
    if post_form.validate_on_submit():
      title=post_form.title.data
      new_post=Post(title=title,election=election)
      new_post.save_post()
      return redirect(request.referrer)


  return render_template('admin/election.html',election=election,post_form=post_form,posts=posts)

@admin.route('/admin/post/election/<election_id>/post/<post_id>')
@login_required
def post(election_id,post_id):
  if current_user.is_authenticated and current_user.role_id==1:
     return redirect(url_for('main.student'))
  post=Post.query.filter_by(id=post_id).first()
  students=User.query.filter_by(role_id=1).all()
  candidates=Candidate.query.filter_by(post_id=post_id).all()
  get_elections()
  return render_template('admin/post.html',post=post,students=students,candidates=candidates,election_id=election_id)


@admin.route('/admin/post/election/<election_id>/post/<post_id>/candidate/<user_id>')
@login_required
def add_candidate(election_id,post_id,user_id):
  if current_user.is_authenticated and current_user.role_id==1:
     return redirect(url_for('main.student'))
  target_post=Post.query.filter_by(id=post_id).first()
  target_user=User.query.filter_by(id=user_id).first()

  if Candidate.query.filter_by(user=target_user,post=target_post).first():
    return redirect(url_for('admin.post',election_id=election_id,post_id=post_id))

  else:
    new_candidate=Candidate(user=target_user,post=target_post)
    new_candidate.save_candidate()

    return redirect(url_for('admin.post',election_id=election_id,post_id=post_id))


@admin.route('/admin/post/election/<election_id>/post/<post_id>/candidate/<candidate_id>/remove')
@login_required
def candidate_remove(election_id,post_id,candidate_id):
  if current_user.is_authenticated and current_user.role_id==1:
     return redirect(url_for('main.student'))
  target_candidate=Candidate.query.filter_by(id=candidate_id).first()
  if target_candidate:
    target_candidate.remove_candidate()

  return redirect(url_for('admin.post',election_id=election_id,post_id=post_id))

