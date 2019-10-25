import os, unittest
from mongoengine import *
from app import app
from data.actor import Actor
from data.models import connectToDB, movie_stats 
 
class BasicTests(unittest.TestCase):
 
    # executed prior to each test
    def setUp(self):
        connectToDB()

        self.app = app.test_client()
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        disconnect('movie_db')

    def test_db_connection(self):
        movieLists = movie_stats.objects(actor_1_name__="50 Cent")
        self.assertIn('actor_1_name', movieLists[0])

    def test_actor_initialization(self):
        testActor = Actor("Faraz")
        
        self.assertIsInstance(testActor, Actor)
        self.assertIn('Faraz', testActor.name)
        self.assertEqual(0, testActor.facebook_likes)
 
    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_top_stats_page(self):
        response = self.app.get('/api/top_stats', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'top_ten_genres', response.data)

    def test_get_actors_page(self):
        response = self.app.get('/api/get_actors', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b',"A. Michael Baldwin","A.J. Buckley",', response.data)

    def test_actor_stats(self):
        response = self.app.get('/api/50 Cent', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"actor_name":"50 Cent"', response.data)
 
if __name__ == "__main__":
    unittest.main()

