import unittest
from models.state import State
from datetime import datetime
from time import sleep


class StateTest(unittest.TestCase):
    def test_name_is_string(self):
        self.assertEqual(str, type(State.name))

    def test_unique_id(self):
        instance1 = State()
        instance2 = State()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_is_instance(self):
        self.assertIsInstance(State().created_at, datetime)

    def test_updated_at_is_instance(self):
        self.assertIsInstance(State().updated_at, datetime)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_created_at_is_earlier(self):
        instance1 = State()
        sleep(0.2)
        instance2 = State()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_updated_at_is_earlier(self):
        instance1 = State()
        sleep(0.2)
        instance2 = State()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()

