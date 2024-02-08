#!/usr/bin/python3
""" TESTING file definition"""
import unittest
from models.base_model import BaseModel
from models.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    """FileStorage class TESTS to sure it's working"""

    def setUp(self):
        """Set up TESTS"""
        self.file_path = "test.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down TESTS"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_instance_creation(self):
        """instance TESTS"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_method(self):
        """all method TESTS"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_method(self):
        """the new method TESTS"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertTrue(obj.__class__.__name__ in self.storage._FileStorage__objects.keys())

    def test_save_method(self):
        """save method TESTS"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_method(self):
        """reload method TESTS"""
        obj = BaseModel()
        obj.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertTrue(obj.__class__.__name__ in self.storage._FileStorage__objects.keys())

if __name__ == "__main__":
    unittest.main()
