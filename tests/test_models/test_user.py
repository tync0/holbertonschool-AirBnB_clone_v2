#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.test_user = User(first_name='test',
                              last_name='test',
                              email='test@test.com',
                              password='12345')

    def test_first_name(self):
        """ """
        self.assertEqual(type(self.test_user.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(self.test_user.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(self.test_user.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(self.test_user.password), str)
