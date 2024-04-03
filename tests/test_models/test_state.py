#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
        self.test_state = State(name="test")

    def test_name3(self):
        """ """
        self.assertEqual(type(self.test_state.name), str)
