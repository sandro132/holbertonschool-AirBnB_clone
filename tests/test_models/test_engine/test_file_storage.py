#!/usr/bin/python3
"""
Unittest for file_storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity


class test_file_storage(unittest.TestCase):
    """
    Test for file_storage
    """
    def test_object(self):
        """
        Check instance
        """
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_file_path(self):
        """
        Check untance attribute of BaseModel
        """
        self.assertFalse(hasattr(FileStorage(), "__file_path"), False)

    def test_initializes(self):
        """
        initialize storage
        """
        self.assertEqual(type(storage), FileStorage)

    def test_private_str(self):
        """
        Check private string
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_private_dic(self):
        """
        Check private dic
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_for_same_type(self):
        """
        Testing that storage same type of dict
        """
        self.assertEqual(dict, type(storage.all()))

    def test_file_inst_no_arg(self):
        """
        Check instance with not args
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_inst_with_arg(self):
        """
        Check instance with args
        """
        with self.assertRaises(TypeError):
            FileStorage(None)


class test_file_storage_save(unittest.TestCase):
    """
    Tests for method save
    """
    def test_method_save(self):
        """
        Check if save is a method of file_inst
        """
        self.assertTrue(hasattr(FileStorage(), "save"), True)

    def test_save(self):
        """
        Check for method save
        """
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        storage.new(Amenity())
        storage.save()
        storage.reload()
        endic = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + BaseModel().id, endic)
        self.assertIn("User." + User().id, endic)
        self.assertIn("Place." + Place().id, endic)
        self.assertIn("Amenity." + Amenity().id, endic)


class file_storage_all(unittest.TestCase):
    """
    Class for tests method
    """
    def test_all_returns_dict(self):
        """
        Check if all return FileStorage.__objects attr
        """
        dic = FileStorage().all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, FileStorage()._FileStorage__objects)

    def test_method_all(self):
        """
        Check if all is a method of file_inst
        """
        self.assertTrue(hasattr(FileStorage(), "all"), True)

    def test_all_arg(self):
        """
        Testing all args arg
        """
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_all_arg(self):
        """
        Testing all args arg
        """
        with self.assertRaises(TypeError):
            storage.all(None)


class file_storage_new(unittest.TestCase):
    """
    class for method new
    """
    def test_new(self):
        """
        Test new with instances
        """
        storage.new(BaseModel())
        storage.new(User())
        storage.new(Place())
        storage.new(Amenity())
        self.assertIn("BaseModel." + BaseModel().id, storage.all().keys())
        self.assertIn(BaseModel(), storage.all().values())
        self.assertIn("User." + User().id, storage.all().keys())
        self.assertIn(User(), storage.all().values())
        self.assertIn("Place." + Place().id, storage.all().keys())
        self.assertIn(Place(), storage.all().values())
        self.assertIn("Amenity." + Amenity().id, storage.all().keys())
        self.assertIn(Amenity(), storage.all().values())

    def test_method_new(self):
        """
        Check if new is a method of file_inst
        """
        self.assertTrue(hasattr(FileStorage(), "new"), True)

    def test_new_args(self):
        """
        Checking new with arguments
        """
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_new_none(self):
        """
        Checking new with none
        """
        with self.assertRaises(AttributeError):
            storage.new(None)


class file_storage_reload(unittest.TestCase):
    """
    test for method reload
    """
    def test_method_reload(self):
        """
        Check if reload is a method of file_inst
        """
        self.assertTrue(hasattr(FileStorage(), "reload"), True)

    def test_for_reload(self):
        """
        Check if reload is a method of file_inst
        """
        self.assertTrue(hasattr(FileStorage(), "reload"), True)

    def test_reload_args(self):
        """
        Chesk reaload with arguments
        """
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
