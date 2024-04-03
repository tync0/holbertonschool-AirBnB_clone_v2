#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.test_review = Review(place_id="1",
                                  user_id="1",
                                  text="test")

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.test_review.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.test_review.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.test_review.text), str)
