#!/usr/bin/python3
"""
Unittest session for amenity.py
"""

import unittest
from unittest import mock
from models import amenity

Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """ Test Amenity class """
    def setUp(self):
        """ Set instance for class tests """
        self.amenity = Amenity()

    def test_init(self):
        """ Test base class instantiation """
        self.assertIsInstance(self.amenity, Amenity)

    def test_init_att(self):
        """ test if initial attributes are set up """
        amenity_str = str(self.amenity)
        amenity_lst = ['id', 'created_at', 'updated_at']
        count = 0
        for word in amenity_lst:
            if word in amenity_str:
                count += 1
        self.assertEqual(3, count)

    def test_class_attr(self):
        """ Test class attribute pass as kwarg """
        amenity_class = Amenity(__class__='Test', id='1234567890987654321')
        self.assertEqual(type(amenity_class), Amenity)

    def test_kwargs(self):
        """ Test for attributes pass by kwargs """
        k_amenity = Amenity(name="Test_Model", number=42)
        dict_kamenity = k_amenity.to_dict()
        test_attr = ['name',
                     'number',
                     '__class__'
                     ]
        real_attr = list(dict_kamenity.keys())
        self.assertCountEqual(real_attr, test_attr)

    @mock.patch('models.storage')
    def test_save(self, mock_engine):
        """ Test base save method without models.storage method"""
        init_updated_at = self.amenity.updated_at
        self.amenity.save()
        last_updated_at = self.amenity.updated_at
        self.assertNotEqual(init_updated_at, last_updated_at)
        self.assertTrue(mock_engine.save.called)

    def test_to_dict(self):
        """ Test dictionary conversion creating new key/value pairs """
        self.amenity.name = "Test_Model"
        self.amenity.number = 42
        dict_test = self.amenity.to_dict()
        test_attr = ['id',
                     'name',
                     'number',
                     'created_at',
                     'updated_at',
                     '__class__'
                     ]
        real_attr = list(dict_test.keys())
        self.assertCountEqual(real_attr, test_attr)

    def test_to_dict_values(self):
        """ Test dict values """
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.amenity.name = "Test_Model"
        self.amenity.number = 42
        dict_test = self.amenity.to_dict()
        self.assertEqual(dict_test['name'], "Test_Model")
        self.assertEqual(dict_test['number'], 42)
        self.assertEqual(dict_test['__class__'], "Amenity")
        self.assertEqual(dict_test['created_at'],
                         self.amenity.created_at.strftime(time_fmt))
        self.assertEqual(dict_test['updated_at'],
                         self.amenity.updated_at.strftime(time_fmt))

    def test_str(self):
        """ Test string method """
        test_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(test_str, str(self.amenity))

    def test_name_attr(self):
        """ Test if name is an attribute of Amenity """
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")
        self.amenity.name = "Holbertonlandia"
        self.assertEqual(self.amenity.name, "Holbertonlandia")


if __name__ == '__main__':
    unittest.main()
