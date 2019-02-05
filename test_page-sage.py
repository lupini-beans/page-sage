import os
import tempfile

#import pytest
import unittest

from app import app


class BasicRouteTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    #########################
    ## Landing Page Routes ##
    #########################

    def test_landing_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_welcome_page(self):
        response = self.app.get('/welcome', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

  
    ##################
    ## AuthN Routes ##
    ##################

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)


    #################
    ## User Routes ##
    #################

    def test_user_page(self):
        response = self.app.get('/user')
        self.assertEqual(response.status_code, 200)

    def test_profile_page(self):
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 200)

    def test_user_book(self):
        response = self.app.get('/user/book')
        self.assertEqual(response.status_code, 200)

    def test_my_shelf(self):
        response = self.app.get('/my-shelf')
        self.assertEqual(response.status_code, 200)

    def test_user_search(self):
        response = self.app.get('/user/search')
        self.assertEqual(response.status_code, 200)

    def test_user_settings(self):
        response = self.app.get('user/settings')
        self.assertEqual(response.status_code, 200)


    #####################
    ## Bookclub Routes ##
    #####################

    def test_bookclub(self):
        response = self.app.get('/bookclub')
        self.assertEqual(response.status_code, 200)

    def test_club(self):
        response = self.app.get('/club')
        self.assertEqual(response.status_code, 200)

    def test_forums(self):
        response = self.app.get('/bookclub/forums')
        self.assertEqual(response.status_code, 200)

    def test_forum(self):
        response = self.app.get('/bookclub/forum')
        self.assertEqual(response.status_code, 200)

    def test_bookclub_shelf(self):
        response = self.app.get('/bookclub/shelf')
        self.assertEqual(response.status_code, 200)

    def test_bookclub_bookshelf(self):
        response = self.app.get('/bookclub/bookshelf')
        self.assertEqual(response.status_code, 200)

    def test_bookclub_suggestions(self):
        response = self.app.get('/bookclub/suggestions')
        self.assertEqual(response.status_code, 200)

    def test_bookclub_book(self):
        response = self.app.get('/bookclub/book')
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
