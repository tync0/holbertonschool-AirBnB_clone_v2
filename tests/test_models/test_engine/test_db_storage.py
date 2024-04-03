#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage, type_of_storage


@unittest.skipIf(type_of_storage != "db", "Storage type: Database")
class TestDBStorage(unittest.TestCase):
    """ class to test the database storage method """

    def test_all(self):
        """  """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
