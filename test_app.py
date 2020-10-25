import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


class MovieTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "movie_agency_test"
        self.database_path = os.getenv('TEST_URL')
        setup_db(self.app, self.database_path)
        self.executive_producer = os.getenv('EXECUTIVE_PRODUCER')
        # self.casting_director = os.environ['CASTING_DIRECTOR']
        self.casting_assistant = os.getenv('CASTING_ASSISTANT')

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_a_get_actors(self):
        update_actor = Actor('Tom Hardy', 44, 'male')
        update_actor.insert()

        res = self.client().get(
            '/actors',
            headers={
                'Authorization': 'Bearer ' + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['actors'])

    def test_401_no_authorization_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEquals(data['success'], False)
        self.assertEquals(
            data['description'],
            "Authorization header is expected.")

    def test_b_get_movies(self):
        movie = Movie("title", "1999-9-9", 1)
        movie.insert()

        res = self.client().get(
            '/movies',
            headers={
                'Authorization': 'Bearer ' + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['movies'])

    def test_401_no_auth_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEquals(data['success'], False)
        self.assertEquals(
            data['description'],
            "Authorization header is expected.")

    def test_post_actors(self):
        self.new_actor = {
            'name': 'name',
            'age': 32,
            'gender': "female"
        }

        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                'Authorization': 'Bearer ' + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['movies'])

    def test_422_create_actor_with_missing_data_fields(self):
        self.new_actor = {
            'name': 'name',
            'gender': "female"
        }

        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                'Authorization': 'Bearer ' + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 422)
        self.assertEquals(data['success'], False)
        self.assertEquals(data['message'], "unprocessable")

    def test_post_movie(self):
        self.new_movie = {
            "title": "new",
            "release_date": "1993-01-08",
            "actor_id": 1
        }

        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                'Authorization': 'Bearer ' + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['movies'])

        movie = Movie.query.filter(Movie.title == "new").one_or_none()
        movie.delete()

    def test_422_create_movie_with_missing_data_fields(self):
        self.new_movie = {
            "title": "Jurassic Park",
            "release_date": "1993-01-08",
            "actor_id": 2
        }

        res = self.client().post(
            '/actors',
            json=self.new_movie,
            headers={
                'Authorization': 'Bearer ' + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 422)
        self.assertEquals(data['success'], False)
        self.assertEquals(data['message'], "unprocessable")

    def test_update_actor(self):
        # insert actor to update
        update_actor = Actor('Tom Hardy', 44, 'male')
        update_actor.insert()
        id = update_actor.id

        self.new_info = {
            "name": "Orlando Bloom"
        }

        res = self.client().patch('/actors/' + str(id), json=self.new_info,
                                  headers={'Authorization': 'Bearer '
                                           + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['actor'])

    def test_400_wrong_id_update_actor(self):

        res = self.client().patch('/actors/9999',
                                  headers={'Authorization': 'Bearer '
                                           + self.executive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Resource Not Found")

    def test_update_movie(self):
        # insert movie to update
        update_movie = Movie('update_movie', "1998-9-9", 1)
        update_movie.insert()
        id = update_movie.id

        self.new_info = {
            "title": "new movie"
        }

        res = self.client().patch('/movies/' + str(id), json=self.new_info,
                                  headers={'Authorization': 'Bearer '
                                           + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['movie'])

    def test_400_wrong_id_update_movie(self):

        res = self.client().patch('/movies/9999999',
                                  headers={'Authorization': 'Bearer '
                                           + self.executive_producer})
        data = json.loads(res.data)

        self.assertEquals(res.status_code, 404)
        self.assertEquals(data['success'], False)
        self.assertEquals(data['message'], "Resource Not Found")

    def test_delete_actor(self):
        # insert actor to delete
        delete_actor = Actor('name', 2, "male")
        delete_actor.insert()
        id = delete_actor.id

        res = self.client().delete('/actors/' + str(id),
                                   headers={'Authorization': 'Bearer '
                                            + self.executive_producer})
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == id).one_or_none()

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['delete'])
        self.assertEqual(actor, None)

    def test_404_delete_non_existing_actor(self):
        res = self.client().delete('/actors/9999',
                                   headers={'Authorization': 'Bearer '
                                            + self.executive_producer})
        data = json.loads(res.data)
        self.assertEquals(res.status_code, 404)
        self.assertEquals(data['success'], False)
        self.assertEqual(data['message'], "Resource Not Found")

    def test_delete_movie(self):
        delete_movie = Movie("title", "1999-9-9", 1)
        delete_movie.insert()
        id = delete_movie.id

        res = self.client().delete('/movies/' + str(id),
                                   headers={'Authorization': 'Bearer '
                                            + self.executive_producer})
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == id).one_or_none()

        self.assertEquals(res.status_code, 200)
        self.assertEquals(data['success'], True)
        self.assertTrue(data['delete'])
        self.assertEqual(movie, None)

    def test_404_delete_non_existing_movie(self):
        res = self.client().delete('/movies/9999',
                                   headers={'Authorization': 'Bearer '
                                            + self.executive_producer})
        data = json.loads(res.data)
        self.assertEquals(res.status_code, 404)
        self.assertEquals(data['success'], False)
        self.assertEqual(data['message'], "Resource Not Found")

    def test_401_post_actor_not_permitted_for_casting_assistant(self):
        self.new_actor = {
            'name': 'name',
            'age': 32,
            'gender': "female"
        }

        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                'Authorization': 'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEquals(data['success'], False)
        self.assertEquals(data['description'], "Permission not found.")

    def test_401_post_movie_not_permitted_for_casting_assistant(self):
        self.new_movie = {
            "title": "new",
            "release_date": "1993-01-08",
            "actor_id": 13
        }

        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                'Authorization': 'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEquals(data['success'], False)
        self.assertEquals(data['description'], "Permission not found.")


if __name__ == "__main__":
    unittest.main()
