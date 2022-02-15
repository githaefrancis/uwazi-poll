from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

simple=SimpleMDE()
bootstrap=Bootstrap()
csrf=CSRFProtect()
mail=Mail()

def create_app(config_name):
  app=Flask(__name__)
  app.config.from_object(config_options[config_name])
  
  db.init_app(app)
  login_manager.init_app()
  simple.init_app()
  csrf.init_app(app)
  bootstrap.init_app(app)
  mail.init_app(app)


  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  from .admin import admin as admin_blueprint
  app.register_blueprint(admin_blueprint)
  
  return app


 