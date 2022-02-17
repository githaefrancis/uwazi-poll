from sqlite3 import dbapi2

from sqlalchemy import true
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

def get_votes_for_candidate_count_per_post(id):
  
  '''
  method to fetch all votes for a candidate
  '''
  
  votes_dict={}
  candidates=Candidate.query.filter_by(post_id=id).query.all()
  for candidate in candidates:
    vote_count=len(Vote.query.filter_by(post_id=id,candidate_id=candidate.id).all())
    votes_dict[candidate.id]=vote_count

  return votes_dict

def vote_for_candidate(voter_id,post_id,candidate_id):
  '''
  Method to vote for a candidate

  Args: voter_id is the user_id of the student 
  '''
  new_vote=Vote(user_id=voter_id,post_id=post_id,candidate_id=candidate_id)
  new_vote.save_vote()
  return

def has_voted(voter_id,post_id):
  '''
  method to check if a user has already voted
  '''
  if Vote.query.filter_by(user_id=voter_id,post_id=post_id).first():
    return True
  else:
    return False