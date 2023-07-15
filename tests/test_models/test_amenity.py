#!/usr/bin/python3
"""
Unittest for Amenity
"""

import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """
    Class test amenity
    """
    def test_instance(self):
        """
        Check instance of Amenity
        """
        self.assertIsInstance(Amenity(), Amenity)

    def test_name(self):
        """
        Test name of amenity
        """
        self.assertTrue(hasattr(Amenity, "name"), True)

    def test_createdat(self):
        """
        Check created at
        """
        self.assertTrue(hasattr(Amenity(), "created_at"), True)

    def test_updatedat(self):
        """
        Check update at
        """
        self.assertTrue(hasattr(Amenity(), "updated_at"), True)

    def test_id(self):
        """
        Test for id
        """
        self.assertTrue(hasattr(Amenity(), "id"), True)

    def test_to_dict(self):
        """
        Check dict
        """
        self.assertTrue(hasattr(Amenity(), "to_dict"), True)


if __name__ == "__main__":
    unittest.main()
