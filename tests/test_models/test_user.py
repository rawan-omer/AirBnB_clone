#!/usr/bin/python3
"""User class's definition"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """TESTING the User class"""

    def test_instance_creation(self):
        """TESTING the instance"""
        var = User()
        self.assertIsInstance(var, User)

    def test_attributes(self):
        """TESTING the attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_setting_and_getting_attributes(self):
        """more TESTS"""
        user = User()
        user.email = "testing@example.com"
        user.password = "my_password123"
        user.first_name = "rawan"
        user.last_name = "omer"

        self.assertEqual(user.email, "testing@example.com")
        self.assertEqual(user.password, "my_password123")
        self.assertEqual(user.first_name, "rawan")
        self.assertEqual(user.last_name, "omer")

if __name__ == "__main__":
    unittest.main()
