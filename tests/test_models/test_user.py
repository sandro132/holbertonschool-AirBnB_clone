import unittest
from models.user import User
from datetime import datetime
from time import sleep


class UserTest(unittest.TestCase):
    def test_email_is_string(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_string(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_string(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_string(self):
        self.assertEqual(str, type(User.last_name))

    def test_unique_id(self):
        instance1 = User()
        instance2 = User()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_is_instance(self):
        self.assertIsInstance(User().created_at, datetime)

    def test_updated_at_is_instance(self):
        self.assertIsInstance(User().updated_at, datetime)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_created_at_is_earlier(self):
        instance1 = User()
        sleep(0.2)
        instance2 = User()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_updated_at_is_earlier(self):
        instance1 = User()
        sleep(0.2)
        instance2 = User()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()
