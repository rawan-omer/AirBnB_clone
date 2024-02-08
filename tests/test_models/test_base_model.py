import unittest
from models.base_model import BaseModel
"""this is test file for BaseModel class"""


class TestBaseModel(unittest.TestCase):
    """test BaseModel class"""
    def test_base_model_creation(self):
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_base_model_str(self):
        base_model = BaseModel()
        self.assertTrue(str(base_model).startswith("[BaseModel]"))

    def test_base_model_save(self):
        base_model = BaseModel()
        created_at_before_save = base_model.created_at
        base_model.save()
        self.assertNotEqual(created_at_before_save, base_model.updated_at)

    def test_base_model_to_dict(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn('__class__', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)


if __name__ == '__main__':
    unittest.main()
