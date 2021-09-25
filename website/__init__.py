from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

def create_app():
  app = Flask(__name__)
  app.config['SCRIPT_KEY'] = 'random string'
  api = Api(app)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
  db = SQLAlchemy(app)
  db.create_all()

  from .views import views
  from .auth import auth
  from .api.auth import Auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  api.add_resource(Auth, '/api/auth/<int:user_id>')

  return app
