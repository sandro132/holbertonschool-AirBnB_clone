import unittest
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    def test_instance(self):
        self.assertIsInstance(Amenity(), Amenity)

    def test_name_attribute(self):
        self.assertTrue(hasattr(Amenity, "name"))

    def test_created_at_attribute(self):
        self.assertTrue(hasattr(Amenity(), "created_at"))

    def test_updated_at_attribute(self):
        self.assertTrue(hasattr(Amenity(), "updated_at"))

    def test_id_attribute(self):
        self.assertTrue(hasattr(Amenity(), "id"))

    def test_to_dict_method(self):
        self.assertTrue(hasattr(Amenity(), "to_dict"))


if __name__ == "__main__":
    unittest.main()

