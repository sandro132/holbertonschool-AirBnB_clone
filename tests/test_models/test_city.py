import unittest
from models.city import City
from datetime import datetime
from time import sleep


class CityTest(unittest.TestCase):
    def test_state_id_is_string(self):
        self.assertEqual(str, type(City.state_id))

    def test_name_is_string(self):
        self.assertEqual(str, type(City.name))

    def test_unique_id(self):
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_is_instance(self):
        self.assertIsInstance(City().created_at, datetime)

    def test_updated_at_is_instance(self):
        self.assertIsInstance(City().updated_at, datetime)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_created_at_is_earlier(self):
        instance1 = City()
        sleep(0.2)
        instance2 = City()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_updated_at_is_earlier(self):
        instance1 = City()
        sleep(0.2)
        instance2 = City()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()

