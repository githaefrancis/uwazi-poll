from email.policy import default
from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  '''
  User class that defines the user model

  Args:
      UserMixin and parent class db.Model
  '''
  __tablename__='users'
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(255))
  username=db.Column(db.String(255))
  email=db.Column(db.String(255))
  created_at=db.Column(db.DateTime,default=datetime.utcnow)
  bio=db.Column(db.String(255))
  profile_pic_path=db.Column(db.String(255))
  password_secure=db.Column(db.String(255))
  role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))
  candidates=db.relationship('Candidate',backref='user',lazy='dynamic')
  votes=db.relationship('Vote',backref='user',lazy='dynamic')
  student_id=db.Column(db.String(50),default=None,unique=True)
  status=db.Column(db.String(50),default="active")

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')
  

  @password.setter
  def password(self,password):
    self.password_secure=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_secure,password)

  def save_user(self):
    db.session.add(self)
    db.session.commit()
  
  def __repr__(self):
    return f'User{self.username}'

class Role(db.Model):
  '''
  Role class that defines the Role model
  '''
  __tablename__='roles'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255))
  users=db.relationship('User',backref='role',lazy='dynamic')



class Election(db.Model):
  '''
  Election class that defines the Election Model
  '''
  __tablename__='elections'
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(255))
  election_date=db.Column(db.Date)
  start_time=db.Column(db.DateTime)
  end_time=db.Column(db.DateTime)
  active=db.Column(db.Boolean,default=False)
  status=db.Column(db.String(50),default="open")
  posts=db.relationship('Post',backref="election",lazy='dynamic')
  
  def save_election(self):
    db.session.add(self)
    db.session.commit()

class Post(db.Model):
  '''
  Post class that defines the election post model
  '''
  __tablename__='posts'
  id=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(255))
  election_id=db.Column(db.Integer,db.ForeignKey('elections.id'))
  candidates=db.relationship('Candidate',backref='post',lazy='dynamic')
  votes=db.relationship('Vote',backref='post',lazy='dynamic')

  def save_post(self):
    db.session.add(self)
    db.session.commit()

class Candidate(db.Model):
  '''
  Candidate class that defines the candidate model
  '''
  __tablename__='candidates'
  id=db.Column(db.Integer,primary_key=True)
  post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
  win=db.Column(db.Boolean,default=False)
  votes=db.relationship('Vote',backref='candidate',lazy='dynamic')

  def save_candidate(self):
    db.session.add(self)
    db.session.commit()

  def remove_candidate(self):
    db.session.delete(self)
    db.session.commit()

class Vote(db.Model):
  '''
  Vote class that defines the Vote model
  '''
  __tablename__='votes'
  id=db.Column(db.Integer,primary_key=True)
  user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
  post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))
  candidate_id=db.Column(db.Integer,db.ForeignKey('candidates.id'))
  status=db.Column(db.String(255),default="active")

  def save_vote(self):
    db.session.add(self)
    db.session.commit()