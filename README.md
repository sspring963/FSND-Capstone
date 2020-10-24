# Capstone Project

## Movie Casting Agency
This is my final capstone project for Udacity's Full Stack Developer Nano Degree. Its simulates the backend application for a casting agency that creates movies and assigns actors to those movies.

## Getting Started 

### Prerequisites 

#### Python 3.7.4
This application was built and tested using python 3.7.4 though it can work with higher versions. Install the lasted version of python from [here](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Environment
It is recommended to operate python projects in a virtual environments to keep their dependencies independent and seperate. Instructions to set up a virtual environment can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies 
After the virtual environment has been created and running, install dependencies by running:
		
		$ pip install -r requirements.txt

#### Key Dependencies
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/)is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.
- [jose](https://python-jose.readthedocs.io/en/latest/)JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


### Local Deployment

#### Setting Up the Database

Create local database:

		$ createdb movie_agency
 
#### Migrations
Run migrations with manage.py like this or use flask db migrate.

		$ python manage.py db init
		$ python manage.py db upgrade 
		$ python manage.py db migrate

#### Running the Server
Before running the server, update and load the environment variables. Go to setup.sh and update user and password in DEFAULT_URL and TEST_URL. Do not edit other variables.

		DEFAULT_URL='postgres://user:password@localhost:5432/movie_agency'
		TEST_URL='postgres://user:password@localhost:5432/movie_agency_test'

To run the server, execute:

		$ set FLASK_APP=app.py
		$ flask run --reload

This will reload the server everytime a change is saved to the application.

#### Testing 

Create test database:
		
		$ createdb movie_agency_test

Run the unittests by executing:

		$ python test_app.py

## API Reference

### Getting Started
-Base URL: This app can be run locally at http://127.0.0.1:5000/. It can be live tested at [https://fsnd-capstone-sspring963.herokuapp.com](https://fsnd-capstone-sspring963.herokuapp.com/).
-Authentication: This application requires authentication from AUTH0

### Error Handling

Errors are returned as JSON objects in the following format:

	{
		'success': False,
		'error': 400,
		'message': "Bad Request"
	}

The api will return these types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 422: Unprocessable Entity
- 500: Internal Server Error

### Endpoints

GET '/actors'
- General: Fetches all of the actors and returns their gender, id and, name.
- Request Arguments: None
- Sample:
		curl --location --request GET 'https://fsnd-capstone-sspring963.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q'
- Returns:
{
    "actors":[
        {
            "gender":"male",
            "id":1,
            "name":"Orlando Bloom"
        },
        {
            "gender":"male",
            "id":3,
            "name":"Brad Pitt"
        },
        {
            "gender":"male",
            "id":4,
            "name":"Brad Pitt"
        },
        {
            "gender":"male",
            "id":5,
            "name":"Brad Pitt"
        }
    ],
    "success":true
}

GET '/movies'
- General: Fetches all of the movies and returns their actor id, id, release date, and title.
- Request Arguments: None
- Sample:
curl --location --request GET 'https://fsnd-capstone-sspring963.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q'
- Returns:
{
   "movies":[
      {
         "actor_id":1,
         "id":3,
         "release_date":"Fri, 08 Jan 1993 00:00:00 GMT",
         "title":"Jurassic Park"
      },
      {
         "actor_id":1,
         "id":4,
         "release_date":"Fri, 08 Jan 1993 00:00:00 GMT",
         "title":"Jurassic Park"
      },
      {
         "actor_id":1,
         "id":1,
         "release_date":"Thu, 11 Nov 2004 00:00:00 GMT",
         "title":"Troy"
      }
   ],
   "success":true
}

POST '/actors'
- General: Creates a new actor that is added to actors. Returns actor's information.
- Request arguments: gender, name, age
- Sample: 
curl --location --request POST 'https://fsnd-capstone-sspring963.herokuapp.com/actors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q' \
--data-raw '{
    "name": "Brad Pitt",
    "age": 56,
    "gender": "male"
}'
- Returns:
{
   "movies":{
      "gender":"male",
      "id":6,
      "name":"Brad Pitt"
   },
   "success":true
}

POST '/movies'
- General: Creates a new movie that is added to movies. Returns movie's information.
- Request arguments: title, release_date, actor_id
- Sample:
curl --location --request POST 'https://fsnd-capstone-sspring963.herokuapp.com/movies' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q' \
--data-raw '{
    "title": "Jurassic Park",
    "release_date": "1993-01-08",
    "actor_id": 1
}'
- Return:
{
   "movies":{
      "actor_id":1,
      "id":5,
      "release_date":"Fri, 08 Jan 1993 00:00:00 GMT",
      "title":"Jurassic Park"
   },
   "success":true
}

PATCH '/movies/<int:id>'
- General: Updates information about a movie.
- Request arguments: id, optional: title, release_date, actor_id
- Sample:
curl --location --request PATCH 'https://fsnd-capstone-sspring963.herokuapp.com/movies/3' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q' \
--data-raw '{
    "title": "Troy",
    "release_date": "2004-11-11"
}'
- Return:
{
   "movie":{
      "actor_id":1,
      "id":3,
      "release_date":"Thu, 11 Nov 2004 00:00:00 GMT",
      "title":"Troy"
   },
   "success":true
}
 
PATCH '/actors/<int:id>'
- General: Updates information about actor.
- Request Arguments: id, optional: name, gender, age
- Sample:
curl --location --request PATCH 'https://fsnd-capstone-sspring963.herokuapp.com/actors/1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q' \
--data-raw '{
    "name": "Orlando Bloom"
}'
- Return:
{
   "actor":{
      "gender":"male",
      "id":1,
      "name":"Orlando Bloom"
   },
   "success":true
}

DELETE '/movies/<int:id>'
- General: Deletes the specified movie.
- Request Arguments: Movie id
- Sample:
curl --location --request DELETE 'https://fsnd-capstone-sspring963.herokuapp.com/movies/3' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q'
- Return:
{
   "delete":3,
   "success":true
}

DELETE '/actors/<int:id>
- General: Deletes the specified actor.
- Request Arguments: Actor id
- Sample: 
curl --location --request DELETE 'https://fsnd-capstone-sspring963.herokuapp.com/actors/5' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVjb21YNFNmVHAtdk95eFZuRlBnbCJ9.eyJpc3MiOiJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQzODY4NzgwMTUwMDA2MjUzNDUiLCJhdWQiOlsibW92aWUiLCJodHRwczovL2Rldi1seXl6cDY2aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjAzNTAxMzM3LCJleHAiOjE2MDM1ODc3MzcsImF6cCI6IlcxZWM4UkxMWEcxdlVhV3pNbWJzbHAyNE84TWJyMlVMIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.dzKaorpe-VSCT2kyTsv3Paa6krLFRaZTAt1fetelESqdwCVAjPwb6UJ50prA1jfULNsS6bENBsHXOXkUsD4Be29Us3v4-FTs3qKub2M68VcWyvKvKDj2Oap_OsOMnCl-IbYNstbM4q3HSFuavRDHZ3MWAUx8hkilyu1HnHIhy9S4MRv65bPVrlSVdMSyYwKLS9DgjFWPnkzOOkRB4ltZ5oQPsGhxB8Wz1-q__Q7IDx_bZ3Ti2aMZ74J1OT8lDDexUmZUhhV8YcrsoqOdbYNEhKOX4WA1pGWSrOYmMUkfcFtqbGQUCm9tuAWrDWXloMiXt31lkJecAq3_dMNYxv317Q'
- Return:
{
   "delete":5,
   "success":true
}

