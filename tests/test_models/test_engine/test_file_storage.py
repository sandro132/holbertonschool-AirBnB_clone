import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity


class FileStorageTest(unittest.TestCase):
    def setUp(self):
        if hasattr(storage, "_FileStorage__objects"):
            storage._FileStorage__objects = {}

    def tearDown(self):
        if hasattr(storage, "_FileStorage__objects"):
            del storage._FileStorage__objects

    def test_object_instance(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_file_path_attribute(self):
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_storage_initialization(self):
        self.assertEqual(type(storage), FileStorage)

    def test_private_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_private_objects_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all_returns_dict(self):
        dictionary = FileStorage().all()
        self.assertEqual(type(dictionary), dict)
        self.assertIs(dictionary, FileStorage()._FileStorage__objects)

    def test_new_method(self):
        self.assertTrue(hasattr(FileStorage(), "new"))

    def test_save_method(self):
        self.assertTrue(hasattr(FileStorage(), "save"))

    def test_reload_method(self):
        self.assertTrue(hasattr(FileStorage(), "reload"))

    def test_new_method_with_instances(self):
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

    def test_save_and_reload(self):
        storage.new(BaseModel())
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + BaseModel().id, storage.all().keys())

if __name__ == "__main__":
    unittest.main()
