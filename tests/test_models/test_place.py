#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.testplace = Place(city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b",
                               user_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b",
                               name="test",
                               description="test",
                               number_rooms=5,
                               number_bathrooms=3,
                               max_guest=4,
                               price_by_night=150,
                               latitude=13.3,
                               longtitude=13.3,
                               amenity_ids=[])

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.testplace.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.testplace.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.testplace.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(self.testplace.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(self.testplace.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(self.testplace.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(self.testplace.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(self.testplace.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(self.testplace.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(self.testplace.latitude), float)

    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(self.testplace.amenity_ids), list)
