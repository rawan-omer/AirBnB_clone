import unittest
from models.amenity import Amenity
"""test module for Amenity class"""


class TestAmenity(unittest.TestCase):
    """Amenity class tests"""
    def test_amenity_creation(self):
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_amenity_name(self):
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_invalid_name(self):
        with self.assertRaises(TypeError):
            amenity = Amenity()
            amenity.name = 123  # Name should be a string


if __name__ == '__main__':
    unittest.main()
