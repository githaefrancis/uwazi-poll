from app import create_app
# from app.models import User,Comment,Pitch,Category,Role
# from flask_migrate import Migrate

app=create_app('development')
# migrate=Migrate()
# migrate.init_app(app,db)

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
  return dict(app=app)

if __name__=='__main__':
  app.run()