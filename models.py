import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Moives
Have title and release date
'''
class Movies(db.Model):  
  __tablename__ = 'Movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  catchphrase = Column(String)

  def __init__(self, title, catchphrase=""):
    self.title = title
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'catchphrase': self.catchphrase}


class Actors(db.Model):  
  __tablename__ = 'Actors'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  catchphrase = Column(String)

  def __init__(self, title, catchphrase=""):
    self.title = title
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'catchphrase': self.catchphrase}
    
