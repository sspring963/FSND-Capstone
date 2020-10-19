import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, Movie, Actor

def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def home():
        return jsonify({
            'success': True
            })

    @app.route('/movies', methods=['GET'])
    def get_Movies():
        movies = Movie.query.all()
        
        formatted_movies = [movie.format() for movie in movies]
        
        return jsonify({
            'success':True,
            'drinks': formatted_movies
            })
    
    @app.route('/actors', methods=['GET'])
    def get_Actors():
        actors = Actor.query.all()
        
        formatted_actors = [actor.format() for actor in actors]
        
        return jsonify({
            'success':True,
            'drinks':formatted_actors
            })
    
    @app.route('/movies', methods=['POST'])
    def post_movies():
        body = request.get_json()
        
        
        
        if body.get('title') == '' or body.get('release_date') == '' or body.get('actor_id') == '':
            abort(404)
        
        new_title = body.get('title')
        new_release_date = body.get('release_date')
        new_actor_id = body.get('actor_id')
        
        
        try:
            new_movie = Movie(title=new_title, 
                              release_date=new_release_date,
                              actor_id=new_actor_id)
            new_movie.insert()
        
            return jsonify({
                'success':True,
                'movies': new_movie.format()
                })
        except BaseException:
            abort(422)
    
    
    @app.route('/actors', methods=['POST'])
    def post_actors():
        body = request.get_json()
        
        
        if body.get('name') == '' or body.get('age') == '' or body.get('gender') == '':
            abort(404)
        
        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')
        
        
        try:
            new_actor = Actor(name=new_name, 
                              age=new_age,
                              gender=new_gender)
            new_actor.insert()
            
            return jsonify({
                'success':True,
                'movies': new_actor.format()
                })
        except BaseException:
            abort(422)
    
    @app.route('/movies/<int:id>', methods=['PATCH'])
    def update_movies(id):
        body = request.get_json()
        
        if not id:
            abort(400)
        
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if not movie:
            abort(404)
        
        update_title = body.get('title')
        update_release_date = body.get('release_date')
        update_actor_id = body.get('actor_id')
        
        try:
            if update_title:
                movie.title = update_title
                
            if update_release_date:
                movie.release_date = update_release_date
                
            if update_actor_id:
                movie.actor_id = update_actor_id
                
            movie.update()
            
            return jsonify({
                'success': True,
                'movie': movie.format()
               })
        except BaseException:
            abort(422)
            
    @app.route('/actors/<int:id>', methods=['PATCH'])
    def update_actors(id):
        body = request.get_json()
        
        if not id:
            abort(400)
        
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if not actor:
            abort(404)
        
        update_name = body.get('name')
        update_age = body.get('age')
        update_gender = body.get('gender')
        
        try:
            if update_name:
                actor.name = update_name
                
            if update_age:
                actor.age = update_age
                
            if update_gender:
                actor.gender = update_gender
                
            actor.update()
            
            return jsonify({
                'success': True,
                'actor': actor.format()
               })
        except BaseException:
            abort(422)
            
    @app.route('/movies/<int:id>', methods=['DELETE'])
    def delete_movie(id):
        body = request.get_json()
        
        if not id:
            abort(400)
        
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if not movie:
            abort(404)
            
        movie.delete()
        
        return jsonify({
            'success': True,
            'delete': id
            })
    
    
    @app.route('/actors/<int:id>', methods=['DELETE'])
    def delete_actor(id):
        body = request.get_json()
        
        if not id:
            abort(400)
        
        actor = Actor.query.filter(Actor.id == id).one_or_none()
        if not actor:
            abort(404)
            
        actor.delete()
        
        return jsonify({
            'success': True,
            'delete': id
            })
    
    
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
            
        

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "Bad Request"
        }), 400
    
    
    @app.errorhandler(404)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Resource Not Found"
        }), 404
    
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "Internal Server Error"
        }), 500
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)