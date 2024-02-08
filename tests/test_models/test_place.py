import unittest
from models.place import Place
""" Place class Test"""


class TestPlace(unittest.TestCase):
    """TestPlace class"""
    def test_place_creation(self):
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_place_attributes(self):
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Cozy Apartment"
        place.description = "A beautiful apartment with stunning views."
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["1", "2", "3"]

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(
                place.description, "A beautiful apartment with stunning views."
                )
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    def test_place_invalid_city_id(self):
        with self.assertRaises(TypeError):
            place = Place()
            place.city_id = 123  # City ID should be a string

    def test_place_invalid_latitude(self):
        with self.assertRaises(TypeError):
            place = Place()
            place.latitude = "invalid"


if __name__ == '__main__':
    unittest.main()
