#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.test_city = City(state_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b",
                              name="test")

    def test_state_id(self):
        """ """
        self.assertEqual(type(self.test_city.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.test_city.name), str)
