import unittest
from datetime import date,datetime
from app.models import Election,Post

class PostModelTest(unittest.TestCase):
  def setUp(self):
    self.new_election=Election(title='Annual student elections',election_date=date.today(),start_time=datetime.utcnow(),end_time=datetime.utcnow())
    self.new_posts=Post(title='Student Leader',election=self.new_election)

  def tearDown(self):
    Post.query.delete()
    Election.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_posts.title,'Student Leader')

  def test_save_post(self):
    self.new_election.save_election()
    self.new_posts.save_post()