import unittest
from models.city import City
"""this is tests for city class"""


class TestCity(unittest.TestCase):
    """city class tests"""
    def test_city_creation(self):
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_city_name(self):
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_city_state_id(self):
        city = City()
        city.state_id = "123"
        self.assertEqual(city.state_id, "123")


if __name__ == '__main__':
    unittest.main()
