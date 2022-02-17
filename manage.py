from app import create_app,db
from app.models import User,Role,Election,Post,Candidate,Vote
from flask_migrate import Migrate

# app=create_app('development')
app=create_app('mainConfig')
migrate=Migrate()
migrate.init_app(app,db)

@app.cli.command()
def test():
  """
  Run unit tests
  """
  import unittest

  tests=unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

@app.shell_context_processor
def make_shell_context():
  return dict(app=app,db=db,User=User,Role=Role,Election=Election,Post=Post,Candidate=Candidate,Vote=Vote)

if __name__=='__main__':
  app.run()