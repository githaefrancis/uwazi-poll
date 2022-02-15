from app.models import User,Election
import unittest
from datetime import date, datetime,time

class ElectionModelTest(unittest.TestCase):
  def setUp(self):
    self.new_election=Election(title='Annual student elections',election_date=date.today(),start_time=datetime.utcnow(),end_time=datetime.utcnow())

  def tearDown(self):
    Election.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_election.title,'Annual student elections')
    self.assertEquals(self.new_election.election_date,date.today())

  def test_save_election(self):
    self.new_election.save_election()
    self.assertTrue(len(Election.query.all())>0)