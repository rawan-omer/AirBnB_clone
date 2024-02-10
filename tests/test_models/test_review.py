#!/usr/bin/python3
"""Review class for TESTING review file"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """TESTING Review class"""

    def test_instance_creation(self):
        """TESTING the instance"""
        var = Review()
        self.assertIsInstance(var, Review)

    def test_attributes_initialization(self):
        """TESTING the attributes"""
        rev = Review()
        self.assertEqual(rev.place_id, "")
        self.assertEqual(rev.user_id, "")
        self.assertEqual(rev.text, "")

    def test_setting_and_getting_attributes(self):
        """set and get TESTING"""
        review = Review()
        review.place_id = "52345"
        review.user_id = "57890"
        review.text = "our test review."

        self.assertEqual(review.place_id, "52345")
        self.assertEqual(review.user_id, "57890")
        self.assertEqual(review.text, "our test review.")


if __name__ == "__main__":
    unittest.main()
