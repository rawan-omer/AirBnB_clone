#!/usr/bin/python3
"""our test file definition"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """State class"""

    def test_instance_creation(self):
        """TESTS for instance"""
        instance = State()
        self.assertIsInstance(instance, State)

    def test_attributes_initialization(self):
        """TESTS for attributes"""
        state = State()
        self.assertEqual(state.name, "")

    def test_setting_and_getting_attributes(self):
        """TESTS"""
        state = State()
        state.name = "rawan"

        self.assertEqual(state.name, "rawan")


if __name__ == "__main__":
    unittest.main()
