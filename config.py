
import os

class Config:
  '''
  General configuration parent class
  '''
  SECRET_KEY=os.environ.get("SECRET_KEY")


class ProdConfig(Config):
  '''
  Production configuration child class
  '''
  pass

class DevConfig(Config):
  '''
  Development configuratiion child class
  '''
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/uwazi_poll'

  DEBUG=True

class TestConfig(Config):
  '''
  Test configuration child class
  '''
  pass

config_options={

  'production':ProdConfig,
  'development':DevConfig,
  'test':TestConfig
}
