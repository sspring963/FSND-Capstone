import os
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, DateTime, Enum
from flask_sqlalchemy import SQLAlchemy
import json


database_name = "trivia"
database_path = "postgres://{}/{}".format('postgres:435s606S@localhost:5432', database_name)

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
Moive
Have title, release date, and actor
'''
class Movie(db.Model):  
  __tablename__ = 'Movie'

  id = Column(Integer, primary_key=True)
  title = Column(String(80), unique=True, nullable=False)
  release_date = Column(DateTime, nullable=False)
  actor_id = Column(Integer, ForeignKey('Actor.id'))

  def __init__(self, title, release_date, actor_id):
    self.title = title
    self.release_date = release_date
    self.actor_id = actor_id
    
  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date
      }

'''
Actor
Have name, age, gender
'''

class Actor(db.Model):  
  __tablename__ = 'Actor'

  id = Column(Integer, primary_key=True)
  name = Column(String(80))
  age = Column(Integer)
  gender = Column(Enum("female", "male", name="sex",))
  movies = db.relationship("Movies", db.backref('actor'), lazy=True)

  def __init__(self, name, age, gender):
    self.name = name
    self.gender = gender
    self.age = age
    
  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'gender': self.gender
      }
    
