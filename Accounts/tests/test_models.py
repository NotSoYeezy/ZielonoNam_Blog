from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password



class TestUserModel(TestCase):
    
    def test_creating_user_successfull(self):
        """Testing if user can be successfully created"""
        user_data = {
            'username': 'TestUser',
            'email': 'test@test.pl',
            'password': 'testpassword'
        }

        user = get_user_model().objects.create(username=user_data['username'], email=user_data['email'])
        user.set_password(user_data['password'])

        self.assertEqual(user.email, user_data['email'])
        self.assertEqual(user.username, user_data['username'])
        self.assertTrue(user.check_password(user_data['password']))
        