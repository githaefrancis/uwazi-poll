from sqlite3 import dbapi2
from .models import User,Role,Election,Post,Candidate,Vote





def get_elections():
  electionslist=Election.query.all()
  print(electionslist)
  return

def get_single_election(id):
  return Election.query.filter_by(id=id).first()

def get_posts_per_election(id):
  return Post.query.filter_by(election_id=id).all()

def get_single_post(id):
  return Post.query.filter_by(id=id).first()

def get_candidates_per_post(id):
  '''
  Method that fetches candidates of an election post
  Args: id of the election post
  Return: list of candidates for the post
  '''

  return Candidate.query.filter_by(post_id=id).all()

def get_votes_count_per_post(id):
  pass

