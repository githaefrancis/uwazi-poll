from sqlite3 import dbapi2

from sqlalchemy import true
from .models import User,Role,Election,Post,Candidate,Vote


def get_elections():
  electionslist=Election.query.all()
  print(electionslist)
  return electionslist

def get_single_election(id):
  return Election.query.filter_by(id=id).first()

def get_posts_per_election(id):
  return Post.query.filter_by(election_id=id).all()

def get_posts_count_per_election(id):
  return len(get_posts_per_election(id))

def get_single_post(id):
  return Post.query.filter_by(id=id).first()

def get_candidates_per_post(id):
  '''
  Method that fetches candidates of an election post
  Args: id of the election post
  Return: list of candidates for the post
  '''

  return Candidate.query.filter_by(post_id=id).all()

def get_candidates_for_all_posts_per_election(id):
  candidates_dict={}
  posts=get_posts_per_election(id)
  for post in posts:
    candidates_list=get_candidates_per_post(post.id)
    candidates_dict[post.id]=candidates_list

  return candidates_dict

def get_votes_for_candidate_count_per_post(id):
  
  '''
  method to fetch all votes for a candidate
  '''
  
  votes_dict={}
  candidates=Candidate.query.filter_by(post_id=id).all()
  for candidate in candidates:
    vote_count=len(Vote.query.filter_by(post_id=id,candidate_id=candidate.id).all())
    votes_dict[candidate.id]=vote_count

  return votes_dict



def get_posts_count_for_all_elections():
  '''
  method to fetch post count for elections
  '''
  posts_dict={}
  elections=Election.query.all()
  for election in elections:
    post_count=len(Post.query.filter_by(election_id=election.id).all())
    posts_dict[election.id]=post_count

  return posts_dict



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

def has_voted_all_posts(voter_id,election_id):
  vote_status_dict={}
  posts=get_posts_per_election(election_id)
  for post in posts:
    status=has_voted(voter_id,post.id)
    vote_status_dict[post.id]=status
  return vote_status_dict

def get_the_winner_in_a_post(post_id):
  votes=get_votes_for_candidate_count_per_post(post_id)
  post=Post.query.filter_by(id=post_id).first()
  if post.election.status=='open':
    return None
  if votes:
    highest_vote_candidate_id=max(votes,key=votes.get)
    if votes[highest_vote_candidate_id]>0:
      candidate=Candidate.query.filter_by(id=highest_vote_candidate_id).first()
      return candidate.user.name

    else:
      return None
  else:
     return None
def get_all_election_winners(election_id):
  all_election_winners={}
  all_posts=get_posts_per_election(election_id)
  for post in all_posts:
    all_election_winners[post.id]=get_the_winner_in_a_post(post.id)

  return all_election_winners

