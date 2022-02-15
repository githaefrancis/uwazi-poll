import unittest
from datetime import date,datetime
from app.models import Candidate, Election,Post,User,Role

class PostModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Person One",username='person',password='password',email="personone@gmail.com",role=Role.query.filter_by(id=1).first())

    self.new_election=Election(title='Annual student elections',election_date=date.today(),start_time=datetime.utcnow(),end_time=datetime.utcnow())
    self.new_post=Post(title='Student Leader',election=self.new_election)
    self.new_candidate=Candidate(post=self.new_post,user=self.new_user)
  def tearDown(self):
    Candidate.query.delete()
    Post.query.delete()
    Election.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_post.title,'Student Leader')

  def test_save_candidate(self):
    self.new_election.save_election()
    self.new_post.save_post()
    self.new_candidate.save_candidate()

    self.assertTrue(len(Candidate.query.all())>0)