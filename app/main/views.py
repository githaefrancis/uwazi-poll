from flask import render_template
from . import main
from flask import redirect, render_template,request,url_for
from flask_login import current_user, login_required
from ..models import Candidate, Election, Post,User

@main.route('/')
def index():
  elections = Election.query.all();
  return render_template('main/index.html',elections=elections)


@main.route('/student')
def student():
  elections = Election.query.all();

  return render_template('main/stdView_1.html',elections=elections)

  # return render_template('main/student.html',title='Student') 


# @main.route('/student/elections') 
# def testStudent():
#   elections = Election.query.all();
#   return render_template('main/stdView_1.html',elections=elections)


@main.route('/student/election/<election_id>',methods=['GET','POST']) 
@login_required
def submitElection(election_id):
  post=Post.query.filter_by(election_id=election_id).first()
  candidates = Candidate.query.filter_by(post_id=post.id).join(User, Candidate.user_id == User.id).all()
  return render_template('main/newest.html',post=post, candidates=candidates)

