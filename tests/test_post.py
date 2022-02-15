import unittest
from datetime import date,datetime
from app.models import Election,Post

class PostModelTest(unittest.TestCase):
  def setUp(self):
    self.new_election=Election(title='Annual student elections',election_date=date.today(),start_time=datetime.utcnow(),end_time=datetime.utcnow())
    self.new_posts=Post()

