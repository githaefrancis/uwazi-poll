from re import A
from flask import redirect, render_template,request,url_for
from flask_login import current_user, login_required
from . import admin
from .forms import ElectionForm, PostForm
from ..models import Election, Post
from datetime import datetime


@admin.route('/admin',methods=['GET','POST'])
@login_required
def admin_view():
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
  if current_user.role_id==1:
    return redirect(url_for('main.index'))
  post=Post.query.filter_by(id=post_id).first()

  return render_template('admin/post.html',post=post)
  
